import pytest
import random
import types

from cities import *


# read_cities tests

def test_read_cities_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_cities('gobblydigook.notatextfile')
        read_cities('thisfiledoes.not.exist')


def test_read_cities_returns_list():
    assert isinstance(read_cities('test-city-data.txt'), list)


def test_read_cities_returns_list_of_tuples():
    cities = read_cities('test-city-data.txt')
    for i in cities:
        assert isinstance(i, tuple)


def test_read_cities_returns_tuples_of_right_size():
    cities = read_cities('test-city-data.txt')
    for i in cities:
        assert len(i) == 4


def test_read_cities_returns_tuples_with_members_of_right_type():
    cities = read_cities('test-city-data.txt')
    for city in cities:
        for i in range(4):
            assert isinstance(city[i], [str, float][i // 2])


def test_read_cities_returns_list_of_right_length():
    assert len(read_cities('test-city-data.txt')) == 3


def test_read_cities_test_data_as_expected():
    expected_data = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                     ('Alaska', 'Juneau', 58.301935, -134.41974),
                     ('Arizona', 'Phoenix', 33.448457, - 112.073844)]
    actual_data = read_cities('test-city-data.txt')
    for city in range(3):
        for i in range(2):
            assert actual_data[city][i] == expected_data[city][i]
            assert actual_data[city][i + 2] == pytest.approx(expected_data[city][i + 2])


# tests for distance
def test_distance_calculates_as_expected_1():
    city1 = ('Rhode Island', 'Providence', 41.82355, -71.422132)
    city2 = ('South Carolina', 'Columbia', 34.0, -81.035)
    assert distance(city1, city2) == pytest.approx(12.39415853)


def test_distance_calculates_as_expected_2():
    city1 = ('Delaware', 'Dover', 39.161921, -75.526755)
    city2 = ('Florida', 'Tallahassee', 30.4518, -84.27277)
    assert distance(city1, city2) == pytest.approx(12.34337823)


def test_distance_calculates_as_expected_3():
    city1 = ('North Carolina', 'Raleigh', 35.771, -78.638)
    city2 = ('North Dakota', 'Bismarck', 48.813343, -100.779004)
    assert distance(city1, city2) == pytest.approx(25.6968241)


def test_distance_calculates_as_expected_4():
    city1 = ('West Virginia', 'Charleston', 38.349497, -81.633294)
    city2 = ('Wisconsin', 'Madison', 43.074722, -89.384444)
    assert distance(city1, city2) == pytest.approx(9.077889492)


def test_distance_calculates_as_expected_5():
    city1 = ('Michigan', 'Lansing', 42.7335, -84.5467)
    city2 = ('Minnesota', 'Saint Paul', 44.95, -93.094)
    assert distance(city1, city2) == pytest.approx(8.830017528)


# compute_total_distance tests
def test_compute_total_distance_single_city():
    road_map = [('Michigan', 'Lansing', 42.7335, -84.5467)]
    assert compute_total_distance(road_map) == pytest.approx(0)


def test_compute_total_distance_repeated_city():
    road_map = [('Michigan', 'Lansing', 42.7335, -84.5467),
                ('Michigan', 'Lansing', 42.7335, -84.5467)]
    assert compute_total_distance(road_map) == pytest.approx(0)


def test_compute_total_distance_calculates_as_expected_1():
    road_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Delaware", "Dover", 39.161921, -75.526755),
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert compute_total_distance(road_map) == pytest.approx(9.386 + 18.496 + 10.646, 0.01)


def test_compute_total_distance_calculates_as_expected_2():
    road_map = [('Michigan', 'Lansing', 42.7335, -84.5467),
                ('Minnesota', 'Saint Paul', 44.95, -93.094),
                ('Mississippi', 'Jackson', 32.32, -90.207),
                ('Missouri', 'Jefferson City', 38.572954, -92.189283)]
    assert compute_total_distance(road_map) == pytest.approx(37.047094902)


def test_compute_total_distance_calculates_as_expected_3():
    road_map = [('New York', 'Albany', 42.659829, -73.781339),
                ('North Carolina', 'Raleigh', 35.771, -78.638),
                ('North Dakota', 'Bismarck', 48.813343, -100.779004),
                ('Ohio', 'Columbus', 39.962245, -83.000647),
                ('Oklahoma', 'Oklahoma City', 35.482309, -97.534994),
                ('Oregon', 'Salem', 44.931109, -123.029159),
                ('Pennsylvania', 'Harrisburg', 40.269789, -76.875613),
                ('Rhode Island', 'Providence', 41.82355, -71.422132)]
    assert compute_total_distance(road_map) == pytest.approx(150.9452)


def test_compute_total_distance_calculates_as_expected_pole_to_pole():
    road_map = [('The Arctic', 'North Pole', 90, -180),
                ('The Antarctic', 'South Pole', -90, 180)]
    assert compute_total_distance(road_map) == pytest.approx(804.984471899)


def test_compute_total_distance_calculates_as_expected_equatorial_trip():
    road_map = [('No Where', 'No Where', 0.0, 180.0),
                ('No Where', 'No Where', 0.0, -180.0)]
    assert compute_total_distance(road_map) == pytest.approx(720)


def test_compute_total_distance_returns_float():
    road_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Delaware", "Dover", 39.161921, -75.526755),
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert isinstance(compute_total_distance(road_map), float)


# Example cities for testing on
city_1 = ("Kentucky", "Frankfort", 38.197274, -84.86311)
city_2 = ("Delaware", "Dover", 39.161921, -75.526755)
city_3 = ("Minnesota", "Saint Paul", 44.95, -93.094)


# swap_cities tests
def test_swap_cities_in_place():
    map_in = [city_1, city_2, city_3]
    assert swap_cities(map_in, 0, 2)[0] is map_in


def test_swap_cities_as_expected_1():
    map_in = [city_1, city_2, city_3]
    map_out = swap_cities(map_in[:], 0, 2)[0]

    assert map_in[0] is map_out[2]
    assert map_in[2] is map_out[0]
    assert map_in[1] is map_out[1]


def test_swap_cities_as_expected_2():
    map_in = [city_1, city_2, city_3]
    map_out = swap_cities(map_in[:], 2, 1)[0]

    assert map_in[2] is map_out[1]
    assert map_in[1] is map_out[2]
    assert map_in[0] is map_out[0]


def test_swap_cities_same_city():
    map_in = [city_1, city_2, city_3]
    map_out = swap_cities(map_in[:], 1, 1)[0]

    assert map_in[0] is map_out[0]
    assert map_in[1] is map_out[1]
    assert map_in[2] is map_out[2]


def test_swap_cities_large_map():
    map_in = [('state', 'city', random.randint(-90, 90), random.randint(-180, 180)) for x in range(10000)]

    index_1, index_2 = (random.randint(0, 9999) for x in range(2))

    map_out = swap_cities(map_in[:], index_1, index_2)[0]

    for i in range(10000):
        if i == index_1:
            assert map_out[index_1] is map_in[index_2]
        elif i == index_2:
            assert map_out[index_2] is map_in[index_1]
        else:
            assert map_out[i] is map_in[i]


def test_swap_cities_returns_tuple():
    map_in = [city_1, city_2, city_3]
    assert isinstance(swap_cities(map_in[:], 0, 0), tuple)


def test_swap_cities_returns_tuple_length_2():
    map_in = [city_1, city_2, city_3]
    assert len(swap_cities(map_in[:], 0, 0)) == 2


def test_swap_cities_returns_list_and_float():
    map_in = [city_1, city_2, city_3]
    map_out, calculated_distance = swap_cities(map_in[:], 0, 1)
    assert isinstance(map_out, list)
    assert isinstance(calculated_distance, float)


def test_swap_cities_returns_list_of_same_length_as_input():
    map_in = [city_1, city_2, city_3]
    map_out = swap_cities(map_in[:], 1, 1)[0]
    assert len(map_out) == len(map_in)


# shift_cities tests
def test_shift_cities_in_place():
    map_in = [city_1, city_2, city_3]
    map_out = shift_cities(map_in)
    assert map_in == map_out


def test_shift_cities_as_expected_1():
    map_in = [city_1, city_2, city_3]
    map_out = shift_cities(map_in[:])

    assert map_in[0] is map_out[1]
    assert map_in[1] is map_out[2]
    assert map_in[2] is map_out[0]


def test_shift_cities_as_expected_2():
    map_in = [city_1, city_2, city_3]
    shift_cities(map_in)

    assert map_in[0] is city_3
    assert map_in[1] is city_1
    assert map_in[2] is city_2


def test_shift_cities_two_shifts():
    map_in = [city_1, city_2, city_3]
    shift_cities(map_in)
    shift_cities(map_in)

    assert map_in[0] is city_2
    assert map_in[1] is city_3
    assert map_in[2] is city_1


def test_shift_cities_one_city():
    map_in = [city_1]
    map_out = shift_cities(map_in[:])
    assert len(map_out) == 1
    assert map_out[0] is map_in[0]


def test_shift_cities_large_map():
    map_in = [('state', 'city', random.randint(-90, 90), random.randint(-180, 180)) for x in range(10000)]
    map_out = shift_cities(map_in[:])
    for i in range(10000):
        assert map_in[i] is map_out[(i + 1) % 10000]


def test_shift_cities_returns_list():
    map_in = [city_1, city_2, city_3]
    assert isinstance(shift_cities(map_in[:]), list)


def test_shift_cities_returns_list_of_same_length():
    for n in [1, 5, 10, 50, 100]:
        map_in = [('state', 'city', random.randint(-90, 90), random.randint(-180, 180)) for x in range(n)]
        assert len(shift_cities(map_in[:])) == n

        shift_cities(map_in)
        assert len(map_in) == n


def test_drawing_area_returns_numeric():
    a = drawing_area(500, 50)
    assert isinstance(a, int) or isinstance(a, float)


def test_drawing_area_expected_result_1():
    assert drawing_area(500, 50) == 400


def test_drawing_area_expected_result_2():
    assert drawing_area(50, 10) == 30


def test_drawing_area_expected_result_3():
    assert drawing_area(5000, 10) == 4980


def test_drawing_area_margin_all_of_canvas():
    assert drawing_area(50, 25) == 0


def test_drawing_area_margin_bigger_than_canvas():
    assert drawing_area(10, 25) == 0


def test_drawing_area_zero_canvas():
    assert drawing_area(0, 10) == 0


def test_drawing_area_negative_canvas_as_zero():
    assert drawing_area(-10, 10) == 0


def test_drawing_area_negative_margin_as_zero():
    assert drawing_area(100, -10) == 100


def test_longitude_to_x_as_expected_1():
    assert longitude_to_x(-100, -157.83, -69.77, 400, 50) == pytest.approx(312.68, abs=0.1)


def test_longitude_to_x_as_expected_2():
    assert longitude_to_x(101.71, 95.38, 127.72, 100, 20) == pytest.approx(39.57, abs=0.1)


def test_longitude_to_x_as_expected_3():
    assert longitude_to_x(33.3, -42.12, 127.76, 300, 10) == pytest.approx(143.2, abs=0.1)


def test_longitude_to_x_as_expected_4():
    assert longitude_to_x(25.06, 22.15, 147.74, 1000, 80) == pytest.approx(103.19, abs=0.1)


def test_longitude_to_x_as_expected_5():
    assert longitude_to_x(-53.08, -142.66, -0.42, 600, 200) == pytest.approx(577.86, abs=0.1)


def test_longitude_to_x_as_expected_6():
    assert longitude_to_x(-146.88, -153.81, -37.01, 400, 50) == pytest.approx(73.72, abs=0.1)


def test_longitude_to_x_as_expected_7():
    assert longitude_to_x(28.75, 0.74, 122.11, 100, 20) == pytest.approx(43.08, abs=0.1)


def test_longitude_to_x_as_expected_8():
    assert longitude_to_x(147.12, 31.18, 164.38, 300, 10) == pytest.approx(271.12, abs=0.1)


def test_longitude_to_x_returns_float_1():
    assert isinstance(longitude_to_x(155.38, 137.58, 160.34, 1000, 80), float)


def test_longitude_to_x_returns_float_2():
    assert isinstance(longitude_to_x(105.62, 95.25, 149.79, 600, 200), float)


def test_latitude_to_y_as_expected_1():
    assert latitude_to_y(92.38, 56.59, 122.15, 400, 50) == pytest.approx(231.62, abs=0.1)


def test_latitude_to_y_as_expected_2():
    assert latitude_to_y(166.93, 126.86, 171.29, 100, 20) == pytest.approx(29.81, abs=0.1)


def test_latitude_to_y_as_expected_3():
    assert latitude_to_y(66.17, -72.24, 122.37, 300, 10) == pytest.approx(96.63, abs=0.1)


def test_latitude_to_y_as_expected_4():
    assert latitude_to_y(119.61, -71.19, 167.74, 1000, 80) == pytest.approx(281.43, abs=0.1)


def test_latitude_to_y_as_expected_5():
    assert latitude_to_y(-38.28, -83.33, 114.53, 600, 200) == pytest.approx(663.38, abs=0.1)


def test_latitude_to_y_as_expected_6():
    assert latitude_to_y(86.35, -102.19, 172.43, 400, 50) == pytest.approx(175.38, abs=0.1)


def test_latitude_to_y_as_expected_7():
    assert latitude_to_y(-49.89, -55.83, -28.52, 100, 20) == pytest.approx(98.24, abs=0.1)


def test_latitude_to_y_as_expected_8():
    assert latitude_to_y(25.31, -7.52, 117.59, 300, 10) == pytest.approx(231.28, abs=0.1)


def test_gridline_spacing_as_expected_1():
    assert gridline_spacing(-170.88, -170.78) == pytest.approx(0.02, abs=0.1)


def test_gridline_spacing_as_expected_2():
    assert gridline_spacing(-166.78, -166.48) == pytest.approx(0.05, abs=0.1)


def test_gridline_spacing_as_expected_3():
    assert gridline_spacing(156.75, 157.37) == pytest.approx(0.1, abs=0.1)


def test_gridline_spacing_as_expected_4():
    assert gridline_spacing(-122.52, -120.67) == pytest.approx(0.2, abs=0.1)


def test_gridline_spacing_as_expected_5():
    assert gridline_spacing(35.2, 44.74) == pytest.approx(1, abs=0.1)


def test_gridline_spacing_as_expected_6():
    assert gridline_spacing(-12.75, 10.99) == pytest.approx(2, abs=0.1)


def test_gridline_spacing_as_expected_7():
    assert gridline_spacing(62.1, 111.32) == pytest.approx(5, abs=0.1)


def test_gridline_spacing_as_expected_8():
    assert gridline_spacing(49.18, 134.24) == pytest.approx(10, abs=0.1)


def test_gridline_spacing_returns_float_1():
    assert isinstance(gridline_spacing(-182.24, -158.5), float)


def test_gridline_spacing_returns_float_2():
    assert isinstance(gridline_spacing(-32.44, 52.62), float)


def test_gridline_locations_as_expected_1():
    expected = list(range(-160, -50, 10))
    received = gridline_coords(-157.83, -69.77, 400, 50)
    assert len(received) == len(expected)
    for coord_expected, coord_received in zip(expected, received):
        assert coord_expected == pytest.approx(coord_received, abs=0.01)


def test_gridline_locations_as_expected_2():
    expected = [9.8, 10, 10.2, 10.4, 10.6, 10.8, 11, 11.2]
    received = gridline_coords(10, 11, 300, 100)
    assert len(received) == len(expected)
    for coord_expected, coord_received in zip(expected, received):
        assert coord_expected == pytest.approx(coord_received, abs=0.01)


def test_gridline_locations_as_expected_3():
    expected = [-40, -20, 0, 20, 40, 60, 80, 100]
    received = gridline_coords(-25, 85, 300, 50)
    assert len(received) == len(expected)
    for coord_expected, coord_received in zip(expected, received):
        assert coord_expected == pytest.approx(coord_received, abs=0.01)


def test_gridline_locations_as_expected_4():
    expected = [-56, -55, -54, -53, -52, -51, -50, -49]
    received = gridline_coords(-55, -50, 200, 50)
    assert len(received) == len(expected)
    for coord_expected, coord_received in zip(expected, received):
        assert coord_expected == pytest.approx(coord_received, abs=0.01)


def test_gridline_locations_as_expected_5():
    expected = [69.85, 69.855, 69.86, 69.865, 69.87, 69.875, 69.88]
    received = gridline_coords(69.85, 69.88, 800, 50)
    assert len(received) == len(expected)
    for coord_expected, coord_received in zip(expected, received):
        assert coord_expected == pytest.approx(coord_received, abs=0.01)


def test_coordinates_returns_tuple_1():
    road_map = [('X', 'C', 6.1707, 6.4855),
                ('E', 'W', -1.4313, 138.1282),
                ('H', 'A', 18.7915, -128.7887),
                ('R', 'Y', 40.9942, -133.3007),
                ('C', 'V', -52.8836, -103.7741),
                ('B', 'R', -66.5549, -113.4921),
                ('L', 'N', 59.2405, 24.8351),
                ('M', 'B', -17.1408, 176.0781),
                ('X', 'L', 63.9711, -122.9314),
                ('K', 'K', 60.6304, 65.0157),
                ('T', 'I', -85.5885, -151.8833),
                ('K', 'G', -76.6842, -119.3297),
                ('Q', 'Q', -22.0429, 115.9045),
                ('U', 'S', -70.4604, 119.4519),
                ('K', 'C', -65.5839, 2.5201),
                ('R', 'K', -63.7202, -121.0386),
                ('R', 'A', -42.7979, 23.3631),
                ('Q', 'C', -1.9149, -57.7485)]
    assert isinstance(coordinates(road_map), tuple)


def test_coordinates_returns_tuple_2():
    road_map = [('N', 'E', -20.0695, 165.2267),
                ('B', 'F', 54.0981, 11.6462),
                ('Q', 'Z', -40.4051, 179.336),
                ('X', 'G', 77.9415, 173.0162),
                ('S', 'S', -28.6265, -62.7077),
                ('C', 'P', 10.5781, 2.8633),
                ('X', 'N', -81.6378, -56.6629),
                ('Z', 'D', 44.3644, -60.2304)]
    assert isinstance(coordinates(road_map), tuple)


def test_coordinates_returns_collection_of_lists_1():
    road_map = [('X', 'C', 6.1707, 6.4855),
                ('E', 'W', -1.4313, 138.1282),
                ('H', 'A', 18.7915, -128.7887),
                ('R', 'Y', 40.9942, -133.3007),
                ('C', 'V', -52.8836, -103.7741),
                ('B', 'R', -66.5549, -113.4921),
                ('L', 'N', 59.2405, 24.8351),
                ('M', 'B', -17.1408, 176.0781),
                ('X', 'L', 63.9711, -122.9314),
                ('K', 'K', 60.6304, 65.0157),
                ('T', 'I', -85.5885, -151.8833),
                ('K', 'G', -76.6842, -119.3297),
                ('Q', 'Q', -22.0429, 115.9045),
                ('U', 'S', -70.4604, 119.4519),
                ('K', 'C', -65.5839, 2.5201),
                ('R', 'K', -63.7202, -121.0386),
                ('R', 'A', -42.7979, 23.3631),
                ('Q', 'C', -1.9149, -57.7485)]
    for element in coordinates(road_map):
        assert isinstance(element, list)


def test_coordinates_returns_collection_of_lists_2():
    road_map = [('N', 'E', -20.0695, 165.2267),
                ('B', 'F', 54.0981, 11.6462),
                ('Q', 'Z', -40.4051, 179.336),
                ('X', 'G', 77.9415, 173.0162),
                ('S', 'S', -28.6265, -62.7077),
                ('C', 'P', 10.5781, 2.8633),
                ('X', 'N', -81.6378, -56.6629),
                ('Z', 'D', 44.3644, -60.2304)]
    for element in coordinates(road_map):
        assert isinstance(element, list)


def test_coordinates_right_length_1():
    road_map = [('X', 'C', 6.1707, 6.4855),
                ('E', 'W', -1.4313, 138.1282),
                ('H', 'A', 18.7915, -128.7887),
                ('R', 'Y', 40.9942, -133.3007),
                ('C', 'V', -52.8836, -103.7741),
                ('B', 'R', -66.5549, -113.4921),
                ('L', 'N', 59.2405, 24.8351),
                ('M', 'B', -17.1408, 176.0781),
                ('X', 'L', 63.9711, -122.9314),
                ('K', 'K', 60.6304, 65.0157),
                ('T', 'I', -85.5885, -151.8833),
                ('K', 'G', -76.6842, -119.3297),
                ('Q', 'Q', -22.0429, 115.9045),
                ('U', 'S', -70.4604, 119.4519),
                ('K', 'C', -65.5839, 2.5201),
                ('R', 'K', -63.7202, -121.0386),
                ('R', 'A', -42.7979, 23.3631),
                ('Q', 'C', -1.9149, -57.7485)]
    expected = (
        [6.1707, -1.4313, 18.7915, 40.9942, -52.8836, -66.5549, 59.2405, -17.1408, 63.9711, 60.6304, -85.5885, -76.6842,
         -22.0429, -70.4604, -65.5839, -63.7202, -42.7979, -1.9149],
        [6.4855, 138.1282, -128.7887, -133.3007, -103.7741, -113.4921, 24.8351, 176.0781, -122.9314, 65.0157, -151.8833,
         -119.3297, 115.9045, 119.4519, 2.5201, -121.0386, 23.3631, -57.7485])
    received = coordinates(road_map)
    assert len(received) == len(expected)
    assert len(received[0]) == len(expected[0])
    assert len(received[1]) == len(expected[1])


def test_coordinates_right_length_2():
    road_map = [('N', 'E', -20.0695, 165.2267),
                ('B', 'F', 54.0981, 11.6462),
                ('Q', 'Z', -40.4051, 179.336),
                ('X', 'G', 77.9415, 173.0162),
                ('S', 'S', -28.6265, -62.7077),
                ('C', 'P', 10.5781, 2.8633),
                ('X', 'N', -81.6378, -56.6629),
                ('Z', 'D', 44.3644, -60.2304)]
    expected = ([-20.0695, 54.0981, -40.4051, 77.9415, -28.6265, 10.5781, -81.6378, 44.3644],
                [165.2267, 11.6462, 179.336, 173.0162, -62.7077, 2.8633, -56.6629, -60.2304])
    received = coordinates(road_map)
    assert len(received) == len(expected)
    assert len(received[0]) == len(expected[0])
    assert len(received[1]) == len(expected[1])


def test_coordinates_as_expected_1():
    road_map = [('X', 'C', 6.1707, 6.4855),
                ('E', 'W', -1.4313, 138.1282),
                ('H', 'A', 18.7915, -128.7887),
                ('R', 'Y', 40.9942, -133.3007),
                ('C', 'V', -52.8836, -103.7741),
                ('B', 'R', -66.5549, -113.4921),
                ('L', 'N', 59.2405, 24.8351),
                ('M', 'B', -17.1408, 176.0781),
                ('X', 'L', 63.9711, -122.9314),
                ('K', 'K', 60.6304, 65.0157),
                ('T', 'I', -85.5885, -151.8833),
                ('K', 'G', -76.6842, -119.3297),
                ('Q', 'Q', -22.0429, 115.9045),
                ('U', 'S', -70.4604, 119.4519),
                ('K', 'C', -65.5839, 2.5201),
                ('R', 'K', -63.7202, -121.0386),
                ('R', 'A', -42.7979, 23.3631),
                ('Q', 'C', -1.9149, -57.7485)]
    expected = (
        [6.1707, -1.4313, 18.7915, 40.9942, -52.8836, -66.5549, 59.2405, -17.1408, 63.9711, 60.6304, -85.5885, -76.6842,
         -22.0429, -70.4604, -65.5839, -63.7202, -42.7979, -1.9149],
        [6.4855, 138.1282, -128.7887, -133.3007, -103.7741, -113.4921, 24.8351, 176.0781, -122.9314, 65.0157, -151.8833,
         -119.3297, 115.9045, 119.4519, 2.5201, -121.0386, 23.3631, -57.7485])
    received = coordinates(road_map)
    for lat_expected, lat_received, long_expected, long_received in zip(expected[0], received[0], expected[1],
                                                                        received[1]):
        assert lat_received == pytest.approx(lat_expected, abs=0.01)
        assert long_received == pytest.approx(long_expected, abs=0.01)


def test_coordinates_as_expected_2():
    road_map = [('N', 'E', -20.0695, 165.2267),
                ('B', 'F', 54.0981, 11.6462),
                ('Q', 'Z', -40.4051, 179.336),
                ('X', 'G', 77.9415, 173.0162),
                ('S', 'S', -28.6265, -62.7077),
                ('C', 'P', 10.5781, 2.8633),
                ('X', 'N', -81.6378, -56.6629),
                ('Z', 'D', 44.3644, -60.2304)]
    expected = ([-20.0695, 54.0981, -40.4051, 77.9415, -28.6265, 10.5781, -81.6378, 44.3644],
                [165.2267, 11.6462, 179.336, 173.0162, -62.7077, 2.8633, -56.6629, -60.2304])
    received = coordinates(road_map)

    for lat_expected, lat_received, long_expected, long_received in zip(expected[0], received[0], expected[1],
                                                                        received[1]):
        assert lat_received == pytest.approx(lat_expected, abs=0.01)
        assert long_received == pytest.approx(long_expected, abs=0.01)


def test_coordinate_ranges_as_expected_1():
    lats = [-41.485, 58.779, -68.5554, 85.7656, 20.7768, 5.9504]
    longs = [17.5276, 151.4407, 1.0818, -164.2764, -20.0873, -14.2232]
    expected = [-68.5554, 85.7656, -164.2764, 151.4407]
    received = coordinate_ranges(lats, longs)
    for extrema_expected, extrema_received in zip(expected, received):
        assert extrema_received == pytest.approx(extrema_expected, abs=0.01)


def test_coordinate_ranges_as_expected_2():
    lats = [-7.8059, 84.4342, 49.3749, 18.8722]
    longs = [115.7646, -40.435, 61.1988, -69.2588]
    expected = [-7.8059, 84.4342, -69.2588, 115.7646]
    received = coordinate_ranges(lats, longs)
    for extrema_expected, extrema_received in zip(expected, received):
        assert extrema_received == pytest.approx(extrema_expected, abs=0.01)


def test_coordinate_ranges_as_expected_3():
    lats = [-23.0642, 11.115, 55.5314, 51.5128, -30.6322, -60.7191, 28.4359, 79.8216]
    longs = [113.1924, -36.8924, -25.2197, 96.5879, 146.6252, 8.9988, 61.4995, -38.4625]
    expected = [-60.7191, 79.8216, -38.4625, 146.6252]
    received = coordinate_ranges(lats, longs)
    for extrema_expected, extrema_received in zip(expected, received):
        assert extrema_received == pytest.approx(extrema_expected, abs=0.01)


def test_coordinate_ranges_as_expected_4():
    lats = [41.1296]
    longs = [99.2094]
    expected = [41.1296, 41.1296, 99.2094, 99.2094]
    received = coordinate_ranges(lats, longs)
    for extrema_expected, extrema_received in zip(expected, received):
        assert extrema_received == pytest.approx(extrema_expected, abs=0.01)


def test_coordinate_ranges_as_expected_5():
    lats = [80.5122, -42.8356, -27.8176, 29.5528, -0.6372]
    longs = [-26.1421, 4.5991, -68.875, 69.1392, -1.682]
    expected = [-42.8356, 80.5122, -68.875, 69.1392]
    received = coordinate_ranges(lats, longs)
    for extrema_expected, extrema_received in zip(expected, received):
        assert extrema_received == pytest.approx(extrema_expected, abs=0.01)


def test_coordinates_to_points_returns_list_1():
    lats = [38.197274, 39.161921, 44.95]
    longs = [-84.86311, -75.526755, -93.094]
    lat_min, lat_max, long_min, long_max = 38.197274, 44.95, -93.094, -75.526755
    received = coordinates_to_points(lats, longs, lat_min, lat_max, long_min, long_max, 400, 400, 50, 50)
    assert isinstance(received, list)


def test_coordinates_to_points_returns_list_2():
    lats = [42.659829, 35.771, 48.813343, 39.962245, 35.482309, 44.931109, 40.269789, 41.82355]
    longs = [-73.781339, -78.638, -100.779004, -83.000647, -97.534994, -123.029159, -76.875613, -71.422132]
    lat_min, lat_max, long_min, long_max = (35.482309, 48.813343, -123.029159, -71.422132)
    received = coordinates_to_points(lats, longs, lat_min, lat_max, long_min, long_max, 400, 400, 50, 50)
    assert isinstance(received, list)


def test_coordinates_to_points_returns_collection_of_tuples_1():
    lats = [38.197274, 39.161921, 44.95]
    longs = [-84.86311, -75.526755, -93.094]
    lat_min, lat_max, long_min, long_max = 38.197274, 44.95, -93.094, -75.526755
    received = coordinates_to_points(lats, longs, lat_min, lat_max, long_min, long_max, 400, 400, 50, 50)
    for element in received:
        assert isinstance(element, tuple)


def test_coordinates_to_points_returns_collection_of_tuples_2():
    lats = [42.659829, 35.771, 48.813343, 39.962245, 35.482309, 44.931109, 40.269789, 41.82355]
    longs = [-73.781339, -78.638, -100.779004, -83.000647, -97.534994, -123.029159, -76.875613, -71.422132]
    lat_min, lat_max, long_min, long_max = (35.482309, 48.813343, -123.029159, -71.422132)
    received = coordinates_to_points(lats, longs, lat_min, lat_max, long_min, long_max, 400, 400, 50, 50)
    for element in received:
        assert isinstance(element, tuple)


def test_coordinates_to_points_returns_collection_of_collections_of_length_two_1():
    lats = [38.197274, 39.161921, 44.95]
    longs = [-84.86311, -75.526755, -93.094]
    lat_min, lat_max, long_min, long_max = 38.197274, 44.95, -93.094, -75.526755
    received = coordinates_to_points(lats, longs, lat_min, lat_max, long_min, long_max, 400, 400, 50, 50)
    for element in received:
        assert len(element) == 2


def test_coordinates_to_points_returns_collection_of_collections_of_length_two_2():
    lats = [42.659829, 35.771, 48.813343, 39.962245, 35.482309, 44.931109, 40.269789, 41.82355]
    longs = [-73.781339, -78.638, -100.779004, -83.000647, -97.534994, -123.029159, -76.875613, -71.422132]
    lat_min, lat_max, long_min, long_max = (35.482309, 48.813343, -123.029159, -71.422132)
    received = coordinates_to_points(lats, longs, lat_min, lat_max, long_min, long_max, 400, 400, 50, 50)
    for element in received:
        assert len(element) == 2


def test_coordinates_to_points_collection_right_length_1():
    lats = [38.197274, 39.161921, 44.95]
    longs = [-84.86311, -75.526755, -93.094]
    lat_min, lat_max, long_min, long_max = 38.197274, 44.95, -93.094, -75.526755
    expected = [(237.414, 450.0), (450.0, 392.858), (50.0, 50.0)]
    received = coordinates_to_points(lats, longs, lat_min, lat_max, long_min, long_max, 400, 400, 50, 50)
    assert len(expected) == len(received)


def test_coordinates_to_points_collection_right_length_2():
    lats = [42.659829, 35.771, 48.813343, 39.962245, 35.482309, 44.931109, 40.269789, 41.82355]
    longs = [-73.781339, -78.638, -100.779004, -83.000647, -97.534994, -123.029159, -76.875613, -71.422132]
    lat_min, lat_max, long_min, long_max = (35.482309, 48.813343, -123.029159, -71.422132)
    expected = [(431.71406386188454, 234.63726069560695),
                (394.0706553392428, 441.33777619950564),
                (222.45833595490788, 50.0),
                (360.25629126049057, 315.5787390535498),
                (247.60227613964284, 450.0),
                (50.0, 166.48710820180952),
                (407.7307098120572, 306.3508277002369),
                (449.99999999999994, 259.7299579312454)]
    received = coordinates_to_points(lats, longs, lat_min, lat_max, long_min, long_max, 400, 400, 50, 50)
    assert len(expected) == len(received)


def test_coordinates_to_points_as_expected_1():
    lats = [38.197274, 39.161921, 44.95]
    longs = [-84.86311, -75.526755, -93.094]
    lat_min, lat_max, long_min, long_max = 38.197274, 44.95, -93.094, -75.526755
    expected = [(237.414, 450.0), (450.0, 392.858), (50.0, 50.0)]
    received = coordinates_to_points(lats, longs, lat_min, lat_max, long_min, long_max, 400, 400, 50, 50)
    for i in range(3):
        assert received[i][0] == pytest.approx(expected[i][0], abs=0.01)
        assert received[i][1] == pytest.approx(expected[i][1], abs=0.01)


def test_coordinates_to_points_as_expected_2():
    lats = [42.659829, 35.771, 48.813343, 39.962245, 35.482309, 44.931109, 40.269789, 41.82355]
    longs = [-73.781339, -78.638, -100.779004, -83.000647, -97.534994, -123.029159, -76.875613, -71.422132]
    lat_min, lat_max, long_min, long_max = (35.482309, 48.813343, -123.029159, -71.422132)
    expected = [(431.71406386188454, 234.63726069560695),
                (394.0706553392428, 441.33777619950564),
                (222.45833595490788, 50.0),
                (360.25629126049057, 315.5787390535498),
                (247.60227613964284, 450.0),
                (50.0, 166.48710820180952),
                (407.7307098120572, 306.3508277002369),
                (449.99999999999994, 259.7299579312454)]
    received = coordinates_to_points(lats, longs, lat_min, lat_max, long_min, long_max, 400, 400, 50, 50)
    for i in range(8):
        assert received[i][0] == pytest.approx(expected[i][0], abs=0.01)
        assert received[i][1] == pytest.approx(expected[i][1], abs=0.01)


def test_coordinates_to_points_as_expected_3():
    lats = [32.361538, 58.301935, 33.448457]
    longs = [-86.279118, -134.41974, -112.073844]
    lat_min, lat_max, long_min, long_max = (32.361538, 58.301935, -134.41974, -86.279118)
    expected = [(450.0, 450.0), (50.0, 50.0), (235.67185110321176, 433.2397476414876)]
    received = coordinates_to_points(lats, longs, lat_min, lat_max, long_min, long_max, 400, 400, 50, 50)
    for i in range(3):
        assert received[i][0] == pytest.approx(expected[i][0], abs=0.01)
        assert received[i][1] == pytest.approx(expected[i][1], abs=0.01)


""" Test Case 1 """


@pytest.fixture
def road_map_1():
    return [('Minnesota', 'Saint Paul', 44.95, -93.094),
            ('Mississippi', 'Jackson', 32.32, -90.207),
            ('Missouri', 'Jefferson City', 38.572954, -92.189283),
            ('Montana', 'Helana', 46.595805, -112.027031),
            ('Nebraska', 'Lincoln', 40.809868, -96.675345),
            ('Nevada', 'Carson City', 39.160949, -119.753877),
            ('New Hampshire', 'Concord', 43.220093, -71.549127),
            ('New Jersey', 'Trenton', 40.221741, -74.756138),
            ('New Mexico', 'Santa Fe', 35.667231, -105.964575),
            ('New York', 'Albany', 42.659829, -73.781339),
            ('North Carolina', 'Raleigh', 35.771, -78.638),
            ('North Dakota', 'Bismarck', 48.813343, -100.779004)]


@pytest.fixture
def length_1():
    return 12


@pytest.fixture
def states_1():
    return ['Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
            'New Mexico', 'New York', 'North Carolina', 'North Dakota']


@pytest.fixture
def cities_1():
    return ['Saint Paul', 'Jackson', 'Jefferson City', 'Helana', 'Lincoln', 'Carson City', 'Concord', 'Trenton',
            'Santa Fe', 'Albany', 'Raleigh', 'Bismarck']


@pytest.fixture
def latitudes_1():
    return [44.95, 32.32, 38.572954, 46.595805, 40.809868, 39.160949, 43.220093, 40.221741, 35.667231, 42.659829,
            35.771, 48.813343]


@pytest.fixture
def longitudes_1():
    return [-93.094, -90.207, -92.189283, -112.027031, -96.675345, -119.753877, -71.549127, -74.756138, -105.964575,
            -73.781339, -78.638, -100.779004]


""" Test Case 2 """


@pytest.fixture
def road_map_2():
    return [('Delaware', 'Dover', 39.161921, -75.526755),
            ('Florida', 'Tallahassee', 30.4518, -84.27277),
            ('Georgia', 'Atlanta', 33.76, -84.39),
            ('Hawaii', 'Honolulu', 21.30895, -157.826182),
            ('Idaho', 'Boise', 43.613739, -116.237651),
            ('Illinois', 'Springfield', 39.78325, -89.650373),
            ('Indiana', 'Indianapolis', 39.790942, -86.147685)]


@pytest.fixture
def length_2():
    return 7


@pytest.fixture
def states_2():
    return ['Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana']


@pytest.fixture
def cities_2():
    return ['Dover', 'Tallahassee', 'Atlanta', 'Honolulu', 'Boise', 'Springfield', 'Indianapolis']


@pytest.fixture
def latitudes_2():
    return [39.161921, 30.4518, 33.76, 21.30895, 43.613739, 39.78325, 39.790942]


@pytest.fixture
def longitudes_2():
    return [-75.526755, -84.27277, -84.39, -157.826182, -116.237651, -89.650373, -86.147685]


""" Test Case 3 """


@pytest.fixture
def road_map_3():
    return [('Montana', 'Helana', 46.595805, -112.027031)]


@pytest.fixture
def length_3():
    return 1


@pytest.fixture
def states_3():
    return ['Montana']


@pytest.fixture
def cities_3():
    return ['Helana']


@pytest.fixture
def latitudes_3():
    return [46.595805]


@pytest.fixture
def longitudes_3():
    return [-112.027031]


""" Test Case 4 """


@pytest.fixture
def road_map_4():
    return [('Alabama', 'Montgomery', 32.361538, -86.279118),
            ('Alaska', 'Juneau', 58.301935, -134.41974),
            ('Arizona', 'Phoenix', 33.448457, -112.073844),
            ('Arkansas', 'Little Rock', 34.736009, -92.331122),
            ('California', 'Sacramento', 38.555605, -121.468926),
            ('Colorado', 'Denver', 39.7391667, -104.984167),
            ('Connecticut', 'Hartford', 41.767, -72.677),
            ('Delaware', 'Dover', 39.161921, -75.526755),
            ('Florida', 'Tallahassee', 30.4518, -84.27277),
            ('Georgia', 'Atlanta', 33.76, -84.39),
            ('Hawaii', 'Honolulu', 21.30895, -157.826182),
            ('Idaho', 'Boise', 43.613739, -116.237651)]


@pytest.fixture
def length_4():
    return 12


@pytest.fixture
def states_4():
    return ['Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
            'Hawaii', 'Idaho']


@pytest.fixture
def cities_4():
    return ['Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver', 'Hartford', 'Dover', 'Tallahassee', 'Atlanta',
            'Honolulu', 'Boise']


@pytest.fixture
def latitudes_4():
    return [58.301935, 33.448457, 34.736009, 38.555605, 39.7391667, 41.767, 39.161921, 30.4518, 33.76, 21.30895,
            43.613739]


@pytest.fixture
def longitudes_4():
    return [-134.41974, -112.073844, -92.331122, -121.468926, -104.984167, -72.677, -75.526755, -84.27277, -84.39,
            -157.826182, -116.237651]


# tests for itinerary.road_map()


def test_itinerary_road_map_is_list_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.road_map(), list)


