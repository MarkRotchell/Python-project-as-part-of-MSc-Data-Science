from math import sqrt, log10
from random import randint, shuffle
from tkinter import filedialog, messagebox
from tkinter import *
from itertools import islice, chain


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
    print(cities_as_string(road_map))


def cities_as_string(road_map):
    result = '     State                City                  Latitude  Longitude\n'
    for i, (state, city, lat, long) in enumerate(road_map):
        result += f'{i + 1:<4} {state:<20.20} {city:<20.20}  {lat:>8.2f}   {long:>8.2f}\n'
    return result


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

    print(map_as_string(road_map))


def map_as_string(road_map):
    result = 'Estimated optimal cycle:\n\n'
    for city1, city2 in zip(road_map, road_map[1:] + [road_map[0]]):
        dist = distance(city1, city2)
        result += f'{city1[1]:>20.20} --> {city2[1]:<20.20}  {dist:>8.2f}\n'
    result += '                                           -------------\n'
    total = compute_total_distance(road_map)
    result += f'                              Total Distance   {total:8.2f}\n'
    return result


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


class Itinerary:
    def __init__(self, road_map):
        self._road_map = road_map
        self._reset_extrema()

    def _reset_extrema(self):
        self._lat_max = max(self.latitudes())
        self._lat_min = min(self.latitudes())
        self._long_max = max(self.longitudes())
        self._long_min = min(self.longitudes())

    def road_map(self):
        return self._road_map

    def length(self):
        return len(self._road_map)

    def states(self):
        return (city[0] for city in self._road_map)

    def cities(self):
        return (city[1] for city in self._road_map)

    def latitudes(self):
        return (city[2] for city in self._road_map)

    def longitudes(self):
        return (city[3] for city in self._road_map)

    def latitude_max(self):
        return self._lat_max

    def latitude_min(self):
        return self._lat_min

    def longitude_max(self):
        return self._long_max

    def longitude_min(self):
        return self._long_min

    def reroute(self):
        shuffle(self._road_map)
        self._road_map = find_best_cycle(self._road_map)
        self._reset_extrema()


