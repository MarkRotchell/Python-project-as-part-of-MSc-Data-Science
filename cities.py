from math import sqrt, log10
from random import randint, shuffle
from tkinter import filedialog, messagebox
from tkinter import *
from itertools import chain, count, tee
from collections import namedtuple

City = namedtuple('City', ['state', 'name', 'latitude', 'longitude'])


def read_cities(file_name):
    """Read File and return road_map

    :param file_name: (str) a path to the file containing the road_map
    :return: list of four-tuples: [(state, city, latitude, longitude), ...]
    """
    if not isinstance(file_name, str):
        raise TypeError()
    try:
        infile = open(file=file_name, mode="r")
    except FileNotFoundError:
        raise
    line = infile.readline()
    if not line:
        raise EOFError()
    lines = []
    while line:
        city = City(*line.rstrip().split(sep='\t'))
        lines.append((str(city.state), str(city.name), float(city.latitude), float(city.longitude)))
        line = infile.readline()
    infile.close()
    return lines


def print_cities(road_map):
    """Prints a list of cities, along with their locations.

    :param road_map: list of four-tuples: [(state, city, latitude, longitude), ...]
    """
    print(cities_as_string(road_map=road_map))


def cities_as_string(road_map):
    """Returns a multi-line string containing a table of details about each city

    :param road_map: list of four-tuples: [(state, city, latitude, longitude), ...]
    :return: multi-line string
    """
    result = '     State                City                  Latitude  Longitude\n'
    for i, city in enumerate(road_map):
        city = City(*city)
        result += f'{i + 1:<4} {city.state:<20.20} {city.name:<20.20}  {city.latitude:>8.2f}   {city.longitude:>8.2f}\n'
    return result


def distance(city0, city1):
    """Calculates the Euclidean distance between two cities assuming a flat (i.e. cartesian) world

    :param city0: a tuple of the form (state, city, latitude, longitude)
    :param city1: a tuple of the form (state, city, latitude, longitude)
    :return : (float) the Euclidean distance between the two cities
    """
    city0, city1 = City(*city0), City(*city1)
    return sqrt((city1.latitude - city0.latitude) ** 2 + (city1.longitude - city0.longitude) ** 2)


def pairwise_circuit(iterable):
    """Yields pairs of adjacent elements from an iterable. The last element is paired with the first

    :param iterable: any iterable
    :return: iterator yielding pairs of form (x_i, x_i+1) for 0 <= i < n, and final pair (x_n, x_0)
    """
    a, b = tee(iterable)
    b = chain(b, [next(b)])
    return zip(a, b)


def print_map(road_map):
    """Prints, the route between cities, the distance of each leg and the total distance

    :param road_map:  list of four-tuples: [(state, city, latitude, longitude), ...]
    """
    print(map_as_string(road_map=road_map))


def map_as_string(road_map):
    """Multi-line string detailing the route between cities, the distance of each leg and the total distance

    :param road_map:  list of four-tuples: [(state, city, latitude, longitude), ...]
    :return: multi-line string
    """
    result = 'Estimated optimal cycle:\n\n'
    for city0, city1 in pairwise_circuit(iterable=road_map):
        dist = distance(city0, city1)
        city0, city1 = City(*city0), City(*city1)
        result += f'{city0.name:>20.20} --> {city1.name:<20.20}  {dist:>8.2f}\n'
    result += '                                           -------------\n'
    total = compute_total_distance(road_map=road_map)
    result += f'                              Total Distance   {total:8.2f}\n'
    return result


def compute_total_distance(road_map):
    """Computes the sum of the distances of all the connections in the `road_map`.
    :param road_map: list of four-tuples: [(state, city, latitude, longitude), ...]
    :return: float
    """
    return sum(distance(city0=city1, city1=city2) for city1, city2 in pairwise_circuit(road_map))


def swap_cities(road_map, index1, index2):
    """
    Swap cities at location `index` and `index2`, compute the new total distance, and return the tuple
        (new_road_map, new_total_distance)
    """
    road_map[index1], road_map[index2] = road_map[index2], road_map[index1]
    return road_map, compute_total_distance(road_map=road_map)


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves to the position i+1.
    The city at the last position moves to the position 0. Return the new road map.
    """
    road_map.insert(0, road_map.pop())
    return road_map


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`,  try `10000` swaps/shifts, and each time keep the best
    cycle found so far. After `10000` swaps/shifts, return the best cycle found so far. Use randomly generated indices
    """
    map_best = road_map[:]
    dist_best = compute_total_distance(road_map=map_best)
    n = len(map_best) - 1
    for i in range(10000):
        map_cand, dist_cand = swap_cities(road_map=map_best[:], index1=randint(0, n), index2=randint(0, n))
        if dist_cand < dist_best:
            map_best, dist_best = map_cand, dist_cand
        shift_cities(road_map=map_best)
    return map_best


