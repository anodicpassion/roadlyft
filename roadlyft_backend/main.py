from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import time, random
import datetime, pytz

app = Flask(__name__)
CORS(app, supports_credentials=True)
limiter = Limiter(get_remote_address, app=app)

usr_d: dict = {}
oth_usr_data: dict = {}
deck_handler: dict = {}
char_a_z = "abcdefghijklmnopqrstuvwxyz"
route = []

with open("enc/pyc_cache", "r") as pycache:
    exec(pycache.read())

with open("enc/locations", "r") as loc:
    locations = loc.read().split("\n")


def deck_create_instance(usr_mobile):
    """Creates the deck instance for the advanced access to the user. This provides the additional security features."""
    temp_de = ""
    ist_timezone = pytz.timezone('Asia/Kolkata')
    current_date_ist = datetime.datetime.now(ist_timezone)
    cur_dat_time = current_date_ist.strftime("%H:%M:%S %D")
    # cur_dat_time = datetime.datetime.now().strftime("%H:%M:%S %D")

    # if usr_mobile
    # if deck_handler.get(usr_mobile):

    while True:
        for i in range(8):
            temp_de = temp_de + char_a_z[random.randint(0, len(char_a_z) - 1)]
        if deck_handler.get(usr_mobile):
            if deck_handler[usr_mobile][0] != temp_de:
                deck_handler[usr_mobile] = [temp_de, cur_dat_time, True, cur_dat_time, cur_dat_time]
                break
        else:
            deck_handler[usr_mobile] = [temp_de]
            break
    deck_handler[usr_mobile] = [temp_de, cur_dat_time, True, cur_dat_time, cur_dat_time]
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
            return [True, i]
    return [False]


@app.route("/")
@limiter.limit("60 per minute")
def index():
    return "<center>ROAD-LIST Coming Soon...!</center>"


@app.route("/get", methods=["POST"])
def get():
    print(request.cookies.keys())
    # time.sleep(5)
    return jsonify({"k": "v"})


@app.route("/create_account", methods=["POST"])
def create_account():
    request_data = request.json
    usr_name = request_data['user_name'].strip()
    usr_mobile = request_data['mobile'].strip()
    usr_password = request_data['password']
    print(usr_name, usr_mobile, usr_password)
    print
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


@app.route("/login", methods=["POST"])
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
                return response
            else:
                response = jsonify({"LOGIN_STAT": "FAILURE"})
                return response
        else:
            response = jsonify({"LOGIN_STAT": "FAILURE"})
            return response
    else:
        response = jsonify({"LOGIN_STAT": "FAILURE"})
        return response


@app.route("/get_homepage_da", methods=["POST"])
def get_dates():
    ist = pytz.timezone('Asia/Kolkata')
    today = datetime.datetime.now(ist).date().today()
    tomorrow = today + datetime.timedelta(days=1)
    day_after_tomorrow = tomorrow + datetime.timedelta(days=1)
    third_date = day_after_tomorrow + datetime.timedelta(days=1)
    forth_date = third_date + datetime.timedelta(days=1)

    request_body = request.json
    print("Requesting the homepage data with given request body: ", request_body)
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    val = valid_usr_req(usr_id)
    if usr_id == local_str and val[0]:
        usr_name_d, driving_flag = oth_usr_data[val[1]][0: 2]
        return jsonify({"RESP_STAT": "SUCCESS", "TODAY": today.strftime("%d"), "TOMORROW": tomorrow.strftime("%d"),
                        "DATE_AFTER_TOMORROW": day_after_tomorrow.strftime("%d"),
                        "DAY_AFTER_TOMORROW": day_after_tomorrow.strftime("%A")[:3],
                        "THIRD_DATE": third_date.strftime("%d"), "THIRD_DAY": third_date.strftime("%A")[:3],
                        "FORTH_DATE": forth_date.strftime("%d"), "FORTH_DAY": forth_date.strftime("%A")[:3],
                        "USR_NAME": usr_name_d, "DRIVING_FLAG": driving_flag})

    else:
        print("Failed to respond with homepage data with given request body: ", request_body)
        return jsonify({"RESP_STAT": "FAILURE"})


@app.route("/get_loc_da", methods=["POST"])
def get_locations():
    global locations
    request_body = request.json
    print("Requesting the location data with given request body: ", request_body)
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    if usr_id == local_str and valid_usr_req(usr_id):
        return jsonify({"RESP_STAT": "SUCCESS", "LOC": locations})
    else:
        return jsonify({"RESP_STAT": "FAILURE"})


@app.route("/p_go")
def booking_passanger_s1():
    request_body = request.json
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    loyalty = request_body["loyalty"]
    print("Requesting to ride booking with given request body: ", request_body)
    if loyalty != "spawned%20uWSG":
        print()


@app.route("/d_post", methods=["POST"])
def ride_publish():
    request_body = request.json
    usr_id = request_body["auth_toc_usr"]
    local_str = request_body["local_str"]
    loyalty = request_body["loyalty"]
    pickup = request_body["pickup_point"]
    dropoff = request_body["dropoff_point"]
    s_time = request_body["start_time"]
    s_date = request_body["start_date"]
    
    print("Requesting ride publish with given request body: ", request_body)
    val = valid_usr_req(usr_id)
    if loyalty == "spawned%20uWSGI" and val[0] and usr_id == local_str:

        return jsonify({"RESP_STAT": "SUCCESS"})
    else:
        return jsonify({"RESP_STAT": "FAILURE"})


@app.route("/commit", methods=["POST"])
def commit():
    global usr_d, oth_usr_data

    with open("enc/pyc_cache", "w") as commit_file:
        commit_file.write(f"usr_d ={usr_d}\noth_usr_data = {oth_usr_data}")


@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify(general_message="You have reached the ratelimit.",
                   security_message="If you are a cybersecurity expert and you call yourself cybersecurity expert, "
                                    "then buddy... you really need to think on this again!",
                   developer_message="err_cd_429 RL_Ext"), 429


if __name__ == "__main__":
    app.run(debug=True, port=5555)