class ItineraryDrawer:
    def __init__(self, itinerary, canvas, margin_left_right, margin_top_bottom):
        self._itinerary = itinerary
        self._canvas = canvas
        self._canvas_width = canvas.winfo_width()
        self._canvas_height = canvas.winfo_height()
        self._canvas_margin_left_right = margin_left_right
        self._canvas_margin_top_bottom = margin_top_bottom
        self._drawable_width = self._canvas_width - 2 * margin_left_right
        self._drawable_height = self._canvas_height - 2 * margin_top_bottom

    @staticmethod
    def _longitude_to_x(longitude, long_min, long_max, drawing_area_width, margin_left_right):
        return drawing_area_width * (longitude - long_min) / (long_max - long_min) + margin_left_right

    @staticmethod
    def _latitude_to_y(latitude, lat_min, lat_max, drawing_area_height, margin_top_bottom):
        return drawing_area_height * (lat_max - latitude) / (lat_max - lat_min) + margin_top_bottom

    @staticmethod
    def gridline_spacing(min_coord, max_coord):
        if min_coord == max_coord:
            return 1.0
        else:
            min_lines = 5
            range_coord = max_coord - min_coord

            scale = 10 ** (log10(range_coord / min_lines) // 1)
            multiple = 10 ** (log10(range_coord / min_lines) % 1)

            if multiple < 2:
                multiple = 1
            elif multiple < 5:
                multiple = 2
            else:
                multiple = 5
            return multiple * scale

    @staticmethod
    def gridline_coords(min_coord, max_coord, drawing_area_extent, margin):
        spacing = ItineraryDrawer.gridline_spacing(min_coord, max_coord)
        displayed_range = (max_coord - min_coord) * margin / drawing_area_extent

        displayed_max = max_coord + displayed_range
        displayed_min = min_coord - displayed_range

        displayed_max -= (displayed_max % spacing)
        displayed_min += spacing - (displayed_min % spacing)
        steps = round((displayed_max - displayed_min) / spacing) + 1

        return (displayed_min + i * spacing for i in range(steps))

    def itinerary(self):
        return self._itinerary

    def points(self):
        return ((self._longitude_to_x(longitude=longitude,
                                      long_min=self._itinerary.longitude_min(),
                                      long_max=self._itinerary.longitude_max(),
                                      drawing_area_width=self._drawable_width,
                                      margin_left_right=self._canvas_margin_left_right),
                 self._latitude_to_y(latitude=latitude,
                                     lat_min=self._itinerary.latitude_min(),
                                     lat_max=self._itinerary.latitude_max(),
                                     drawing_area_height=self._drawable_height,
                                     margin_top_bottom=self._canvas_margin_top_bottom))
                for longitude, latitude in zip(self._itinerary.longitudes(), self._itinerary.latitudes()))

    def point_pairs(self):
        p0 = self.points()
        p1 = chain(islice(self.points(), 1, None), self.points())
        return (((x_0, y_0), (x_1, y_1)) for (x_0, y_0), (x_1, y_1) in zip(p0, p1))

    def latitude_gridlines(self):
        return self.gridline_coords(min_coord=self._itinerary.latitude_min(),
                                    max_coord=self._itinerary.latitude_max(),
                                    drawing_area_extent=self._drawable_height,
                                    margin=self._canvas_margin_top_bottom)

    def longitude_gridlines(self):
        return self.gridline_coords(min_coord=self._itinerary.longitude_min(),
                                    max_coord=self._itinerary.longitude_max(),
                                    drawing_area_extent=self._drawable_width,
                                    margin=self._canvas_margin_left_right)

    def x_gridlines(self):
        return ((self._longitude_to_x(longitude=longitude,
                                      long_min=self._itinerary.longitude_min(),
                                      long_max=self._itinerary.longitude_max(),
                                      drawing_area_width=self._drawable_width,
                                      margin_left_right=self._canvas_margin_left_right),
                 longitude)
                for longitude in self.longitude_gridlines())

    def y_gridlines(self):
        return ((self._latitude_to_y(latitude=latitude,
                                     lat_min=self._itinerary.latitude_min(),
                                     lat_max=self._itinerary.latitude_max(),
                                     drawing_area_height=self._drawable_height,
                                     margin_top_bottom=self._canvas_margin_top_bottom),
                 latitude)
                for latitude in self.latitude_gridlines())

    def draw_connectors(self):
        for (x_0, y_0), (x_1, y_1) in self.point_pairs():
            self._canvas.create_line(x_0, y_0, x_1, y_1, fill="red")

    def draw_points(self):
        oval_width = min(self._canvas_width, self._canvas_height) / 200
        for i, (x, y) in enumerate(self.points()):
            self._canvas.create_oval(x - oval_width, y - oval_width, x + oval_width, y + oval_width,
                                     fill='white', outline='black', width=1)
            self._canvas.create_text(x, y - 5, text=str(i + 1), anchor=S, font=('purisa', 8))

    def draw_gridlines(self):
        for x, long in self.x_gridlines():
            self._canvas.create_line(x, 0, x, self._canvas_height, fill="lightblue1")
            self._canvas.create_text(x, 5, text=str(long), anchor=NW, font=('purisa', 8))

        for y, lat in self.y_gridlines():
            self._canvas.create_line(0, y, self._canvas_width, y, fill="lightblue1")
            self._canvas.create_text(5, y - 5, text=str(lat), anchor=SW, font=('purisa', 8))

    def draw_map(self):
        self._canvas.update()
        self._canvas.delete("all")
        self.draw_gridlines()
        self.draw_connectors()
        self.draw_points()


class ApplicationWindow:
    def __init__(self, road_map, canvas_height=800, canvas_width=800,
                 margin_top_bottom=50, margin_left_right=50):
        self._road_map = road_map
        self._canvas_height = canvas_height
        self._canvas_width = canvas_width
        self._margin_top_bottom = margin_top_bottom
        self._margin_left_right = margin_left_right
        self._itinerary = Itinerary(road_map)
        self._set_up_window()
        self._set_up_control_frame()
        self._set_up_output_frame()
        self._set_up_text_frame()
        self._drawer = ItineraryDrawer(self._itinerary, self._canvas, self._margin_left_right, self._margin_top_bottom)

    def _set_up_window(self):
        self._window = Tk()
        self._window.title("Travelling Salesman GUI")

    def _set_up_control_frame(self):
        control_frame = Frame(self._window)
        control_frame.pack(side=LEFT, padx=10, pady=10, fill=BOTH, expand=YES)
        Button(control_frame, text='Re Route', command=self.re_route).pack(side=TOP, anchor='n', fill=X, expand=NO)

    def _set_up_output_frame(self):
        output_frame = Frame(self._window)
        output_frame.pack(side=LEFT, padx=10, pady=10, anchor='nw', fill=X, expand=YES)
        self._canvas = Canvas(output_frame, width=self._canvas_width, height=self._canvas_height, bg='white')
        self._canvas.pack()
        self._canvas.update()

    def _set_up_text_frame(self):
        text_frame = Frame(self._window)
        text_frame.pack(side=LEFT, padx=10, pady=10, anchor='nw', fill=X, expand=YES)
        scrollbar = Scrollbar(text_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        self._cities_box = Listbox(text_frame, yscrollcommand=scrollbar.set, height=20, width=70, font='TkFixedFont')
        self._cities_box.pack(side=LEFT, padx=10, pady=10, anchor='nw', fill=X, expand=YES)


    def draw(self):
        self._drawer.draw_map()

    def show_cities(self):
        self._cities_box.delete(0, END)
        for i, line in enumerate(cities_as_string(self._itinerary.road_map()).splitlines()):
            self._cities_box.insert(i, line)

    def re_route(self):
        self._drawer.itinerary().reroute()
        self.draw()
        self.show_cities()

    def main_loop(self):
        self._window.mainloop()


def visualise(road_map):
    app = ApplicationWindow(road_map)
    app.draw()
    app.show_cities()
    app.main_loop()


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

                print_map(road_map)

                visualise(road_map)

                load_another_map = user_wants_to_load_a_different_file(
                    'Would you like to open another map?')


if __name__ == "__main__":  # keep this in
    main()
