# Write your solution here
import math
def get_station_data(filename: str) -> dict:
    stations = {}
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(';')
            if parts[0] == "Longitude":
                continue
            else:
                stations[parts[3]] = (float(parts[0]),float(parts[1]))
    return stations

def distance(stations: dict,station1: str,station2: str):
    long1 = 0
    long2 = 0
    lat1 = 0
    lat2 = 0
    
    for stations, coordinates in stations.items():
        long, lat = coordinates
        
        if station1 == stations:
            long1 = long
            lat1 = lat
        elif station2 == stations:
            long2 = long
            lat2 = lat

    x_km = (long1 - long2) * 55.26
    y_km = (lat1 - lat2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    max_distance = 0
    station1 = ""
    station2 = ""

    for i in stations.items():
        for j in stations.items():
            if i == j:
                continue
            if max_distance < distance(stations,i[0],j[0]):
                max_distance = distance(stations,i[0],j[0])
                station1 = i[0]
                station2 = j[0]

    return station1,station2, max_distance

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)