def test_itinerary_road_map_is_list_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert isinstance(itinerary.road_map(), list)


def test_itinerary_road_map_is_collection_of_tuples_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    for element in itinerary.road_map():
        assert isinstance(element, tuple)


def test_itinerary_road_map_is_collection_of_tuples_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    for element in itinerary.road_map():
        assert isinstance(element, tuple)


def test_itinerary_road_map_has_right_length_1(road_map_1, length_1):
    itinerary = Itinerary(road_map_1)
    assert len(itinerary.road_map()) == length_1


def test_itinerary_road_map_has_right_length_2(road_map_2, length_2):
    itinerary = Itinerary(road_map_2)
    assert len(itinerary.road_map()) == length_2


def test_itinerary_road_map_is_collection_of_collections_of_length_four_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    for element in itinerary.road_map():
        assert len(element) == 4


def test_itinerary_road_map_is_collection_of_collections_of_length_four_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    for element in itinerary.road_map():
        assert len(element) == 4


def test_itinerary_road_map_is_input_list_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert itinerary.road_map() is road_map_1


def test_itinerary_road_map_is_input_list_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert itinerary.road_map() is road_map_2


def test_itinerary_road_map_all_values_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    for received, expected in zip(itinerary.road_map(), road_map_1):
        assert received[0] == expected[0]
        assert received[1] == expected[1]
        assert received[2] == pytest.approx(expected[2])
        assert received[3] == pytest.approx(expected[3])


