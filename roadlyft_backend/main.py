from flask import Flask, request, jsonify, redirect, render_template, send_from_directory
from flask_cors import CORS
import time, random
import datetime, googlemaps
from geopy.distance import geodesic

app = Flask(__name__)
CORS(app, supports_credentials=True)

gmaps = googlemaps.Client(key='AIzaSyCFR4iDnFaRzaDGHzcARIy71DkgZGlDrb0')

usr_d: dict = {}
oth_usr_data: dict = {}
deck_handler: dict = {'8830998140': ['zqsyumos', '21:56:16 07/09/24', True, '21:56:16 07/09/24', '21:56:16 07/09/24'],
                      '9423868113': ['rdwqvsgt', '22:07:37 07/09/24', True, '22:07:37 07/09/24', '22:07:37 07/09/24']}
char_a_z = "abcdefghijklmnopqrstuvwxyz"
# route = {'8830998140': [
#     ['Kolhapur, Maharashtra, India', 'Pune, Maharashtra, India', {'lat': 16.7049873, 'lng': 74.24325270000001},
#      {'lat': 18.5204303, 'lng': 73.8567437}, 0, '1', '2024-07-19', '13:28', '2024-07-19 18:07', [], [
#          ['9423868113', 'Karad, Maharashtra, India', 'Satara, Maharashtra, India',
#           {'lat': 17.277693, 'lng': 74.1843535}, {'lat': 17.6804639, 'lng': 74.018261}, '1']], '1151.47']]}
# p_route = {'9423868113': '8830998140'}

p_route = {}
route = {}
trust_ = []

with open("enc/pyc_cache", "r") as pycache:
    exec(pycache.read())

with open("enc/trust_me", "r") as trust_me:
    exec(trust_me.read())

with open("enc/locations", "r") as loc:
    locations = loc.read().split("\n")


def deck_create_instance(usr_mobile):
    """Creates the deck instance for the advanced access to the user. This provides the additional security features."""
    current_date = datetime.datetime.now()
    cur_dat_time = current_date.strftime("%H:%M:%S %D")

    while True:
        temp_de = ""
        for i in range(8):
            temp_de = temp_de + char_a_z[random.randint(0, len(char_a_z) - 1)]
        if deck_handler.get(usr_mobile):
            if deck_handler[usr_mobile][0] != temp_de:
                deck_handler[usr_mobile] = [temp_de, cur_dat_time, True, cur_dat_time, cur_dat_time]
                break
        else:
            deck_handler[usr_mobile] = [temp_de, cur_dat_time, True, cur_dat_time, cur_dat_time]
            break
    print("deck_handler: ", deck_handler)
    return temp_de


def create_user_space(usr_name, usr_mobile, usr_password) -> bool or str:
    """:returns str: when user already exist
    :returns bool True: when account is created
    :returns bool False: invalid former parameters"""
    if len(usr_name) > 1 and len(usr_mobile) == 10 and len(usr_password) >= 4:
        if usr_d.get(usr_mobile):
            return "USR_EST"
        else:
            usr_d[usr_mobile] = usr_password
            oth_usr_data[usr_mobile] = [usr_name, 0]
            return True
    return False


def valid_usr_req(auth_toc_usr) -> list:
    if len(auth_toc_usr) != 8:
        return [False]
    for i in deck_handler:
        if auth_toc_usr == deck_handler[i][0] and deck_handler:
            current_date = datetime.datetime.now()
            cur_dat_time = current_date.strftime("%H:%M:%S %D")
            deck_handler[i][4] = cur_dat_time
            print(deck_handler)
            return [True, i]
    return [False]


def get_route_points(origin, destination, route_index=0):
    directions_result = gmaps.directions(origin, destination, mode="driving", alternatives=True)
    if directions_result and len(directions_result) > route_index:
        route = directions_result[route_index]
        route_points = []
        has_tolls = False

        for leg in route['legs']:
            for step in leg['steps']:
                start_location = step['start_location']
                end_location = step['end_location']
                route_points.append((start_location['lat'], start_location['lng']))
                route_points.append((end_location['lat'], end_location['lng']))

                if 'toll' in step.get('html_instructions', '').lower():
                    has_tolls = True

        return route_points, route['legs'][0]['duration']['value'], route['legs'][0]['distance']['value'], has_tolls
    return [], None, None, False


