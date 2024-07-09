import googlemaps
from geopy.distance import geodesic

# Initialize Google Maps client
gmaps = googlemaps.Client(key='AIzaSyCFR4iDnFaRzaDGHzcARIy71DkgZGlDrb0')


# Function to get route points from Google Maps Directions API
def get_route_points(origin, destination, route_index=0):
    directions_result = gmaps.directions(origin, destination, mode="driving", alternatives=True)
    if directions_result and len(directions_result) > route_index:
        route = directions_result[route_index]
        route_points = []
        for leg in route['legs']:
            for step in leg['steps']:
                start_location = step['start_location']
                end_location = step['end_location']
                route_points.append((start_location['lat'], start_location['lng']))
                route_points.append((end_location['lat'], end_location['lng']))
        return route_points, route['legs'][0]['duration']['text'], route['legs'][0]['distance']['text']
    return []


# Function to check if a point lies near the route
def is_point_near_route(point, route_points, max_distance=30):
    for route_point in route_points:
        # print(geodesic(point, route_point).kilometers)
        if geodesic(point, route_point).kilometers <= max_distance:
            print(geodesic(point, route_point).kilometers)
            return True
    return False


karad = 17.277693, 74.1843535
delhi = 28.7040592, 77.10249019999999
satara = 17.6804639, 74.018261
pune = 18.5204303, 73.8567437
saswad = 18.3463128, 74.0301826
mumbai = 19.0759837, 72.8776559

gwalior = 26.2124007, 78.1772053
ratlam = 23.3315103, 75.0366677
ujjain = 23.1764665, 75.7885163


route_index = 1

# Example usage
driver_origin = karad
driver_destination = delhi

passenger_start = ujjain
passenger_end = delhi

# Get driver route points
r_t = get_route_points(driver_origin, driver_destination, route_index)
route_points, time, distance = r_t[:]
print(time, distance)
# Check if passenger start and end points are near the route
is_start_near_route = is_point_near_route(passenger_start, route_points)
is_end_near_route = is_point_near_route(passenger_end, route_points)
# print(is_start_near_route, is_end_near_route)
if is_start_near_route and is_end_near_route:
    print("Passenger's route lies on the driver's route.")
else:
    print("Passenger's route does not lie on the driver's route.")