def test_itinerary_road_map_all_values_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    for received, expected in zip(itinerary.road_map(), road_map_2):
        assert received[0] == expected[0]
        assert received[1] == expected[1]
        assert received[2] == pytest.approx(expected[2])
        assert received[3] == pytest.approx(expected[3])


# tests for itinerary.states()

def test_itinerary_states_is_generator_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.states(), types.GeneratorType)


def test_itinerary_states_is_generator_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert isinstance(itinerary.states(), types.GeneratorType)


def test_itinerary_states_elements_are_strings_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    for state in itinerary.states():
        assert isinstance(state, str)


def test_itinerary_states_elements_are_strings_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    for state in itinerary.states():
        assert isinstance(state, str)


def test_itinerary_states_expected_length_1(road_map_1, length_1):
    itinerary = Itinerary(road_map_1)
    assert len(list(itinerary.states())) == length_1


def test_itinerary_states_expected_length_2(road_map_2, length_2):
    itinerary = Itinerary(road_map_2)
    assert len(list(itinerary.states())) == length_2


def test_itinerary_states_expected_values_1(road_map_1, states_1):
    itinerary = Itinerary(road_map_1)
    for received, expected in zip(itinerary.states(), states_1):
        assert received == expected


def test_itinerary_states_expected_values_2(road_map_2, states_2):
    itinerary = Itinerary(road_map_2)
    for received, expected in zip(itinerary.states(), states_2):
        assert received == expected


