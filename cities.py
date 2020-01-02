from math import sqrt, log10
from random import randint, shuffle
from tkinter import filedialog, messagebox
from tkinter import *
from itertools import chain


def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return
    them as a list of four-tuples: [(state, city, latitude, longitude), ...]
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
    """
    Prints a list of cities, along with their locations.
    """
    print(cities_as_string(road_map=road_map))


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

    print(map_as_string(road_map=road_map))


def map_as_string(road_map):
    result = 'Estimated optimal cycle:\n\n'
    for city1, city2 in zip(road_map, road_map[1:] + [road_map[0]]):
        dist = distance(city1, city2)
        result += f'{city1[1]:>20.20} --> {city2[1]:<20.20}  {dist:>8.2f}\n'
    result += '                                           -------------\n'
    total = compute_total_distance(road_map=road_map)
    result += f'                              Total Distance   {total:8.2f}\n'
    return result


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all the connections in the `road_map`.
    """
    return sum(distance(city_1=city1, city_2=city2) for city1, city2 in zip(road_map, road_map[1:] + [road_map[0]]))


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

    def __len__(self):
        return len(self.road_map)

    def _reset_extrema(self):
        self._lat_max = max(self.latitudes())
        self._lat_min = min(self.latitudes())
        self._long_max = max(self.longitudes())
        self._long_min = min(self.longitudes())

    @property
    def road_map(self):
        return self._road_map

    @road_map.setter
    def road_map(self, road_map):
        self._road_map = road_map
        self._reset_extrema()

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

    def coordinates(self):
        return ((latitude, longitude) for latitude, longitude in zip(self.latitudes(), self.longitudes()))

    def legs(self):
        starts = self.coordinates()
        destinations = self.coordinates()
        # pop first element of destinations and add to the back
        destinations = chain(destinations, [next(destinations)])
        return ((start, destination) for start, destination in zip(starts, destinations))


class ItineraryDrawer:
    def __init__(self, drawable_size_px=700, margin_px=50, min_grid_lines=5, grid_line_colour='lightblue1',
                 grid_line_thickness=1, leg_line_colour='red', leg_line_thickness=1, city_radius=2, city_fill='white',
                 city_line_colour='black', city_line_thickness=1, label_font=('purisa', 8)):
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

    def _lat_to_y(self, latitude, px_per_deg, lat_max):
        return int(round((lat_max - latitude) * px_per_deg + self.margin_px))

    def _long_to_x(self, longitude, px_per_deg, long_min):
        return int(round((longitude - long_min) * px_per_deg + self.margin_px))

    def _points(self, itinerary, px_per_deg, lat_max, long_min):
        return ((self._long_to_x(longitude=longitude, px_per_deg=px_per_deg, long_min=long_min),
                 self._lat_to_y(latitude=latitude, px_per_deg=px_per_deg, lat_max=lat_max))
                for latitude, longitude in itinerary.coordinates())

    def _point_pairs(self, itinerary, px_per_deg, lat_max, long_min):
        return (((self._long_to_x(longitude=long_0, px_per_deg=px_per_deg, long_min=long_min),
                  self._lat_to_y(latitude=lat_0, px_per_deg=px_per_deg, lat_max=lat_max)),
                 (self._long_to_x(longitude=long_1, px_per_deg=px_per_deg, long_min=long_min),
                  self._lat_to_y(latitude=lat_1, px_per_deg=px_per_deg, lat_max=lat_max)))
                for (lat_0, long_0), (lat_1, long_1) in itinerary.legs())

    def _canvas_dimensions(self, lat_range, long_range):
        if lat_range == long_range:
            canvas_height_px = self.drawable_size_px + 2 * self.margin_px
            canvas_width_px = self.drawable_size_px + 2 * self.margin_px
        elif lat_range > long_range:
            canvas_height_px = int(round(self.drawable_size_px + 2 * self.margin_px))
            canvas_width_px = int(round(self.drawable_size_px * long_range / lat_range + 2 * self.margin_px))
        else:
            canvas_width_px = int(round(self.drawable_size_px + 2 * self.margin_px))
            canvas_height_px = int(round(self.drawable_size_px * lat_range / long_range + 2 * self.margin_px))

        return canvas_width_px, canvas_height_px

    def _grid_line_spacing(self, max_range):
        scale = 10 ** (log10(max_range / self.min_grid_lines) // 1)
        multiple = 10 ** (log10(max_range / self.min_grid_lines) % 1)

        if multiple < 2:
            grid_line_spacing_deg = scale * 1
        elif multiple < 5:
            grid_line_spacing_deg = scale * 2
        else:
            grid_line_spacing_deg = scale * 5

        return grid_line_spacing_deg

    def _grid_lines(self, grid_line_spacing, deg_min, deg_max, px_per_deg, converter, ref_point):
        margin_deg = self.margin_px / px_per_deg
        first_line = grid_line_spacing * (1 + (deg_min - margin_deg) // grid_line_spacing)
        for i in range(self.min_grid_lines * 3):
            grid_line = first_line + i * grid_line_spacing
            if grid_line > deg_max + margin_deg:
                break
            else:
                yield grid_line, converter(grid_line, px_per_deg, ref_point)

    def _lat_grid_lines(self, grid_line_spacing, lat_min, lat_max, px_per_deg):
        return self._grid_lines(grid_line_spacing=grid_line_spacing, deg_min=lat_min, deg_max=lat_max,
                                px_per_deg=px_per_deg, converter=self._lat_to_y, ref_point=lat_max)

    def _long_grid_lines(self, grid_line_spacing, long_min, long_max, px_per_deg):
        return self._grid_lines(grid_line_spacing=grid_line_spacing, deg_min=long_min, deg_max=long_max,
                                px_per_deg=px_per_deg, converter=self._long_to_x, ref_point=long_min)

    def draw(self, itinerary, canvas):
        canvas.update()
        canvas.delete('all')

        ''' get map dimensions'''
        lat_min, lat_max = itinerary.latitude_min(), itinerary.latitude_max()
        long_min, long_max = itinerary.longitude_min(), itinerary.longitude_max()
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
        px_per_deg = self.drawable_size_px / max_range

        ''' resize canvas '''
        canvas_width_px, canvas_height_px = self._canvas_dimensions(lat_range, long_range)
        canvas.config(width=canvas_width_px, height=canvas_height_px)

        ''' draw gridlines '''
        grid_line_spacing = self._grid_line_spacing(max_range)
        rounding = -int(log10(grid_line_spacing) - 1)

        for deg, y in self._lat_grid_lines(grid_line_spacing, lat_min, lat_max, px_per_deg):
            canvas.create_line(0, y, canvas_width_px, y, fill=self.grid_line_colour, width=self.grid_line_thickness)
            canvas.create_text(5, y - 5, text=format(deg, f'.{rounding}f'), anchor=SW, font=self.label_font)

        for deg, x in self._long_grid_lines(grid_line_spacing, long_min, long_max, px_per_deg):
            canvas.create_line(x, 0, x, canvas_height_px, fill=self.grid_line_colour, width=self.grid_line_thickness)
            canvas.create_text(x, 5, text=format(deg, f'.{rounding}f'), anchor=NW, font=self.label_font)

        ''' draw legs '''
        for (x_0, y_0), (x_1, y_1) in self._point_pairs(itinerary, px_per_deg, lat_max, long_min):
            canvas.create_line(x_0, y_0, x_1, y_1, fill=self.leg_line_colour, width=self.leg_line_thickness)

        ''' draw cities '''
        for i, (x, y) in enumerate(self._points(itinerary, px_per_deg, lat_max, long_min)):
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


class dialogue_box:
    """
    context manager for dialogue boxes from TKinter
    Handles the underlying root window creation, hiding and destruction
    """
    def __enter__(self):
        """ create root window and hide it"""
        self._root = Tk()
        self._root.withdraw()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ destroy root window when dialogue box has been used"""
        self._root.destroy()

    @staticmethod
    def get_file_name():
        return open_map_dialogue_box()

    @staticmethod
    def yes_no_question(question):
        """ return boolean regarding whether user wants to perform given action"""
        return messagebox.askyesno(message=question, icon='question', title='Travelling Salesman')


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"cycle and prints it out.
    """
    load_another_map = True
    while load_another_map:
        with dialogue_box() as box:
            file_path = box.get_file_name()
        if not file_path:
            with dialogue_box() as box:
                load_another_map = box.yes_no_question(
                    question='No file specified, would you like to try again?')
        else:
            try:
                road_map = read_cities(file_name=file_path)
            except Exception:
                with dialogue_box() as box:
                    load_another_map = box.yes_no_question(
                        question='Unable to Load file given, would you like to select a different file?')
            else:
                print('The following cities were loaded')
                print_cities(road_map=road_map)
                road_map = find_best_cycle(road_map=road_map)
                print_map(road_map=road_map)
                visualise(road_map=road_map)
                with dialogue_box() as box:
                    load_another_map = box.yes_no_question(question='Would you like to open another map?')


if __name__ == "__main__":  # keep this in
    main()