def is_point_near_route(point, route_points, max_distance=50) -> (bool, int):
    min_dist, ro_pt = 50, 0
    for route_point in route_points:
        # print(geodesic(point, route_point).kilometers)
        km = geodesic(point, route_point).kilometers
        if km <= max_distance:
            if km < min_dist:
                min_dist = km
                ro_pt = route_point
    if min_dist < 50:
        return True, min_dist, ro_pt
    return False, 0, None


def get_travel_time_between_points(point1, point2):
    result = gmaps.distance_matrix(origins=[point1], destinations=[point2], mode="driving")
    if result['rows'] and result['rows'][0]['elements']:
        element = result['rows'][0]['elements'][0]
        if element['status'] == 'OK':
            return element['duration']['value'], element['distance']['value']
    return None, None


def add_driver_ride(usr_id, pickup_name_d, dropoff_name_d, pickup_latlng_d, dropoff_latlng_d, route_indx, d_seats,
                    d_date, d_time, d_cost) -> (bool, str):
    global route

    start_time = datetime.datetime.strptime(d_date + " " + d_time, "%Y-%m-%d %H:%M")

    curr_time = datetime.datetime.now()
    print("current date: ", curr_time.strftime("%Y-%m-%d %H:%M"))
    if start_time < curr_time:
        return False, "Date or time selected is invalid."

    _, mins, l, toll = get_route_points(pickup_latlng_d, dropoff_latlng_d, route_indx)
    hours = mins // 3600
    mins = (mins % 3600) // 60
    time_to_add = datetime.timedelta(hours=hours, minutes=mins)
    end_time_obj = start_time + time_to_add
    end_time = end_time_obj.strftime("%Y-%m-%d %H:%M")

    val = valid_usr_req(usr_id)
    if val[0]:
        if route.get(val[1]):

            "The following 8 line of if if else statement are the limiter of ride."
            if len(route[val[1]]) > 0:
                temp_end_time = datetime.datetime.strptime(route[val[1]][0][8], "%Y-%m-%d %H:%M")

                if curr_time > temp_end_time:
                    route[val[1]].__delitem__(0)
                    # route[val[1]][0] = []
                else:
                    return False, "One ride is already published."
            "The above 8 line of if if else statement are the limiter of ride."

        mobile_number = val[1]
        if oth_usr_data[val[1]][1] == 2:
            if route.get(mobile_number) and len(route[mobile_number]) > 0:

                for r in route[mobile_number]:
                    previous_start_time = datetime.datetime.strptime(str(r[6]) + " " + str(r[7]),
                                                                     "%Y-%m-%d %H:%M")
                    previous_end_time = datetime.datetime.strptime(r[8], "%Y-%m-%d %H:%M")
                    if (start_time < previous_start_time < end_time_obj
                            or previous_start_time < start_time < previous_end_time):
                        return False, f"Time overlapping with ride scheduled from {r[0]} to {r[1]}."

                new_route = \
                    [pickup_name_d, dropoff_name_d, pickup_latlng_d, dropoff_latlng_d, route_indx, d_seats,
                     d_date, d_time, end_time, [], [], d_cost
                     ]
                route[mobile_number].append(new_route)
                print("route: ", route)
                return True, "Successfully scheduled ride."
            else:
                _, mins, l, toll = get_route_points(pickup_latlng_d, dropoff_latlng_d, route_indx)
                hours = mins // 3600
                mins = (mins % 3600) // 60

                print(mins, hours, mins)

                time_to_add = datetime.timedelta(hours=hours, minutes=mins)
                new_datetime_obj = start_time + time_to_add
                end_time = new_datetime_obj.strftime("%Y-%m-%d %H:%M")

                print("start time: ", start_time)
                print("end time: ", new_datetime_obj)

                route[mobile_number] = \
                    [
                        [pickup_name_d, dropoff_name_d, pickup_latlng_d, dropoff_latlng_d, route_indx, d_seats,
                         d_date, d_time, end_time, [], [], d_cost]
                    ]
                print("route: ", route)
                return True, "Successfully scheduled ride."
        else:
            return False, "Ride publishing not enabled. Please verify first."
    else:
        return False, "User invalid request."