# tests for itinerary.cities()

def test_itinerary_cities_is_generator_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.cities(), types.GeneratorType)


def test_itinerary_cities_is_generator_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert isinstance(itinerary.cities(), types.GeneratorType)


def test_itinerary_cities_elements_are_strings_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    for state in itinerary.cities():
        assert isinstance(state, str)


def test_itinerary_cities_elements_are_strings_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    for state in itinerary.cities():
        assert isinstance(state, str)


def test_itinerary_cities_expected_length_1(road_map_1, length_1):
    itinerary = Itinerary(road_map_1)
    assert len(list(itinerary.cities())) == length_1


def test_itinerary_cities_expected_length_2(road_map_2, length_2):
    itinerary = Itinerary(road_map_2)
    assert len(list(itinerary.cities())) == length_2


def test_itinerary_cities_expected_values_1(road_map_1, cities_1):
    itinerary = Itinerary(road_map_1)
    for received, expected in zip(itinerary.cities(), cities_1):
        assert received == expected


def test_itinerary_cities_expected_values_2(road_map_2, cities_2):
    itinerary = Itinerary(road_map_2)
    for received, expected in zip(itinerary.cities(), cities_2):
        assert received == expected


# tests for itinerary.latitudes()

def test_itinerary_latitudes_is_generator_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.latitudes(), types.GeneratorType)


