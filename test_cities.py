import pytest
import random

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
    received = gridline_locations(-157.83, -69.77, 400, 50)
    assert len(received) == len(expected)
    for coord_expected, coord_received in zip(expected, received):
        assert coord_expected == pytest.approx(coord_received, abs=0.01)


def test_gridline_locations_as_expected_2():
    expected = [9.8, 10, 10.2, 10.4, 10.6, 10.8, 11, 11.2]
    received = gridline_locations(10, 11, 300, 100)
    assert len(received) == len(expected)
    for coord_expected, coord_received in zip(expected, received):
        assert coord_expected == pytest.approx(coord_received, abs=0.01)


def test_gridline_locations_as_expected_3():
    expected = [-40, -20, 0, 20, 40, 60, 80, 100]
    received = gridline_locations(-25, 85, 300, 50)
    assert len(received) == len(expected)
    for coord_expected, coord_received in zip(expected, received):
        assert coord_expected == pytest.approx(coord_received, abs=0.01)


def test_gridline_locations_as_expected_4():
    expected = [-56, -55, -54, -53, -52, -51, -50, -49]
    received = gridline_locations(-55, -50, 200, 50)
    assert len(received) == len(expected)
    for coord_expected, coord_received in zip(expected, received):
        assert coord_expected == pytest.approx(coord_received, abs=0.01)


def test_gridline_locations_as_expected_5():
    expected = [69.85, 69.855, 69.86, 69.865, 69.87, 69.875, 69.88]
    received = gridline_locations(69.85, 69.88, 800, 50)
    assert len(received) == len(expected)
    for coord_expected, coord_received in zip(expected, received):
        assert coord_expected == pytest.approx(coord_received, abs=0.01)


def test_canvas_coords_as_expected_1():
    road_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Delaware", "Dover", 39.161921, -75.526755),
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    expected = [(237.414, 450.0), (450.0, 392.858), (50.0, 50.0)]
    received = canvas_coords(road_map, 500, 500, 50, 50)
    for i in range(3):
        assert received[i][0] == pytest.approx(expected[i][0], abs=0.01)
        assert received[i][1] == pytest.approx(expected[i][1], abs=0.01)


def test_canvas_coords_as_expected_2():
    road_map = [('New York', 'Albany', 42.659829, -73.781339),
                ('North Carolina', 'Raleigh', 35.771, -78.638),
                ('North Dakota', 'Bismarck', 48.813343, -100.779004),
                ('Ohio', 'Columbus', 39.962245, -83.000647),
                ('Oklahoma', 'Oklahoma City', 35.482309, -97.534994),
                ('Oregon', 'Salem', 44.931109, -123.029159),
                ('Pennsylvania', 'Harrisburg', 40.269789, -76.875613),
                ('Rhode Island', 'Providence', 41.82355, -71.422132)]
    expected = [(431.71406386188454, 234.63726069560695),
                (394.0706553392428, 441.33777619950564),
                (222.45833595490788, 50.0),
                (360.25629126049057, 315.5787390535498),
                (247.60227613964284, 450.0),
                (50.0, 166.48710820180952),
                (407.7307098120572, 306.3508277002369),
                (449.99999999999994, 259.7299579312454)]
    received = canvas_coords(road_map, 500, 500, 50, 50)
    for i in range(8):
        assert received[i][0] == pytest.approx(expected[i][0], abs=0.01)
        assert received[i][1] == pytest.approx(expected[i][1], abs=0.01)


def test_canvas_coords_as_expected_3():
    road_map = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                ('Alaska', 'Juneau', 58.301935, -134.41974),
                ('Arizona', 'Phoenix', 33.448457, - 112.073844)]
    expected = [(450.0, 450.0), (50.0, 50.0), (235.67185110321176, 433.2397476414876)]
    received = canvas_coords(road_map, 500, 500, 50, 50)
    for i in range(3):
        assert received[i][0] == pytest.approx(expected[i][0], abs=0.01)
        assert received[i][1] == pytest.approx(expected[i][1], abs=0.01)


def test_canvas_coords_returns_list():
    road_map = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                ('Alaska', 'Juneau', 58.301935, -134.41974),
                ('Arizona', 'Phoenix', 33.448457, - 112.073844)]
    assert isinstance(canvas_coords(road_map, 500, 500, 50, 50), list)


def test_canvas_coords_returns_list_of_tuples():
    road_map = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                ('Alaska', 'Juneau', 58.301935, -134.41974),
                ('Arizona', 'Phoenix', 33.448457, - 112.073844)]
    for item in canvas_coords(road_map, 500, 500, 50, 50):
        assert isinstance(item, tuple)


def test_canvas_coords_returns_list_of_right_length():
    road_map = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                ('Alaska', 'Juneau', 58.301935, -134.41974),
                ('Arizona', 'Phoenix', 33.448457, - 112.073844)]
    assert len(canvas_coords(road_map, 500, 500, 50, 50)) == 3