class Itinerary:
    def __init__(self, road_map):
        self.road_map = road_map

    @property
    def road_map(self):
        return self._road_map

    @road_map.setter
    def road_map(self, road_map):
        self._road_map = road_map
        self._lat_max = max(latitude for *_, latitude, _ in self.road_map)
        self._lat_min = min(latitude for *_, latitude, _ in self.road_map)
        self._long_max = max(longitude for *_, longitude in self.road_map)
        self._long_min = min(longitude for *_, longitude in self.road_map)

    @property
    def latitude_max(self):
        return self._lat_max

    @property
    def latitude_min(self):
        return self._lat_min

    @property
    def longitude_max(self):
        return self._long_max

    @property
    def longitude_min(self):
        return self._long_min

    @property
    def is_single_point(self):
        unique_coordinates = set((latitude, longitude) for *_, latitude, longitude in self.road_map)
        return len(unique_coordinates) == 1

    def reroute(self):
        shuffle(self.road_map)
        self.road_map = find_best_cycle(self.road_map)

    def coordinates(self):
        return ((latitude, longitude) for *_, latitude, longitude in self.road_map)

    def legs(self):
        return pairwise_circuit(self.coordinates())


class ItineraryDrawer:
    def __init__(self, drawable_size_px=700, margin_px=50, min_grid_lines=5, grid_line_colour='lightblue1',
                 grid_line_thickness=1, leg_line_colour='red', leg_line_thickness=1, city_radius=2, city_fill='white',
                 city_line_colour='black', city_line_thickness=1, label_font=('purisa', 8),
                 degrees_to_show_for_single_point=1.0):
        self.drawable_size_px = drawable_size_px
        self.margin_px = margin_px
        self.min_grid_lines = min_grid_lines
        self.grid_line_colour = grid_line_colour
        self.grid_line_thickness = grid_line_thickness
        self.leg_line_colour = leg_line_colour
        self.leg_line_thickness = leg_line_thickness
        self.city_radius = city_radius
        self.city_fill = city_fill
        self.city_line_colour = city_line_colour
        self.city_line_thickness = city_line_thickness
        self.label_font = label_font
        self.degrees_to_show_for_single_point = degrees_to_show_for_single_point

    @property
    def drawable_size_px(self):
        return self._drawable_size_px

    @drawable_size_px.setter
    def drawable_size_px(self, drawable_size_px):
        self._drawable_size_px = max(0, int(round(drawable_size_px)))

    @property
    def margin_px(self):
        return self._margin_px

    @margin_px.setter
    def margin_px(self, margin_px):
        self._margin_px = max(0, int(round(margin_px)))

    @property
    def min_grid_lines(self):
        return self._min_grid_lines

    @min_grid_lines.setter
    def min_grid_lines(self, min_grid_lines):
        self._min_grid_lines = max(1, int(round(min_grid_lines)))

    @property
    def _font_offset(self):
        return self.label_font[1] // 2 + 1

    def _lat_to_y(self, latitude, pixels_per_degree, lat_max):
        """
        Converts a latitude in degrees to a canvas y-coordinate in pixels. 'lat_max' is placed the
        margin-distance away from the top of the canvas and other latitudes placed relative to that
        Returns a coordinate in pixels as an int
        """
        return int(round((lat_max - latitude) * pixels_per_degree + self.margin_px))

    def _long_to_x(self, longitude, pixels_per_degree, long_min):
        """
        Converts a longitude in degrees to a canvas x-coordinate in pixels. 'long_min' is placed the
        margin-distance away from the left of the canvas and other longitudes placed relative to that
        Returns a coordinate in pixels as an int
        """
        return int(round((longitude - long_min) * pixels_per_degree + self.margin_px))

    def _points(self, itinerary):
        """
        Computes the canvas x and y coordinates for the cities in an itinerary
        Returns a generator yielding tuples of ints the form (x, y)
        """

        pixels_per_degree = self._pixels_per_degree(itinerary)

        if itinerary.is_single_point:
            mid_point = int(self._margin_px + self.drawable_size_px / 2)
            return ((x, y) for x, y in [(mid_point, mid_point)])
        else:
            return ((self._long_to_x(longitude=longitude, pixels_per_degree=pixels_per_degree,
                                     long_min=itinerary.longitude_min),
                     self._lat_to_y(latitude=latitude, pixels_per_degree=pixels_per_degree,
                                    lat_max=itinerary.latitude_max))
                    for latitude, longitude in itinerary.coordinates())

    def _point_pairs(self, itinerary):
        """
        Computes the canvas x and y coordinates for the start and end cities for each leg of an itinerary
        Returns a generator yielding tuples of ints of the form ((x0, y0), (x1, y1))
        """
        pixels_per_degree = self._pixels_per_degree(itinerary)
        return (((self._long_to_x(longitude=long_0, pixels_per_degree=pixels_per_degree,
                                  long_min=itinerary.longitude_min),
                  self._lat_to_y(latitude=lat_0, pixels_per_degree=pixels_per_degree,
                                 lat_max=itinerary.latitude_max)),
                 (self._long_to_x(longitude=long_1, pixels_per_degree=pixels_per_degree,
                                  long_min=itinerary.longitude_min),
                  self._lat_to_y(latitude=lat_1, pixels_per_degree=pixels_per_degree,
                                 lat_max=itinerary.latitude_max)))
                for (lat_0, long_0), (lat_1, long_1) in itinerary.legs())

    def _canvas_dimensions(self, itinerary):
        """
        Computes the size of the canvas to fit around the map. The largest dimension (either latitude or longitude)
        is given the "drawable_size_px" number of pixels, and the other dimension an amount pro-rata. Each
        dimension is then packed with the margin either side
        Returns a tuple of ints of the form (width, height), each measured in pixels.
        """
        displayed_width = self.drawable_size_px
        displayed_height = self.drawable_size_px
        if not itinerary.is_single_point:
            lat_to_long_ratio = ((itinerary.latitude_max - itinerary.latitude_min)
                                 / (itinerary.longitude_max - itinerary.longitude_min))
            if lat_to_long_ratio > 1:
                displayed_width = int(round(displayed_width / lat_to_long_ratio))
            else:
                displayed_height = int(round(displayed_height * lat_to_long_ratio))

        return displayed_width + 2 * self.margin_px, displayed_height + 2 * self.margin_px

    def _max_range(self, itinerary):
        if itinerary.is_single_point:
            max_range = float(self.degrees_to_show_for_single_point)
        else:
            max_range = max(itinerary.longitude_max - itinerary.longitude_min,
                            itinerary.latitude_max - itinerary.latitude_min)
        return max_range

    def _pixels_per_degree(self, itinerary):
        return self.drawable_size_px / self._max_range(itinerary)

    def _grid_line_spacing(self, itinerary):
        max_range = self._max_range(itinerary)

        scale = 10 ** (log10(max_range / self.min_grid_lines) // 1)
        multiple = 10 ** (log10(max_range / self.min_grid_lines) % 1)

        if multiple < 2:
            grid_line_spacing_deg = scale * 1
        elif multiple < 5:
            grid_line_spacing_deg = scale * 2
        else:
            grid_line_spacing_deg = scale * 5

        return grid_line_spacing_deg

    def _grid_lines(self, itinerary, is_latitude):

        pixels_per_degree = self._pixels_per_degree(itinerary)
        margin_in_degrees = self.margin_px / pixels_per_degree

        if is_latitude:
            start_of_canvas_in_degrees = itinerary.latitude_min - margin_in_degrees
            end_of_canvas_in_degrees = itinerary.latitude_max + margin_in_degrees
            converter_function_to_pixels = self._lat_to_y
            max_allowed_deg = 90
            ref_point = itinerary.latitude_max
        else:
            start_of_canvas_in_degrees = itinerary.longitude_min - margin_in_degrees
            end_of_canvas_in_degrees = itinerary.longitude_max + margin_in_degrees
            converter_function_to_pixels = self._long_to_x
            max_allowed_deg = 180
            ref_point = itinerary.longitude_min

        if itinerary.is_single_point:
            start_of_canvas_in_degrees -= self.degrees_to_show_for_single_point / 2
            end_of_canvas_in_degrees += self.degrees_to_show_for_single_point / 2
            if is_latitude:
                ref_point += self.degrees_to_show_for_single_point / 2
            else:
                ref_point -= self.degrees_to_show_for_single_point / 2

        grid_line_spacing = self._grid_line_spacing(itinerary)
        rounding = -int(log10(grid_line_spacing) - 1)

        first_grid_line = grid_line_spacing * (start_of_canvas_in_degrees // grid_line_spacing + 1)

        for i in count(0):
            grid_line = first_grid_line + i * grid_line_spacing
            if grid_line > end_of_canvas_in_degrees:
                break
            else:
                if grid_line > max_allowed_deg:
                    grid_line_label = 180 - grid_line
                elif grid_line < -max_allowed_deg:
                    grid_line_label = -180 - grid_line
                else:
                    grid_line_label = grid_line
                yield (format(grid_line_label, f'.{rounding}f'),
                       converter_function_to_pixels(grid_line, pixels_per_degree, ref_point))

    def _draw_grid_line(self, canvas, x0, y0, x1, y1, label, anchor):
        canvas.create_line(x0, y0, x1, y1, fill=self.grid_line_colour, width=self.grid_line_thickness)
        if anchor == N:
            y0 += self._font_offset
        else:
            x0 += self._font_offset
        canvas.create_text(x0, y0, text=label, anchor=anchor, font=self.label_font)

    def _draw_city(self, canvas, x, y, label):
        canvas.create_oval(x - self.city_radius, y - self.city_radius,
                           x + self.city_radius, y + self.city_radius,
                           fill=self.city_fill, outline=self.city_line_colour,
                           width=self.city_line_thickness)
        canvas.create_text(x, y - self._font_offset, text=label, anchor=S, font=self.label_font)

    def draw(self, itinerary, canvas):
        canvas.update()
        canvas.delete('all')

        # resize canvas
        canvas_width_px, canvas_height_px = self._canvas_dimensions(itinerary)
        canvas.config(width=0, height=0)
        canvas.config(width=canvas_width_px, height=canvas_height_px)

        # draw gridlines
        for label, y in self._grid_lines(itinerary, is_latitude=True):
            self._draw_grid_line(canvas=canvas, x0=0, y0=y, x1=canvas_width_px, y1=y, label=label, anchor=W)

        for label, x in self._grid_lines(itinerary, is_latitude=False):
            self._draw_grid_line(canvas=canvas, x0=x, y0=0, x1=x, y1=canvas_height_px, label=label, anchor=N)

        # draw legs
        for (x_0, y_0), (x_1, y_1) in self._point_pairs(itinerary):
            canvas.create_line(x_0, y_0, x_1, y_1, fill=self.leg_line_colour, width=self.leg_line_thickness)

        # draw cities
        for i, (x, y) in enumerate(self._points(itinerary)):
            self._draw_city(canvas=canvas, x=x, y=y, label=str(i + 1))


class TravellingSalesman:
    def __init__(self, road_map):
        self.itinerary = Itinerary(road_map=road_map)
        self.drawer = ItineraryDrawer()

        self._window = Tk()
        self._control_frame = Frame(master=self._window)
        self._control_frame.grid(column=0, row=0, sticky=N)

        self._open_button = Button(master=self._control_frame, text='Open', command=self.open)
        self._open_button.grid(column=0, row=0, columnspan=3, sticky=N + E + W)
        self._re_route_button = Button(master=self._control_frame, text='Re-route', command=self.reroute)
        self._re_route_button.grid(column=0, row=1, columnspan=3, sticky=N + E + W)

        self._zoom_in_button = Button(master=self._control_frame, text='Zoom In', command=self.zoom_in)
        self._zoom_in_button.grid(column=0, row=2, columnspan=3, sticky=N + E + W)

        self._zoom_out_button = Button(master=self._control_frame, text='Zoom Out', command=self.zoom_out)
        self._zoom_out_button.grid(column=0, row=3, columnspan=3, sticky=N + E + W)

        self._up_button = Button(master=self._control_frame, text='up', command=self.pan_up)
        self._up_button.grid(column=1, row=4, sticky=N + E + W)

        self._left_button = Button(master=self._control_frame, text='left', command=self.pan_left)
        self._left_button.grid(column=0, row=5, sticky=N + E + W)

        self._right_button = Button(master=self._control_frame, text='right', command=self.pan_right)
        self._right_button.grid(column=2, row=5, sticky=N + E + W)

        self._down_button = Button(master=self._control_frame, text='down', command=self.pan_down)
        self._down_button.grid(column=1, row=6, sticky=N + E + W)

        self._canvas_frame = Frame(master=self._window)
        self._canvas_frame.grid(column=1, row=0, rowspan=2, sticky=N)
        self._canvas = Canvas(master=self._canvas_frame, bg='white')
        self._canvas.grid(column=0, row=0, sticky=N)
        self._cities_scroll_bar = Scrollbar(master=self._window, orient=VERTICAL)
        self._cities_list_box = Listbox(master=self._window, height=20, width=70, font='TkFixedFont')
        self._cities_scroll_bar.config(command=self._cities_list_box.yview)
        self._cities_list_box.config(yscrollcommand=self._cities_scroll_bar.set)
        self._cities_list_box.grid(column=2, row=0, sticky=N + E + S + W)
        self._cities_scroll_bar.grid(column=3, row=0, sticky=N + E + S + W)

        self._route_scroll_bar = Scrollbar(master=self._window, orient=VERTICAL)
        self._route_list_box = Listbox(master=self._window, height=20, width=70, font='TkFixedFont')
        self._route_scroll_bar.config(command=self._route_list_box.yview)
        self._route_list_box.config(yscrollcommand=self._route_scroll_bar.set)
        self._route_list_box.grid(column=2, row=1, sticky=N + E + S + W)
        self._route_scroll_bar.grid(column=3, row=1, sticky=N + E + S + W)

    def draw(self):
        self.drawer.draw(self.itinerary, self._canvas)

    def fill_text(self):
        self._cities_list_box.delete(0, END)
        self._route_list_box.delete(0, END)

        for i, line in enumerate(cities_as_string(self.itinerary.road_map).splitlines()):
            self._cities_list_box.insert(i, line)

        for i, line in enumerate(map_as_string(self.itinerary.road_map).splitlines()):
            self._route_list_box.insert(i, line)

    def reroute(self):
        self.itinerary.reroute()
        self.draw()
        self.fill_text()

    def open(self):
        path = open_map_dialogue_box()
        if path:
            try:
                road_map = read_cities(path)
                road_map = find_best_cycle(road_map)
            except Exception:
                messagebox.showinfo("Warning", "Unable to load selected file")
            else:
                self.itinerary = Itinerary(road_map=road_map)
                self.draw()
                self.fill_text()

    def zoom_in(self):
        x_offset = self._canvas.winfo_width() / 2
        y_offset = self._canvas.winfo_height() / 2
        self._canvas.scale("all", x_offset, y_offset, 1.25, 1.25)

    def zoom_out(self):
        x_offset = self._canvas.winfo_width() / 2
        y_offset = self._canvas.winfo_height() / 2
        self._canvas.scale("all", x_offset, y_offset, 0.8, 0.8)

    def pan_up(self):
        self._canvas.yview_scroll(-1, 'unit')

    def pan_down(self):
        self._canvas.yview_scroll(1, 'unit')

    def pan_left(self):
        self._canvas.xview_scroll(-1, 'unit')

    def pan_right(self):
        self._canvas.xview_scroll(1, 'unit')

    def launch(self):
        self.draw()
        self.fill_text()
        self._window.attributes('-topmost', 1)
        self._window.attributes('-topmost', 0)
        self._window.mainloop()


def visualise(road_map):
    """
    Open Gui to visualise a road map
    """
    TravellingSalesman(road_map).launch()


def open_map_dialogue_box():
    """
    Ask user for a file. Use with the dialouge_box context manager when no root window already
    """
    return filedialog.askopenfilename(initialdir="/", title="Select Route Map File",
                                      filetypes=(("text files", "*.txt"), ("all files", "*.*")))


def rootless_dialogue_box(func):
    """
    decorator for dialogue boxes opened without an existing root window - ensures
    root is created, hidden and destroyed.
    """

    def wrapper(*args, **kwargs):
        root = Tk()
        root.withdraw()
        result = func(*args, **kwargs)
        root.destroy()
        return result

    return wrapper


@rootless_dialogue_box
def open_map():
    return open_map_dialogue_box()


@rootless_dialogue_box
def yes_no(question):
    return messagebox.askyesno(message=question, icon='question', title='Travelling Salesman')


def main():
    """
    Reads in, and prints out, the city data, then creates the "best" cycle and prints it out.
    """
    load_maps = True
    while load_maps:
        file_path = open_map()
        if not file_path:
            load_maps = yes_no(question='No file specified, would you like to try again?')
        else:
            try:
                road_map = read_cities(file_name=file_path)
            except Exception:
                load_maps = yes_no(question='Unable to Load file given, would you like to select a different file?')
            else:
                print('The following cities were loaded')
                print_cities(road_map=road_map)
                road_map = find_best_cycle(road_map=road_map)
                print_map(road_map=road_map)
                visualise(road_map=road_map)
                load_maps = yes_no(question='Would you like to open another map?')


if __name__ == "__main__":  # keep this in
    main()
