from math import sqrt
from random import randint, shuffle
from tkinter import filedialog, messagebox
from tkinter import *
from functools import partial


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


def drawing_area(canvas_dimension, margin):
    """ Returns the drawable area of canvas given some dimension and the margin"""
    return max(max(canvas_dimension, 0) - 2 * max(margin, 0), 0)


def canvas_coords(road_map, canvas_height, canvas_width, margin_top_bottom, margin_left_right):

    drawing_area_width = drawing_area(canvas_width, margin_left_right)
    drawing_area_height = drawing_area(canvas_height, margin_top_bottom)

    lats, longs = [[node[element] for node in road_map] for element in [2, 3]]

    lat_max, long_min = max(lats), min(longs)

    return [(drawing_area_width * (longs[i] - long_min) / (max(longs) - long_min) + margin_left_right,
             drawing_area_height * (lat_max - lats[i]) / (lat_max - min(lats)) + margin_top_bottom)
            for i in range(len(road_map))]


def draw_map(road_map, canvas, margin_left_right, margin_top_bottom):
    canvas.update()
    coords = canvas_coords(road_map, canvas.winfo_height(), canvas.winfo_width(),
                           margin_left_right, margin_top_bottom)

    n = len(coords)

    canvas.delete('all')

    for i in range(n):
        canvas.create_line(coords[i][0], coords[i][1], coords[(i + 1) % n][0], coords[(i + 1) % n][1], fill="red")

    oval_width = min(canvas.winfo_height(), canvas.winfo_width()) / 200

    for x, y in coords:
        canvas.create_oval(x - oval_width, y - oval_width, x + oval_width, y + oval_width, fill='white',
                           outline='black', width=1)


def re_route(road_map, canvas, margin_left_right, margin_top_bottom):
    shuffle(road_map)
    road_map = find_best_cycle(road_map)
    draw_map(road_map, canvas, margin_left_right, margin_top_bottom)


def user_wants_to_load_a_different_file(question):
    root = Tk()
    root.withdraw()
    yes_no = messagebox.askyesno(message=question,
                                 icon='question', title='Unable to load file')
    root.destroy()
    return yes_no


def get_file_name():
    root = Tk()
    root.withdraw()
    path = filedialog.askopenfilename(initialdir="/", title="Select Route Map File",
                                      filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    root.destroy()

    return path


def visualise(road_map):
    canvas_height, canvas_width, margin_top_bottom, margin_left_right = 500, 500, 50, 50

    window = Tk()
    window.title("GUI")

    fm = Frame(window)
    fm.pack(side=LEFT, padx=10, pady=10, fill=BOTH, expand=YES)

    fm2 = Frame(window)
    fm2.pack(side=LEFT, padx=10, pady=10, anchor='nw', fill=X, expand=YES)

    canvas = Canvas(fm2, width=canvas_width, height=canvas_height)
    canvas.pack()

    draw_map(road_map, canvas, margin_left_right, margin_top_bottom)

    re_route_command = partial(re_route, road_map, canvas, margin_left_right, margin_top_bottom)
    Button(fm, text='Re Route', command=re_route_command).pack(side=TOP, anchor='n', fill=X, expand=NO)

    window.mainloop()


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    load_another_map = True

    while load_another_map:
        file_path = get_file_name()

        if not file_path:
            load_another_map = user_wants_to_load_a_different_file('No file specified, would you like to try again?')

        else:

            try:
                road_map = read_cities(file_path)

            except:
                load_another_map = user_wants_to_load_a_different_file(
                    'Unable to Load file given, would you like to select a different file?')

            else:
                print('The following cities were loaded')

                print_cities(road_map)

                road_map = find_best_cycle(road_map)

                print('\nEstimated optimal cycle:\n')

                print_map(road_map)

                visualise(road_map)

                load_another_map = user_wants_to_load_a_different_file(
                    'Would you like to open another map?')


if __name__ == "__main__":  # keep this in
    main()
