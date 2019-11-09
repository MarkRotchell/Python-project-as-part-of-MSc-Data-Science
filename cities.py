from math import sqrt
import random


def read_cities(file_name):
    if type(file_name) is not str:
        raise TypeError('read_cities requires a path string, ' + str(type(file_name)) + ' passed instead')
    infile = open(file_name, "r")
    lines = infile.readlines()
    if len(lines) == 0:
        raise EOFError('file was empty')
    for i, line in enumerate(lines):
        line = line.rstrip().split('\t')
        lines[i] = (line[0], line[1], float(line[2]), float(line[3]))
    return lines

    infile.close()


def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    # max_state_length = max(len(city[0]) for city in road_map)
    # max_city_length = max(len(city[0]) for city in road_map)
    print('State                City                  Latitude  Longitude')
    for city in road_map:
        state, city, lat, long = (city[i] for i in range(4))
        print(f'{state:<20.20} {city:<20.20}  {lat:>8.2f}   {long:>8.2f}')


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and
    their connections, along with the cost for each connection
    and the total cost.
    """
    pass


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    n = len(road_map)
    dist = 0

    for i in range(n):
        city_1, city_2 = road_map[i], road_map[(i+1) % n]
        dist += sqrt((city_2[2] - city_1[2]) ** 2 + (city_2[3] - city_1[3]) ** 2)

    return dist


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    road_map[index1], road_map[index2] = road_map[index2], road_map[index1]
    return road_map, compute_total_distance(road_map)


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    return None


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """

    return None


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """

    road_map = read_cities('city-data.txt')
    print_cities(road_map)


if __name__ == "__main__":  # keep this in
    main()
