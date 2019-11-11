from math import sqrt
from random import randint
from tkinter import *


def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return
    them as a list of four-tuples:

      [(state, city, latitude, longitude), ...]

    Use this as your initial `road_map`, that is, the cycle

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    if type(file_name) is not str:
        raise TypeError()

    with open(file_name, "r") as infile:
        lines = infile.readlines()

    n = len(lines)

    if n == 0:
        raise EOFError()

    for i in range(n):
        line = lines[i].rstrip().split('\t')
        lines[i] = (line[0], line[1], float(line[2]), float(line[3]))

    return lines


def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """

    print('State                City                  Latitude  Longitude')
    for state, city, lat, long in road_map:
        print(f'{state:<20.20} {city:<20.20}  {lat:>8.2f}   {long:>8.2f}')


def distance(city_1, city_2):
    """
    Calculates the distance between two cities via pythagoras
    """
    return sqrt((city_2[2] - city_1[2]) ** 2 + (city_2[3] - city_1[3]) ** 2)


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and
    their connections, along with the cost for each connection
    and the total cost.
    """
    n = len(road_map)
    for i in range(n):
        city1, city2, = road_map[i], road_map[(i + 1) % n]
        dist = distance(city1, city2)
        print(f'{city1[1]:>20.20} --> {city2[1]:<20.20}  {dist:>8.2f}')

    dist = compute_total_distance(road_map)
    print('                                           -------------')
    print(f'                              Total Distance   {dist:8.2f}')


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    n = len(road_map)
    return sum([distance(road_map[i], road_map[(i + 1) % n]) for i in range(n)])


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
    road_map.insert(0, road_map.pop())
    return road_map


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    map_best = road_map[:]

    dist_best = compute_total_distance(map_best)

    n = len(map_best) - 1

    for i in range(10000):

        map_cand, dist_cand = swap_cities(map_best[:], randint(0, n), randint(0, n))

        if dist_cand < dist_best:
            map_best, dist_best = map_cand, dist_cand

        shift_cities(map_best)

    return map_best


def canvas_coords(road_map, canvas_height, canvas_width, margin_top_bottom, margin_left_right):
    drawing_area_left_right = canvas_width - 2 * margin_left_right
    drawing_area_top_bottom = canvas_height - 2 * margin_top_bottom
    lats, longs = [[city[element] for city in road_map] for element in [2, 3]]

    lat_max, lat_min, long_max, long_min = max(lats), min(lats), max(longs), min(longs)

    lat_range, long_range = lat_max - lat_min, long_max - long_min
    n = len(road_map)

    x = [drawing_area_left_right * (longs[i] - long_min) / long_range + margin_left_right for i in range(n)]
    y = [drawing_area_top_bottom * (lat_max - lats[i]) / lat_range + margin_top_bottom for i in range(n)]
    return x, y

def draw_map(road_map, canvas):
    coords_x, coords_y = canvas_coords(road_map, 500, 500, 50, 50)

    n = len(coords_x)

    canvas.delete('all')

    for i in range(n):
        canvas.create_line(coords_x[i], coords_y[i], coords_x[(i + 1) % n], coords_y[(i + 1) % n], fill="red")

    for x, y in zip(coords_x, coords_y):
        canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill='black', width=3)

def visualise(road_map):

    canvas_height = 500
    canvas_width = 500
    margin_top_bottom = 50
    margin_left_right = 50

    window = Tk()
    window.title("GUI")
    fm = Frame(window)

    fm.pack(side=LEFT, padx=10, pady=10, fill=BOTH, expand=YES)

    fm2 = Frame(window)
    canvas = Canvas(fm2, width=canvas_width, height=canvas_height)
    canvas.pack()
    fm2.pack(side=LEFT, padx=10, pady=10, anchor='nw', fill=X, expand=YES)

    draw_map(road_map, canvas)

    Button(fm, text='Top').pack(side=TOP, anchor='n', fill=X, expand=NO)
    Button(fm, text='Center').pack(side=TOP, anchor='n', fill=X, expand=NO)
    Button(fm, text='Bottom').pack(side=TOP, anchor='n', fill=X, expand=NO)
    window.mainloop()


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    while True:
        #file_path = input('Enter Path or Q to quit: ')
        file_path = 'city-data.txt'
        if file_path == 'Q':
            break

        try:
            road_map = read_cities(file_path)
        except FileNotFoundError:
            print('File not found at path: please enter a valid path')
        except TypeError:
            print('Input was not a string, please enter a valid path')
        except EOFError:
            print('File is empty, please choose another file')
        except:
            print('Unknown Error Occurred Reading file, please try another file')
        else:
            print('The following cities were loaded')

            print_cities(road_map)

            road_map = find_best_cycle(road_map)

            print()

            print('Estimated optimal cycle:')

            print()

            print_map(road_map)

            x, y = canvas_coords(road_map, 500, 500, 50, 50)

            #for x_i, y_i in zip(x, y):
             #   print(x_i, y_i)
            visualise(road_map)
        break

if __name__ == "__main__":  # keep this in
    main()