def test_itinerary_latitudes_is_generator_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert isinstance(itinerary.latitudes(), types.GeneratorType)


def test_itinerary_latitudes_elements_are_floats_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    for state in itinerary.latitudes():
        assert isinstance(state, float)


def test_itinerary_latitudes_elements_are_floats_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    for state in itinerary.latitudes():
        assert isinstance(state, float)


def test_itinerary_latitudes_expected_length_1(road_map_1, length_1):
    itinerary = Itinerary(road_map_1)
    assert len(list(itinerary.latitudes())) == length_1


def test_itinerary_latitudes_expected_length_2(road_map_2, length_2):
    itinerary = Itinerary(road_map_2)
    assert len(list(itinerary.latitudes())) == length_2


def test_itinerary_latitudes_expected_values_1(road_map_1, latitudes_1):
    itinerary = Itinerary(road_map_1)
    for received, expected in zip(itinerary.latitudes(), latitudes_1):
        assert received == expected


def test_itinerary_latitudes_expected_values_2(road_map_2, latitudes_2):
    itinerary = Itinerary(road_map_2)
    for received, expected in zip(itinerary.latitudes(), latitudes_2):
        assert received == expected


# tests for itinerary.longitudes()

def test_itinerary_longitudes_is_generator_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.longitudes(), types.GeneratorType)


