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
    def __init__(self, drawable_size_px=700, margin_px=50, min_grid_lines=5):
        self._drawable_size_px = drawable_size_px
        self._margin_px = margin_px
        self._min_grid_lines = min_grid_lines

    def _points(self, itinerary, px_per_deg, lat_max, long_min):
        x_coords = ((longitude-long_min) * px_per_deg + self._margin_px for longitude in itinerary.longitudes())
        y_coords = ((lat_max-latitude) * px_per_deg + self._margin_px for latitude in itinerary.latitudes())
        return ((x,y) for x, y in zip(x_coords, y_coords))

    def _point_pairs(self, itinerary, px_per_deg, lat_max, long_min):
        p0 = self._points(itinerary, px_per_deg, lat_max, long_min)
        p1 = self._points(itinerary, px_per_deg, lat_max, long_min)
        #pop first element of p1 and add to the back
        p1=chain(p1,[next(p1)])
        return (((x_0, y_0), (x_1, y_1)) for (x_0, y_0), (x_1, y_1) in zip(p0, p1))

    def _canvas_dimensions(self, lat_range, long_range):
        if lat_range > long_range:
            canvas_height_px = self._drawable_size_px + 2*self._margin_px
            canvas_width_px = self._drawable_size_px * long_range / lat_range + 2*self._margin_px
        else:
            canvas_width_px = self._drawable_size_px + 2*self._margin_px
            canvas_height_px = self._drawable_size_px * lat_range / long_range +2*self._margin_px

        return canvas_width_px, canvas_height_px

    def _grid_line_spacing(self, max_range):
        scale = 10 ** (log10(max_range / self._min_grid_lines) // 1)
        multiple = 10 ** (log10(max_range / self._min_grid_lines) % 1)

        if multiple < 2:
            grid_line_spacing_deg = scale * 1
        elif multiple < 5:
            grid_line_spacing_deg = scale * 2
        else:
            grid_line_spacing_deg = scale * 5

        return grid_line_spacing_deg

    def _lat_gridlines(self, grid_line_spacing, lat_min, lat_max, px_per_deg):
        margin_deg = self._margin_px / px_per_deg
        deg = grid_line_spacing * (1 + (lat_min - margin_deg) // grid_line_spacing)
        while deg < lat_max + margin_deg:
            y = (lat_max - deg) * px_per_deg + self._margin_px
            yield deg, y
            deg += grid_line_spacing

    def _long_gridlines(self, grid_line_spacing, long_min, long_max, px_per_deg):
        margin_deg = self._margin_px / px_per_deg
        deg = grid_line_spacing * (1 + (long_min - margin_deg) // grid_line_spacing)
        while deg < long_max + margin_deg:
            x = (deg - long_min) * px_per_deg + self._margin_px
            yield deg, x
            deg += grid_line_spacing

    def draw(self, itinerary, canvas):
        canvas.update()
        canvas.delete('all')

        ''' get map dimensions'''

        lat_min, lat_max = itinerary.latitude_min(), itinerary.latitude_max()
        long_min, long_max = itinerary.longitude_min(), itinerary.longitude_max()
        lat_range, long_range = lat_max - lat_min, long_max - long_min

        ''' resize canvas '''

        canvas_width_px, canvas_height_px =  self._canvas_dimensions(lat_range, long_range)
        canvas.config(width=canvas_width_px, height=canvas_height_px)

        ''' draw gridlines '''

        max_range = max(lat_range, long_range)
        px_per_deg = self._drawable_size_px / max_range
        grid_line_spacing = self._grid_line_spacing(max_range)

        for deg, y in self._lat_gridlines(grid_line_spacing, lat_min, lat_max, px_per_deg):
            canvas.create_line(0, y, canvas_width_px, y, fill="lightblue1")
            canvas.create_text(5, y - 5, text=str(round(deg,1)), anchor=SW, font=('purisa', 8))


        for deg, x in self._long_gridlines(grid_line_spacing, long_min, long_max, px_per_deg):
            canvas.create_line(x, 0, x, canvas_height_px, fill="lightblue1")
            canvas.create_text(x, 5, text=str(round(deg,1)), anchor=NW, font=('purisa', 8))


        ''' draw route cities '''

        for (x_0, y_0), (x_1, y_1) in self._point_pairs(itinerary, px_per_deg, lat_max, long_min):
            canvas.create_line(x_0, y_0, x_1, y_1, fill="red")

        for i, (x, y) in enumerate(self._points(itinerary, px_per_deg, lat_max, long_min)):
            canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill='white', outline='black', width=1)
            canvas.create_text(x, y - 5, text=str(i + 1), anchor=S, font=('purisa', 8))



class TravellingSalesman:
    def __init__(self, road_map):
        self.itinerary = Itinerary(road_map=road_map)
        self.drawer = ItineraryDrawer(drawable_size_px=700, margin_px=50, min_grid_lines=5)
        self.window = Tk()
        self.control_frame = Frame(master=self.window)
        self.open_button = Button(master=self.control_frame, text='Open', command=self.open)
        self.re_route_button = Button(master=self.control_frame, text='Re-route', command=self.reroute)
        self.canvas = Canvas(master=self.window, bg='white')

        self.control_frame.grid(column=0, row=0, sticky=N)
        self.open_button.grid(column=0, row=0, sticky=N + E + W)
        self.re_route_button.grid(column=0, row=1, sticky=N + E + W)
        self.canvas.grid(column=1, row=0, sticky=N)
        self.canvas.config(height=700, width=700)

    def draw(self):
        self.drawer.draw(self.itinerary,self.canvas)

    def reroute(self):
        self.itinerary.reroute()
        self.draw()

    def open(self):
        path = filedialog.askopenfilename(initialdir="/", title="Select Route Map File",
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        if path:
            try:
                road_map = read_cities(path)
                road_map = find_best_cycle(road_map)
            except:
                messagebox.showinfo("Warning", "Unable to load selected file")
            else:
                self.itinerary = Itinerary(road_map=road_map)
                self.draw()

    def mainloop(self):
        self.window.attributes('-topmost', 1)
        self.window.attributes('-topmost', 0)
        self.window.mainloop()


def visualise(road_map):

    app = TravellingSalesman(road_map)
    app.draw()
    app.mainloop()


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
        # file_path = get_file_name()
        file_path = 'city-data.txt'
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