@app.route("/backend-server")
def index():
    # client_ip = request.remote_addr
    return redirect("/")


@app.route("/backend-server/status")
def server_status():
    return request.user_agent.string


def detect_device(user_agent):
    # Check for common mobile device identifiers in the User-Agent string
    mobile_agents = [
        'iphone', 'ipad', 'android', 'blackberry', 'nokia', 'opera mini',
        'windows mobile', 'windows phone', 'iemobile', 'mobile'
    ]

    user_agent = user_agent.lower()

    if any(mobile_agent in user_agent for mobile_agent in mobile_agents):
        return 'Mobile'
    else:
        return 'Desktop'


@app.route("/backend-server/create_account", methods=["POST"])
def create_account():
    request_data = request.json
    usr_name = request_data['user_name'].strip()
    usr_mobile = request_data['mobile'].strip()
    usr_password = request_data['password']
    print(usr_name, usr_mobile, usr_password)

    if isinstance(usr_name, str) and isinstance(usr_mobile, str) and isinstance(usr_password, str) and len(
            usr_name) > 1 and len(usr_mobile) == 10 and len(usr_password) >= 4:
        acc_cre_res = create_user_space(usr_name, usr_mobile, usr_password)
        print("usr_d: ", usr_d)
        print("oth_usr_data: ", oth_usr_data)
        if isinstance(acc_cre_res, bool) and acc_cre_res == True:
            dec_inst = deck_create_instance(usr_mobile)
            print("Created account for: ", usr_name, usr_mobile, usr_password)
            return jsonify({"ACC_C_STAT": "SUCCESS", "dock-cid": dec_inst})
        elif isinstance(acc_cre_res, bool) and acc_cre_res == False:
            print("Failed to create account for: ", usr_name, usr_mobile, usr_password)
            return jsonify({"ACC_C_STAT": "FAILURE"})
        else:
            print("Duplicate account for: ", usr_name, usr_mobile, usr_password)
            return jsonify({"ACC_C_STAT": "DUPLICATE"})
    print("Failed to create account with the credentials: ", usr_name, usr_mobile, usr_password)
    return jsonify({"ACC_C_STAT": "FAILURE"})


@app.route("/backend-server/login", methods=["POST"])
def login():
    global usr_d
    data_received = request.json
    usr_mobile = data_received['mobile']
    usr_password = data_received['password']
    print(f"Trying to login with: ", usr_mobile, usr_password)
    if (isinstance(usr_mobile, str) and isinstance(usr_password, str) and len(usr_mobile) == 10
            and len(usr_password) >= 4):
        if usr_d.get(data_received['mobile']):
            if usr_d[data_received['mobile']] == data_received['password']:
                dec_inst = deck_create_instance(data_received['mobile'])
                response = jsonify({"LOGIN_STAT": "SUCCESS", "dock-cid": dec_inst})
                print("Successful login with: ", usr_mobile, usr_password)
                return response
            else:
                print("Failed login with: ", usr_mobile, usr_password)
                response = jsonify({"LOGIN_STAT": "FAILURE"})
                return response
        else:
            print("Failed login with: ", usr_mobile, usr_password)
            response = jsonify({"LOGIN_STAT": "FAILURE"})
            return response
    else:
        print("Failed login with: ", usr_mobile, usr_password)
        response = jsonify({"LOGIN_STAT": "FAILURE"})
        return response