def test_itinerary_longitudes_is_generator_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert isinstance(itinerary.longitudes(), types.GeneratorType)


def test_itinerary_longitudes_elements_are_floats_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    for state in itinerary.longitudes():
        assert isinstance(state, float)


def test_itinerary_longitudes_elements_are_floats_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    for state in itinerary.longitudes():
        assert isinstance(state, float)


def test_itinerary_longitudes_expected_length_1(road_map_1, length_1):
    itinerary = Itinerary(road_map_1)
    assert len(list(itinerary.longitudes())) == length_1


def test_itinerary_longitudes_expected_length_2(road_map_2, length_2):
    itinerary = Itinerary(road_map_2)
    assert len(list(itinerary.longitudes())) == length_2


def test_itinerary_longitudes_expected_values_1(road_map_1, longitudes_1):
    itinerary = Itinerary(road_map_1)
    for received, expected in zip(itinerary.longitudes(), longitudes_1):
        assert received == expected


def test_itinerary_longitudes_expected_values_2(road_map_2, longitudes_2):
    itinerary = Itinerary(road_map_2)
    for received, expected in zip(itinerary.longitudes(), longitudes_2):
        assert received == expected


# tests for itinerary.length()

def test_itinerary_length_is_int_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.length(), int)


def test_itinerary_length_is_int_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert isinstance(itinerary.length(), int)


