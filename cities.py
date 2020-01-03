from math import sqrt, log10
from random import randint, shuffle
from tkinter import filedialog, messagebox
from tkinter import *
from itertools import chain, count, tee


def read_cities(file_name):
    """Read File and return road_map

    :param file_name (str): a path to the file containing the road_map
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
        line = line.rstrip().split(sep='\t')
        lines.append((str(line[0]), str(line[1]), float(line[2]), float(line[3])))
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
    for i, (state, city, lat, long) in enumerate(road_map):
        result += f'{i + 1:<4} {state:<20.20} {city:<20.20}  {lat:>8.2f}   {long:>8.2f}\n'
    return result


def distance(start, destination):
    """Calculates the Euclidean distance between two cities assuming flat world

    :param start: a tuple of the form (state, city, latitude, longitude)
    :param destination: (state, city, latitude, longitude)
    :return (float): the Euclidean distance between the two cities
    """

    return sqrt((destination[2] - start[2]) ** 2 + (destination[3] - start[3]) ** 2)


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
    for city1, city2 in zip(road_map, road_map[1:] + [road_map[0]]):
        dist = distance(city1, city2)
        result += f'{city1[1]:>20.20} --> {city2[1]:<20.20}  {dist:>8.2f}\n'
    result += '                                           -------------\n'
    total = compute_total_distance(road_map=road_map)
    result += f'                              Total Distance   {total:8.2f}\n'
    return result


def pairwise_circuit(iterable):
    """Yields pairs of adjacent elements from an iterable. The last element is paired with the first

    :param iterable: any iterable
    :return: iterator yielding pairs of form (x_i, x_i+1) for 0 <= i < n, and final pair (x_n, x_0)
    """
    a, b = tee(iterable)
    b = chain(b, [next(b)])
    return zip(a, b)


def compute_total_distance(road_map):
    """Computes the sum of the distances of all the connections in the `road_map`.
    :param road_map: list of four-tuples: [(state, city, latitude, longitude), ...]
    :return: float
    """
    return sum(distance(start=city1, destination=city2) for city1, city2 in pairwise_circuit(road_map))


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

    def _reset_extrema(self):
        self._lat_max = max(latitude for _, _, latitude, _ in self.road_map)
        self._lat_min = min(latitude for _, _, latitude, _ in self.road_map)
        self._long_max = max(longitude for _, _, _, longitude in self.road_map)
        self._long_min = min(longitude for _, _, _, longitude in self.road_map)

    @property
    def road_map(self):
        return self._road_map

    @road_map.setter
    def road_map(self, road_map):
        self._road_map = road_map
        self._reset_extrema()

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
        return (len(self.road_map) == 1 or abs(self._lat_max - self._lat_min + self._long_max - self._long_min) < 1e-10)

    def reroute(self):
        shuffle(self.road_map)
        self.road_map = find_best_cycle(self.road_map)

    def coordinates(self):
        return ((latitude, longitude) for _, _, latitude, longitude in self.road_map)

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

    def _points(self, itinerary, pixels_per_degree):
        """
        Computes the canvas x and y coordinates for the cities in an itinerary
        Returns a generator yielding tuples of ints the form (x, y)
        """
        # offset = self.DEGREES_TO_SHOW_FOR_SINGLE_POINT / 2 if itinerary.single_point else 0
        if itinerary.is_single_point:
            mid_point = int(self._margin_px + self.drawable_size_px / 2)
            return ((x, y) for x, y in [(mid_point, mid_point)])
        else:
            return ((self._long_to_x(longitude=longitude, pixels_per_degree=pixels_per_degree,
                                     long_min=itinerary.longitude_min),
                     self._lat_to_y(latitude=latitude, pixels_per_degree=pixels_per_degree,
                                    lat_max=itinerary.latitude_max))
                    for latitude, longitude in itinerary.coordinates())

    def _point_pairs(self, itinerary, pixels_per_degree):
        """
        Computes the canvas x and y coordinates for the start and end cities for each leg of an itinerary
        Returns a generator yielding tuples of ints of the form ((x0, y0), (x1, y1))
        """
        return (((self._long_to_x(longitude=long_0, pixels_per_degree=pixels_per_degree,
                                  long_min=itinerary.longitude_min),
                  self._lat_to_y(latitude=lat_0, pixels_per_degree=pixels_per_degree,
                                 lat_max=itinerary.latitude_max)),
                 (self._long_to_x(longitude=long_1, pixels_per_degree=pixels_per_degree,
                                  long_min=itinerary.longitude_min),
                  self._lat_to_y(latitude=lat_1, pixels_per_degree=pixels_per_degree,
                                 lat_max=itinerary.latitude_max)))
                for (lat_0, long_0), (lat_1, long_1) in itinerary.legs())

    def _canvas_dimensions(self, lat_range, long_range):
        """
        Computes the size of the canvas to fit around the map. The largest dimension (either latitude or longitude)
        is given the "drawable_size_px" number of pixels, and the other dimension an amount pro-rata. Each
        dimension is then packed with the margin either side
        Returns a tuple of ints of the form (width, height), each measured in pixels.
        """
        if lat_range > long_range:
            canvas_height_px = int(round(self.drawable_size_px + 2 * self.margin_px))
            canvas_width_px = int(round(self.drawable_size_px * long_range / lat_range + 2 * self.margin_px))
        else:
            canvas_width_px = int(round(self.drawable_size_px + 2 * self.margin_px))
            canvas_height_px = int(round(self.drawable_size_px * lat_range / long_range + 2 * self.margin_px))

        return canvas_width_px, canvas_height_px


    def _grid_line_spacing(self, itinerary):
        if itinerary.is_single_point:
            max_range = self.degrees_to_show_for_single_point
        else:
            max_range = max(itinerary.longitude_max-itinerary.longitude_min,
                            itinerary.latitude_max-itinerary.latitude_min)

        scale = 10 ** (log10(max_range / self.min_grid_lines) // 1)
        multiple = 10 ** (log10(max_range / self.min_grid_lines) % 1)

        if multiple < 2:
            grid_line_spacing_deg = scale * 1
        elif multiple < 5:
            grid_line_spacing_deg = scale * 2
        else:
            grid_line_spacing_deg = scale * 5

        return grid_line_spacing_deg

    def _grid_lines(self, grid_line_spacing, deg_min, deg_max, pixels_per_degree, converter,
                    ref_point, max_allowed_deg):
        margin_in_degrees = self.margin_px / pixels_per_degree
        start_of_canvas_in_degrees = deg_min - margin_in_degrees
        end_of_canvas_in_degrees = deg_max + margin_in_degrees
        first_grid_line = grid_line_spacing * (start_of_canvas_in_degrees // grid_line_spacing + 1)
        for i in count(0):
            grid_line = first_grid_line + i * grid_line_spacing
            if grid_line > end_of_canvas_in_degrees:
                break
            else:
                # deal with gridlines that go over poles or international date line (should only happen in margins)
                if grid_line > max_allowed_deg:
                    grid_line_label = 180 - grid_line
                elif grid_line < -max_allowed_deg:
                    grid_line_label = -180 - grid_line
                else:
                    grid_line_label = grid_line

                yield grid_line_label, converter(grid_line, pixels_per_degree, ref_point)

    def _lat_grid_lines(self, grid_line_spacing, lat_min, lat_max, pixels_per_degree):
        return self._grid_lines(grid_line_spacing=grid_line_spacing, deg_min=lat_min, deg_max=lat_max,
                                pixels_per_degree=pixels_per_degree, converter=self._lat_to_y,
                                ref_point=lat_max, max_allowed_deg=90)

    def _long_grid_lines(self, grid_line_spacing, long_min, long_max, pixels_per_degree):
        return self._grid_lines(grid_line_spacing=grid_line_spacing, deg_min=long_min, deg_max=long_max,
                                pixels_per_degree=pixels_per_degree, converter=self._long_to_x,
                                ref_point=long_min, max_allowed_deg=180)

    def draw(self, itinerary, canvas):
        canvas.update()
        canvas.delete('all')

        # get map dimensions
        lat_min, lat_max = itinerary.latitude_min, itinerary.latitude_max
        long_min, long_max = itinerary.longitude_min, itinerary.longitude_max
        lat_range, long_range = lat_max - lat_min, long_max - long_min
        max_range = max(lat_range, long_range)

        if max_range == 0:
            # deal with case where all points are same (or just one point)
            max_range = 1
            long_range += 1
            lat_range += 1
            lat_min -= 0.5
            lat_max += 0.5
            long_min -= 0.5
            long_max += 0.5

        pixels_per_degree = self.drawable_size_px / max_range

        # resize canvas
        canvas_width_px, canvas_height_px = self._canvas_dimensions(lat_range, long_range)
        canvas.config(width=canvas_width_px, height=canvas_height_px)

        # draw gridlines
        grid_line_spacing = self._grid_line_spacing(itinerary)
        rounding = -int(log10(grid_line_spacing) - 1)

        for deg, y in self._lat_grid_lines(grid_line_spacing, lat_min, lat_max, pixels_per_degree):
            canvas.create_line(0, y, canvas_width_px, y, fill=self.grid_line_colour, width=self.grid_line_thickness)
            canvas.create_text(5, y - 5, text=format(deg, f'.{rounding}f'), anchor=SW, font=self.label_font)

        for deg, x in self._long_grid_lines(grid_line_spacing, long_min, long_max, pixels_per_degree):
            canvas.create_line(x, 0, x, canvas_height_px, fill=self.grid_line_colour, width=self.grid_line_thickness)
            canvas.create_text(x, 5, text=format(deg, f'.{rounding}f'), anchor=N, font=self.label_font)

        # draw legs
        for (x_0, y_0), (x_1, y_1) in self._point_pairs(itinerary, pixels_per_degree):
            canvas.create_line(x_0, y_0, x_1, y_1, fill=self.leg_line_colour, width=self.leg_line_thickness)

        # draw cities
        for i, (x, y) in enumerate(self._points(itinerary, pixels_per_degree)):
            canvas.create_oval(x - self.city_radius, y - self.city_radius, x + self.city_radius, y + self.city_radius,
                               fill=self.city_fill, outline=self.city_line_colour, width=self.city_line_thickness)
            canvas.create_text(x, y - 5, text=str(i + 1), anchor=S, font=self.label_font)


class TravellingSalesman:
    def __init__(self, road_map):
        self.itinerary = Itinerary(road_map=road_map)
        self.drawer = ItineraryDrawer()

        self._window = Tk()
        self._control_frame = Frame(master=self._window)
        self._open_button = Button(master=self._control_frame, text='Open', command=self.open)
        self._re_route_button = Button(master=self._control_frame, text='Re-route', command=self.reroute)
        self._control_frame.grid(column=0, row=0, sticky=N)
        self._open_button.grid(column=0, row=0, sticky=N + E + W)
        self._re_route_button.grid(column=0, row=1, sticky=N + E + W)

        self._canvas = Canvas(master=self._window, bg='white')
        self._canvas.grid(column=1, row=0, rowspan=2, sticky=N)

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
    app = TravellingSalesman(road_map)
    app.launch()


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