@app.route("/backend-server/get_homepage_da", methods=["POST"])
def get_dash_dat():
    today = datetime.datetime.now().date().today()
    tomorrow = today + datetime.timedelta(days=1)
    day_after_tomorrow = tomorrow + datetime.timedelta(days=1)
    third_date = day_after_tomorrow + datetime.timedelta(days=1)
    forth_date = third_date + datetime.timedelta(days=1)

    request_body = request.json
    print("Requesting the homepage data with given request body: ", request_body)
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    loyalty = request_body["loyalty"]

    val = valid_usr_req(usr_id)
    if loyalty == "spawned%20uWSGI" and val[0] and usr_id == local_str:
        usr_name_d, driving_flag = oth_usr_data[val[1]][0: 2]
        if route.get(val[1]):
            if len(route[val[1]]) > 0:
                cur_time = datetime.datetime.now()
                end_time = datetime.datetime.strptime(route[val[1]][0][8], "%Y-%m-%d %H:%M")

                if cur_time > end_time:

                    for i in route[val[1]][0][10]:
                        if p_route[i[0]] == val[1]:
                            p_route.pop(i[0])

                    for i in route[val[1]][0][9]:
                        if p_route[i[0]] == val[1]:
                            p_route.pop(i[0])

                    route[val[1]].__delitem__(0)

                    # route[val[1]][0] = []
                    print("Removed expired route for ", val[1])
                    ride_stat = 0
                else:
                    ride_stat = 1
            else:
                ride_stat = 0
        else:
            ride_stat = 0

        book_stat = 0
        if p_route.get(val[1]):
            d_mob = p_route[val[1]]
            for ride in route[d_mob]:
                for r in ride[10]:
                    if r[0] == val[1]:
                        book_stat = 1
                        break
                for r in ride[9]:
                    if r[0] == val[1]:
                        book_stat = 2
                        break

        print("Successful returning the homepage data with given request body: ", request_body)
        return jsonify({"RESP_STAT": "SUCCESS", "TODAY": today.strftime("%d"), "TOMORROW": tomorrow.strftime("%d"),
                        "DATE_AFTER_TOMORROW": day_after_tomorrow.strftime("%d"),
                        "DAY_AFTER_TOMORROW": day_after_tomorrow.strftime("%A")[:3],
                        "THIRD_DATE": third_date.strftime("%d"), "THIRD_DAY": third_date.strftime("%A")[:3],
                        "FORTH_DATE": forth_date.strftime("%d"), "FORTH_DAY": forth_date.strftime("%A")[:3],
                        "USR_NAME": usr_name_d, "DRIVING_FLAG": driving_flag, "RIDE_STAT": ride_stat,
                        "BOOK_STAT": book_stat})

    else:
        print("Failed to respond with homepage data with given request body: ", request_body)
        return jsonify({"RESP_STAT": "FAILURE"})


@app.route("/backend-server/get_loc_da", methods=["POST"])
def get_locations():
    global locations
    request_body = request.json
    print("Requesting the location data with given request body: ", request_body)
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    if usr_id == local_str and valid_usr_req(usr_id):
        print("Successful returning the location data with given request body: ", request_body)
        return jsonify({"RESP_STAT": "SUCCESS", "LOC": locations})
    else:
        print("Failed returning the location data with given request body: ", request_body)
        return jsonify({"RESP_STAT": "FAILURE"})


@app.route("/backend-server/p_search_cabs", methods=['POST'])
def booking_passenger_s1():
    request_body = request.json
    print("Requesting to cabs route with given request body: ", request_body)
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    loyalty = request_body["loyalty"]
    pickup_latlng_p = request_body["pickup_latlng"]
    dropoff_latlng_p = request_body["dropoff_latlng"]
    seats = request_body["seats"]
    booking_date_thresh = "booking_date_thresh"
    print("pickup_latlng: ", pickup_latlng_p)
    val = valid_usr_req(usr_id)
    temp_cab_list = []
    if loyalty == "spawned%20uWSGI" and val[0] and usr_id == local_str:
        for r in route:

            if len(route[r]) > 0:
                for i in route[r]:
                    d_start_time = datetime.datetime.strptime(str(i[6]) + " " + str(i[7]),
                                                              "%Y-%m-%d %H:%M")
                    curr_time = datetime.datetime.now()
                    if curr_time < d_start_time:
                        rp, dist, tm, _ = get_route_points((i[2]['lat'], i[2]['lng']), (i[3]['lat'],
                                                                                        i[3]['lng']), int(i[4]))
                        ret_s, km_s, pt_s = is_point_near_route(route_points=rp,
                                                                point=(pickup_latlng_p["lat"], pickup_latlng_p["lng"]))
                        ret_e, km_e, pt_e = is_point_near_route(route_points=rp, point=(
                            dropoff_latlng_p["lat"], dropoff_latlng_p["lng"]))
                        if ret_s and ret_e and int(seats) <= (int(i[5]) - len(i[9])):
                            t_P_s, d_P_s = get_travel_time_between_points(rp[0], pt_s)
                            t_P_e, d_P_e = get_travel_time_between_points(pt_s, pt_e)
                            print("d_P_s, t_P_s: ", d_P_s, t_P_s)
                            print("d_P_e, t_P_e: ", d_P_e, t_P_e)
                            print(i)
                            actual_start = d_start_time + datetime.timedelta(seconds=t_P_s)
                            actual_end = actual_start + datetime.timedelta(seconds=t_P_e)
                            actual_distance = d_P_e / 1000
                            temp = [oth_usr_data[r][0], r, round(float(km_s), 2), round(float(km_e), 2),
                                    actual_start.strftime("%d %b %H:%M"), actual_end.strftime("%d %b %H:%M"),
                                    actual_distance, (int(i[5]) - len(i[9]))]
                            temp.extend(i)
                            temp_cab_list.append(temp)

        if len(temp_cab_list):
            print("Cabs for request: ", temp_cab_list)
            print("Successful returning to cabs route with given request body: ", request_body)
            return jsonify({"RESP_STAT": "SUCCESS", "CAB_LST": temp_cab_list})
        print("No cabs found for the request.")
        print("None return to cabs route with given request body: ", request_body)
        return jsonify({"RESP_STAT": "NONE"})
    else:
        print("Failed returning to cabs route with given request body: ", request_body)
        return jsonify({"RESP_STAT": "FAILURE"})