def test_itinerary_length_expected_value_1(road_map_1, length_1):
    itinerary = Itinerary(road_map_1)
    assert itinerary.length() == length_1


def test_itinerary_length_expected_value_2(road_map_2, length_2):
    itinerary = Itinerary(road_map_2)
    assert itinerary.length() == length_2


def test_itinerary_length_expected_value_3(road_map_3, length_3):
    itinerary = Itinerary(road_map_3)
    assert itinerary.length() == length_3


def test_itinerary_length_expected_value_4(road_map_4, length_4):
    itinerary = Itinerary(road_map_4)
    assert itinerary.length() == length_4


# tests for itinerary.latitude_max()

def test_itinerary_latitude_max_is_float_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.latitude_max(), float)


def test_itinerary_latitude_max_is_float_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert isinstance(itinerary.latitude_max(), float)


def test_itinerary_latitude_max_expected_value_1(road_map_1, latitudes_1):
    itinerary = Itinerary(road_map_1)
    assert itinerary.latitude_max() == pytest.approx(48.813343)


def test_itinerary_latitude_max_expected_value_2(road_map_2, latitudes_2):
    itinerary = Itinerary(road_map_2)
    assert itinerary.latitude_max() == pytest.approx(43.613739)


def test_itinerary_latitude_max_expected_value_3(road_map_3, latitudes_3):
    itinerary = Itinerary(road_map_3)
    assert itinerary.latitude_max() == pytest.approx(46.595805)


