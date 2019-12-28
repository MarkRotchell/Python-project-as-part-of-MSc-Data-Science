from math import sqrt, log10
from random import randint, shuffle
from tkinter import filedialog, messagebox
from tkinter import *
from functools import partial


def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return
    them as a list of four-tuples: [(state, city, latitude, longitude), ...]
    """

    if not isinstance(file_name, str):
        raise TypeError()

    try:
        infile = open(file_name, "r")

    except FileNotFoundError:
        raise

    line = infile.readline()

    if not line:
        raise EOFError()

    lines = []

    while line:
        line = line.rstrip().split('\t')
        lines.append((line[0], line[1], float(line[2]), float(line[3])))
        line = infile.readline()

    infile.close()

    return lines


def print_cities(road_map):
    """
    Prints a list of cities, along with their locations.
    """

    print('State                City                  Latitude  Longitude')
    for state, city, lat, long in road_map:
        print(f'{state:<20.20} {city:<20.20}  {lat:>8.2f}   {long:>8.2f}')


def distance(city_1, city_2):
    """
    Calculates the euclidian distance between two cities via pythagoras
    """
    return sqrt((city_2[2] - city_1[2]) ** 2 + (city_2[3] - city_1[3]) ** 2)


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and their connections,
    along with the cost for each connection and the total cost.
    """

    total = 0
    for city1, city2 in zip(road_map, road_map[1:] + [road_map[0]]):
        dist = distance(city1, city2)
        print(f'{city1[1]:>20.20} --> {city2[1]:<20.20}  {dist:>8.2f}')
        total += dist
    print('                                           -------------')
    print(f'                              Total Distance   {total:8.2f}')


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all the connections in the `road_map`.
    """
    return sum(distance(city1, city2) for city1, city2 in zip(road_map, road_map[1:] + [road_map[0]]))


def swap_cities(road_map, index1, index2):
    """
    Swap cities at location `index` and `index2`, compute the new total distance, and return the tuple
        (new_road_map, new_total_distance)
    """
    road_map[index1], road_map[index2] = road_map[index2], road_map[index1]
    return road_map, compute_total_distance(road_map)


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves to the position i+1.
    The city at the last position moves to the position 0. Return the new road map.
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


def drawing_area(canvas_size, margin):
    """ Returns the drawable size of one dimension of the canvas given size and the margin"""
    return max(max(canvas_size, 0) - 2 * max(margin, 0), 0)


def longitude_to_x(longitude, long_min, long_max, drawing_area_width, margin_left_right):
    return drawing_area_width * (longitude - long_min) / (long_max - long_min) + margin_left_right


def latitude_to_y(latitude, lat_min, lat_max, drawing_area_height, margin_top_bottom):
    return drawing_area_height * (lat_max - latitude) / (lat_max - lat_min) + margin_top_bottom


def gridline_spacing(min_coord, max_coord):
    range_coord = max_coord - min_coord

    scale = 10 ** (log10(range_coord / 5) // 1)
    multiple = 10 ** (log10(range_coord / 5) % 1)

    if multiple < 2:
        multiple = 1
    elif multiple < 5:
        multiple = 2
    else:
        multiple = 5
    return multiple * scale


def gridline_locations(min_coord, max_coord, drawing_area, margin):
    spacing = gridline_spacing(min_coord, max_coord)
    displayed_range = (max_coord - min_coord) * margin / drawing_area

    displayed_max = max_coord + displayed_range
    displayed_min = min_coord - displayed_range

    displayed_max -= (displayed_max % spacing)
    displayed_min += spacing - (displayed_min % spacing)
    steps = round((displayed_max - displayed_min) / spacing) + 1

    return [displayed_min + i * spacing for i in range(steps)]


def canvas_coords(road_map, canvas_height, canvas_width, margin_top_bottom, margin_left_right):
    """
    Calculates the x and y coordinates of cities on the canvas and returns a list of tuples of the form (x,y)
    """

    drawing_area_width = drawing_area(canvas_width, margin_left_right)
    drawing_area_height = drawing_area(canvas_height, margin_top_bottom)

    lats = [city[2] for city in road_map]
    longs = [city[3] for city in road_map]

    lat_max, lat_min = max(lats), min(lats)
    long_max, long_min = max(longs), min(longs)

    x_coords = (longitude_to_x(long, long_min, long_max, drawing_area_width, margin_left_right) for long in longs)
    y_coords = (latitude_to_y(lat, lat_min, lat_max, drawing_area_height, margin_top_bottom) for lat in lats)

    return [(x, y) for x, y in zip(x_coords, y_coords)]


def draw_map(road_map, canvas, margin_left_right, margin_top_bottom):
    """
    Fills the canvas with the route specified by the road map
    not unit-tested as it is an output function.
    """
    canvas.update()
    coords = canvas_coords(road_map, canvas.winfo_height(), canvas.winfo_width(), margin_left_right, margin_top_bottom)
    canvas.delete('all')

    oval_width = min(canvas.winfo_height(), canvas.winfo_width()) / 200
    # temp
    drawing_area_width = drawing_area(canvas.winfo_width(), margin_left_right)
    drawing_area_height = drawing_area(canvas.winfo_height(), margin_top_bottom)

    lats = [city[2] for city in road_map]
    longs = [city[3] for city in road_map]

    lat_max, lat_min = max(lats), min(lats)
    long_max, long_min = max(longs), min(longs)
    #temp

    for gridline in gridline_locations(lat_min, lat_max, drawing_area_height, margin_top_bottom):
        y = latitude_to_y(gridline, lat_min, lat_max, drawing_area_height, margin_top_bottom)
        canvas.create_line(0, y, canvas.winfo_width(), y, fill="lightblue1")
        canvas.create_text(0+5, y - 5, text=str(gridline), anchor=SW, font=('purisa', 8))

    for gridline in gridline_locations(long_min, long_max, drawing_area_width, margin_left_right):
        x = longitude_to_x(gridline, long_min, long_max, drawing_area_width, margin_left_right)
        canvas.create_line(x, 0 , x, canvas.winfo_height(), fill="lightblue1")
        canvas.create_text(x, 5, text=str(gridline), anchor=NW, font=('purisa', 8))

    for city0, city1 in zip(coords, coords[1:] + [coords[0]]):
        canvas.create_line(city0[0], city0[1], city1[0], city1[1], fill="red")

    for x, y in coords:
        canvas.create_oval(x - oval_width, y - oval_width, x + oval_width, y + oval_width,
                           fill='white', outline='black', width=1)

    for i, (x, y) in enumerate(coords):
        canvas.create_text(x, y - 5, text=str(i + 1), anchor=S, font=('purisa', 8))


def re_route(road_map, canvas, margin_left_right, margin_top_bottom):
    """
    shuffles the road_map, recalculates the route, prints and re-draws the route.
    """
    shuffle(road_map)

    road_map = find_best_cycle(road_map)

    print('\nEstimated optimal cycle:\n')

    print_map(road_map)

    draw_map(road_map, canvas, margin_left_right, margin_top_bottom)


def visualise(road_map):
    """
    shows the road_map visually in a Tkinter dialogue box
    also provides a re-route button so user can get a different route if they want
    """

    canvas_height, canvas_width = 1000, 1000
    margin_top_bottom, margin_left_right = 50, 50

    window = Tk()
    window.title("GUI")

    control_frame = Frame(window)
    control_frame.pack(side=LEFT, padx=10, pady=10, fill=BOTH, expand=YES)

    output_frame = Frame(window)
    output_frame.pack(side=LEFT, padx=10, pady=10, anchor='nw', fill=X, expand=YES)

    canvas = Canvas(output_frame, width=canvas_width, height=canvas_height, bg='white')
    canvas.pack()

    draw_map(road_map, canvas, margin_left_right, margin_top_bottom)

    re_route_command = partial(re_route, road_map, canvas, margin_left_right, margin_top_bottom)
    Button(control_frame, text='Re Route', command=re_route_command).pack(side=TOP, anchor='n', fill=X, expand=NO)

    window.mainloop()


def user_wants_to_load_a_different_file(question):
    """
    Asks user if they want to load another file, and returns answer as boolean.
    """
    root = Tk()
    root.withdraw()
    yes_no = messagebox.askyesno(message=question, icon='question', title='Unable to load file')
    root.destroy()
    return yes_no


def get_file_name():
    """
    Opens the file-open dialogue box to ask the user for a file
    """
    root = Tk()
    root.withdraw()
    path = filedialog.askopenfilename(initialdir="/", title="Select Route Map File",
                                      filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    root.destroy()

    return path


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"cycle and prints it out.
    """
    load_another_map = True

    while load_another_map:
        file_path = get_file_name()

        if not file_path:
            load_another_map = user_wants_to_load_a_different_file(
                'No file specified, would you like to try again?')

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