@app.route("/backend-server/p_book_cab", methods=['POST'])
def booking_passenger_s2():
    request_body = request.json
    print("Requesting to ride booking with given request body: ", request_body)
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    loyalty = request_body["loyalty"]
    d_mobile = request_body["driver_mbl"]
    d_origin = request_body["origin"]
    d_destination = request_body["destination"]
    pickup_name = request_body["pickup_name"]
    dropoff_name = request_body["dropoff_name"]
    pickup_latlng = request_body["pickup_latlng"]
    dropoff_latlng = request_body["dropoff_latlng"]
    seats = request_body['seats']

    val = valid_usr_req(usr_id)
    if loyalty == "spawned%20uWSGI" and val[0] and usr_id == local_str:
        if route.get(d_mobile):
            for _, r in enumerate(route[d_mobile]):
                if r[0] == d_origin and r[1] == d_destination:
                    start_time = datetime.datetime.strptime(str(r[6]) + " " + str(r[7]), "%Y-%m-%d %H:%M")
                    curr_time = datetime.datetime.now()
                    if start_time > curr_time:
                        route[d_mobile][_][10].append([val[1], pickup_name, dropoff_name, pickup_latlng,
                                                       dropoff_latlng, seats])
                        p_route[val[1]] = d_mobile
                        print("p_route: ", p_route)
                        print("Successful returning to ride booking with given request body: ", request_body)
                        return jsonify({"RESP_STAT": "SUCCESS"})
            print("Aborted ride booking (ride time or origin mismatched) with given request body: ", request_body)
            return jsonify({"RESP_STAT": "ABORTED"})
        else:
            print("Failed returning to ride booking with given request body: ", request_body)
            return jsonify({"RESP_STAT": "FAILURE"})

    else:
        print("Failed returning to ride booking with given request body: ", request_body)
        return jsonify({"RESP_STAT": "FAILURE"})


@app.route("/backend-server/d_post", methods=["POST"])
def ride_publish():
    request_body = request.json
    print("Requesting ride publish with given request body: ", request_body)
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    loyalty = request_body["loyalty"]

    pickup_name_d = request_body["pickup_name_d"]
    dropoff_name_d = request_body["dropoff_name_d"]
    pickup_latlng_d = request_body["pickup_latlng_d"]
    dropoff_latlng_d = request_body["dropoff_latlng_d"]
    route_indx = request_body["route_indx"]
    d_seats = request_body["d_seats"]
    d_date = request_body["d_date"]
    d_time = request_body["d_time"]
    d_cost = request_body["d_cost"]
    val = valid_usr_req(usr_id)
    if loyalty == "spawned%20uWSGI" and val[0] and usr_id == local_str:
        ret, msg = add_driver_ride(usr_id, pickup_name_d, dropoff_name_d, pickup_latlng_d, dropoff_latlng_d, route_indx,
                                   d_seats,
                                   d_date, d_time, d_cost)
        if ret:
            print("Successful returning ride publish with given request body: ", request_body)
            return jsonify({"RESP_STAT": "SUCCESS"})
        else:
            print("Aborted returning ride publish with given request body: ", request_body)
            return jsonify({"RESP_STAT": "ABORTED", "MSG": msg})
    else:
        print("Failed returning ride publish with given request body: ", request_body)
        return jsonify({"RESP_STAT": "FAILURE"})