def test_itinerary_latitude_max_expected_value_4(road_map_4, latitudes_4):
    itinerary = Itinerary(road_map_4)
    assert itinerary.latitude_max() == pytest.approx(58.301935)


# tests for itinerary.latitude_min()

def test_itinerary_latitude_min_is_float_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.latitude_min(), float)


def test_itinerary_latitude_min_is_float_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert isinstance(itinerary.latitude_min(), float)


def test_itinerary_latitude_min_expected_value_1(road_map_1, latitudes_1):
    itinerary = Itinerary(road_map_1)
    assert itinerary.latitude_min() == pytest.approx(32.32)


def test_itinerary_latitude_min_expected_value_2(road_map_2, latitudes_2):
    itinerary = Itinerary(road_map_2)
    assert itinerary.latitude_min() == pytest.approx(21.30895)


def test_itinerary_latitude_min_expected_value_3(road_map_3, latitudes_3):
    itinerary = Itinerary(road_map_3)
    assert itinerary.latitude_min() == pytest.approx(46.595805)


def test_itinerary_latitude_min_expected_value_4(road_map_4, latitudes_4):
    itinerary = Itinerary(road_map_4)
    assert itinerary.latitude_min() == pytest.approx(21.30895)


# tests for itinerary.longitude_max()

def test_itinerary_longitude_max_is_float_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.longitude_max(), float)


def test_itinerary_longitude_max_is_float_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert isinstance(itinerary.longitude_max(), float)


def test_itinerary_longitude_max_expected_value_1(road_map_1, longitudes_1):
    itinerary = Itinerary(road_map_1)
    assert itinerary.longitude_max() == pytest.approx(-71.549127)


def test_itinerary_longitude_max_expected_value_2(road_map_2, longitudes_2):
    itinerary = Itinerary(road_map_2)
    assert itinerary.longitude_max() == pytest.approx(-75.526755)


def test_itinerary_longitude_max_expected_value_3(road_map_3, longitudes_3):
    itinerary = Itinerary(road_map_3)
    assert itinerary.longitude_max() == pytest.approx(-112.027031)


def test_itinerary_longitude_max_expected_value_4(road_map_4, longitudes_4):
    itinerary = Itinerary(road_map_4)
    assert itinerary.longitude_max() == pytest.approx(-72.677)


# tests for itinerary.longitude_min()

def test_itinerary_longitude_min_is_float_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.longitude_min(), float)


def test_itinerary_longitude_min_is_float_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert isinstance(itinerary.longitude_min(), float)


def test_itinerary_longitude_min_expected_value_1(road_map_1, longitudes_1):
    itinerary = Itinerary(road_map_1)
    assert itinerary.longitude_min() == pytest.approx(-119.753877)


def test_itinerary_longitude_min_expected_value_2(road_map_2, longitudes_2):
    itinerary = Itinerary(road_map_2)
    assert itinerary.longitude_min() == pytest.approx(-157.826182)


def test_itinerary_longitude_min_expected_value_3(road_map_3, longitudes_3):
    itinerary = Itinerary(road_map_3)
    assert itinerary.longitude_min() == pytest.approx(-112.027031)


def test_itinerary_longitude_min_expected_value_4(road_map_4, longitudes_4):
    itinerary = Itinerary(road_map_4)
    assert itinerary.longitude_min() == pytest.approx(-157.826182)




# tests for itinerary.latitude_gridline_spacing()


def test_itinerary_latitude_gridline_spacing_returns_float_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.latitude_gridline_spacing(), float)


def test_itinerary_latitude_gridline_spacing_returns_float_for_one_city(road_map_3):
    itinerary = Itinerary(road_map_3)
    assert isinstance(itinerary.latitude_gridline_spacing(), float)


def test_itinerary_latitude_gridline_spacing_expected_value_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert itinerary.latitude_gridline_spacing() == pytest.approx(2.0)


def test_itinerary_latitude_gridline_spacing_expected_value_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert itinerary.latitude_gridline_spacing() == pytest.approx(2.0)


def test_itinerary_latitude_gridline_spacing_expected_value_3(road_map_3):
    itinerary = Itinerary(road_map_3)
    assert itinerary.latitude_gridline_spacing() == pytest.approx(1.0)


def test_itinerary_latitude_gridline_spacing_expected_value_4(road_map_4):
    itinerary = Itinerary(road_map_4)
    assert itinerary.latitude_gridline_spacing() == pytest.approx(5.0)


# tests for itinerary.longitude_gridline_spacing()


def test_itinerary_longitude_gridline_spacing_returns_float_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.longitude_gridline_spacing(), float)


def test_itinerary_longitude_gridline_spacing_returns_float_for_one_city(road_map_3):
    itinerary = Itinerary(road_map_3)
    assert isinstance(itinerary.longitude_gridline_spacing(), float)


def test_itinerary_longitude_gridline_spacing_expected_value_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert itinerary.longitude_gridline_spacing() == pytest.approx(5.0)


def test_itinerary_longitude_gridline_spacing_expected_value_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert itinerary.longitude_gridline_spacing() == pytest.approx(10.0)


def test_itinerary_longitude_gridline_spacing_expected_value_3(road_map_3):
    itinerary = Itinerary(road_map_3)
    assert itinerary.longitude_gridline_spacing() == pytest.approx(1.0)


def test_itinerary_longitude_gridline_spacing_expected_value_4(road_map_4):
    itinerary = Itinerary(road_map_4)
    assert itinerary.longitude_gridline_spacing() == pytest.approx(10.0)