@app.route("/backend-server/d_inride_content/<route_index>", methods=["POST"])
def in_ride_content(route_index):
    request_body = request.json
    print("Requesting in-ride data with given request body: ", request_body)
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    loyalty = request_body["loyalty"]
    route_index = int(route_index)

    val = valid_usr_req(usr_id)
    if loyalty == "spawned%20uWSGI" and val[0] and usr_id == local_str:
        route_info = route[val[1]][route_index]
        origin = route_info[0]
        destination = route_info[1]
        start_datetime = str(route_info[6]) + " " + str(route_info[7])
        seats = int(route_info[5])
        end_datetime = str(route_info[8])
        passenger_approved = route_info[9]
        passenger_request = route_info[10]

        passenger_approved_n = []
        passenger_request_n = []

        for i in passenger_approved:
            temp = [oth_usr_data[i[0]][0]]
            temp.extend(i)
            passenger_approved_n.append(temp)
            # passenger_approved_n.append(oth_usr_data[i][0])
        for j in passenger_request:
            temp = [oth_usr_data[j[0]][0]]
            temp.extend(j)
            passenger_request_n.append(temp)
            # passenger_request_n.append(oth_usr_data[j][0])

        route_info = [origin, destination, start_datetime, end_datetime, seats, passenger_approved_n,
                      passenger_request_n]
        print("Successful returning in-ride data with given request body: ", request_body)
        return jsonify({"RESP_STAT": "SUCCESS", "ROUTE_INFO": route_info})
    else:
        print("Failed returning in-ride data with given request body: ", request_body)
        return jsonify({"RESP_STAT": "FAILURE"})


@app.route("/backend-server/d_request_accept", methods=["POST"])
def request_accept_d():
    request_body = request.json
    print("Requesting passenger request acceptation with given request body: ", request_body)
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    loyalty = request_body["loyalty"]
    accept_req = request_body["passanger_request"]
    val = valid_usr_req(usr_id)
    if loyalty == "spawned%20uWSGI" and val[0] and usr_id == local_str:
        for _, r in enumerate(route[val[1]]):
            for __, i in enumerate(r[10]):
                print("i: ", i)
                print("accept_req: ", accept_req[1:])
                if accept_req[1:] == i:
                    route[val[1]][_][10].remove(i)
                    route[val[1]][_][9].append(i)
                    print("Successful returning passenger request acceptation with given request body: ", request_body)
                    return jsonify({"RESP_STAT": "SUCCESS"})

        print("Aborted returning passenger request acceptation with given request body: ", request_body)
        return jsonify({"RESP_STAT": "ABORTED"})
    else:
        print("Failed returning passenger request acceptation with given request body: ", request_body)
        return jsonify({"RESP_STAT": "FAILURE"})


@app.route("/backend-server/in_booking", methods=["POST"])
def in_booking():
    request_body = request.json
    print("Requesting in-booking data with given request body: ", request_body)
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    loyalty = request_body["loyalty"]
    val = valid_usr_req(usr_id)
    if loyalty == "spawned%20uWSGI" and val[0] and usr_id == local_str:
        curr_time = datetime.datetime.now()
        if route.get(p_route[val[1]]):
            d_mbl = p_route[val[1]]
            for _, ride in enumerate(route[d_mbl]):
                end_time = datetime.datetime.strptime(ride[8], "%Y-%m-%d %H:%M")
                if curr_time > end_time:
                    for r in route[d_mbl]:
                        for i in r[10]:
                            if p_route.get(i[0]):
                                p_route.pop(i[0])
                        for i in r[9]:
                            if p_route.get(i[0]):
                                p_route.pop(i[0])
                    route[d_mbl].pop(_)
                    print("Removed expired route for ", val[1])

        if p_route.get(val[1]):
            for ride in route[p_route[val[1]]]:
                for r in ride[10]:
                    if r[0] == val[1]:
                        start = r[1]
                        end = r[2]
                        seats = r[5]
                        print("Ride approval pending for: ", val[1], " by: ", p_route[val[1]])
                        print("Successfully returning in-booking data with given request body: ", request_body)
                        return jsonify({"RESP_STAT": "SUCCESS", "STAT": "PENDING", "ORG": start, "DEST": end,
                                        "SEATS": seats, "D_MOB": p_route[val[1]],
                                        "D_NAME": oth_usr_data[p_route[val[1]]][0]})

                for r in ride[9]:
                    if r[0] == val[1]:
                        start = r[1]
                        end = r[2]
                        seats = r[5]
                        print("Ride approved for: ", val[1], " by: ", p_route[val[1]])
                        print("Successfully returning in-booking data with given request body: ", request_body)
                        return jsonify({"RESP_STAT": "SUCCESS", "STAT": "APPROVED", "ORG": start, "DEST": end,
                                        "SEATS": seats, "D_MOB": p_route[val[1]],
                                        "D_NAME": oth_usr_data[p_route[val[1]]][0]})
        print("Ride completed for: ", val[1], " by: ", p_route[val[1]])
        return jsonify({"RESP_STAT": "SUCCESS", "STAT": "COMPLETED"})

    print("Failed to return in-booking data with given request body: ", request_body)
    return jsonify({"RESP_STAT": "FAILURE"})


@app.route("/backend-server/cancel_booking", methods=["POST"])
def cancel_booking_passenger():
    request_body = request.json
    print("Requesting booking cancellation with given request body: ", request_body)
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    loyalty = request_body["loyalty"]
    val = valid_usr_req(usr_id)
    if loyalty == "spawned%20uWSGI" and val[0] and usr_id == local_str:
        if p_route.get(val[1]):
            d_mob = p_route[val[1]]
            for _, ride in enumerate(route[d_mob]):
                for __, r in enumerate(ride[10]):
                    if r[0] == val[1]:
                        route[d_mob][_][10].pop(__)
                        p_route.pop(val[1])
        print("Successfully canceled booking  with given request body: ", request_body)
        return jsonify({"RESP_STAT": "SUCCESS"})
    print("Failed to cancel booking with given request body: ", request_body)
    return jsonify({"RESP_STAT": "FAILURE"})


@app.route("/backend-server/commit", methods=["GET"])
def commit():
    global usr_d, oth_usr_data
    print("Commiting data")
    with open("enc/pyc_cache", "w") as commit_file:
        commit_file.write(f"usr_d ={usr_d}\noth_usr_data = {oth_usr_data}")
    print("Data commited successfully")
    return jsonify({"RET_SATA": "SUCCESS"}), 200


@app.route("/backend-server/control-sys/classified/auth/admin-panel", methods=["GET"])
def admin_panel():
    user_agent = request.headers.get('User-Agent')
    print("Requesting admin panel with given user agent: ", user_agent)
    device_type = detect_device(user_agent)
    if device_type == "Desktop":
        return render_template("index.html")
    # return render_template("index.html")
    return redirect("/")


@app.route("/backend-server/akKokncIBiswen/NConessel/neOnSWEncZ/dat", methods=["POST"])
def admin_data_read_whole():
    global oth_usr_data, deck_handler
    request_body = request.json
    print("Requesting whole user data with given request body: ", request_body)
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    loyalty = request_body["loyalty"]

    val = valid_usr_req(usr_id)
    if loyalty == "spawned%20uWSGI" and val[0] and usr_id == local_str and val[1] in trust_:

        name_list, mobile_list, lst, roll = [], [], [], []
        for i in oth_usr_data:
            temp_dat = oth_usr_data[i]

            mobile_list.append(i)
            name_list.append(temp_dat[0])
            roll.append(temp_dat[1])
            if deck_handler.get(i):
                lst.append(deck_handler[i][4])
            else:
                lst.append("NAN")

        return jsonify({"RESP_STAT": "SUCCESS", "NAME": name_list, "MBL": mobile_list,
                        "LSTA": lst, "ROLL": roll})
    else:
        return jsonify({"RESP_STAT": "Failure"})


@app.route("/backend-server/akKojallwecswen/Naeno2ssel/nXLKEOnSlSXcZ/dat", methods=["POST"])
def admin_data_read_particular():
    request_body = request.json
    print("Requesting particular user data with given request body: ", request_body)
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    loyalty = request_body["loyalty"]
    mobile_num = request_body["MBL"]
    val = valid_usr_req(usr_id)
    if loyalty == "spawned%20uWSGI" and val[0] and usr_id == local_str and val[1] in trust_:
        if oth_usr_data.get(mobile_num):
            name = str(oth_usr_data[mobile_num][0])
            roll = oth_usr_data[mobile_num][1]
            if deck_handler.get(mobile_num):
                lsta = deck_handler[mobile_num][4]
            else:
                lsta = "NAN"
            return jsonify(
                {"RESP_STAT": "SUCCESS", "NAME": [name], "MBL": [str(mobile_num)], "LSTA": [lsta], "ROLL": [roll]})
    return jsonify({"RESP_STAT": "Failure"})


@app.route("/backend-server/ewonallweKNKE/NaenlklkmMsel/nXiocwNOnSlSXcZ/dat", methods=["POST"])
def admin_data_update_particular():
    request_body = request.json
    print("Requesting update in particular user data with given request body: ", request_body)
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    loyalty = request_body["loyalty"]
    mobile_num = request_body["MBL"]
    name = request_body["NME"]
    roll = request_body["RLL"]
    val = valid_usr_req(usr_id)
    if loyalty == "spawned%20uWSGI" and val[0] and usr_id == local_str and val[1] in trust_:
        if usr_d.get(mobile_num):
            try:
                oth_usr_data[mobile_num][0] = str(name)
                oth_usr_data[mobile_num][1] = int(roll)
                return jsonify({"RESP_STAT": "SUCCESS"})
            except:
                return jsonify({"RESP_STAT": "Failure"})
    return jsonify({"RESP_STAT": "Failure"})


@app.route("/backend-server/eioad/mofva", methods=["GET"])
def return_basecss_for_admin_panel():
    return send_from_directory(directory=".", path="static/base.css")


@app.route("/backend-server/cieow/ofiaea", methods=["GET"])
def return_maincss_for_admin_panel():
    return send_from_directory(directory=".", path="static/main.css")


@app.route("/backend-server/icon/Roadlyft_LOGO.png", methods=["GET"])
def return_logo_for_admin_panel():
    return send_from_directory(directory=".", path="static/Roadlyft_LOGO.png")


@app.route("/backend-server/icon/favicon.ico", methods=["GET"])
def return_favicon_for_admin_panel():
    return send_from_directory(directory=".", path="static/favicon.ico")


@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify(general_message="You have reached the ratelimit.",
                   security_message="If you are a cybersecurity expert and you call yourself cybersecurity expert, "
                                    "then buddy... you really need to think on this again!",
                   developer_message="err_cd_429 RL_Ext"), 429


@app.errorhandler(404)
def page_notfound_handler(e):
    return render_template("ERR_PAGE.html", ERROR_CODE=404,
                           ERROR_QUOTE="Page your are looking for has been moved or do not exist.")
    # return jsonify(general_message="Unauthorized access.",
    #                security_message="If you are a cybersecurity expert and you call yourself cybersecurity expert, "
    #                                 "then buddy... you really need to think on this again!",
    #                developer_message="err_cd_404 PG_NULL"), 404


@app.errorhandler(500)
def internal_server_error_handler(e):
    # print(e, str(e))
    # error_disc = str(e)
    # e_code, e_msg = error_disc.split(" ")[0], error_disc
    return render_template("ERR_PAGE.html", ERROR_CODE=500,
                           ERROR_QUOTE="There is some internal error. Hold tight our team is on the problem.")
    # return render_template("ERR_PAGE.html", ERROR_CODE=e_code,
    #                        ERROR_QUOTE=e_msg)


@app.errorhandler(405)
def internal_server_error_handler(e):
    print(e)
    return render_template("ERR_PAGE.html", ERROR_CODE=405,
                           ERROR_QUOTE="You do not hold permission to get into this section.")


if __name__ == "__main__":
    app.run(debug=True, port=5555)
