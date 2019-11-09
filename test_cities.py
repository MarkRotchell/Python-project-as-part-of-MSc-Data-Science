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
    assert compute_total_distance(road_map) == pytest.approx(37.0470)


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
    assert compute_total_distance(road_map) == pytest.approx(804.98)


def test_compute_total_distance_calculates_as_expected_equatorial_trip():
    road_map = [('No Where', 'No Where', 0.0, 180.0),
                ('No Where', 'No Where', 0.0, -180.0)]
    assert compute_total_distance(road_map) == pytest.approx(360)


def test_compute_total_distance_returns_float():
    road_map = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Delaware", "Dover", 39.161921, -75.526755),
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert isinstance(compute_total_distance(road_map), float)


# swap_cities tests
city1 = ("Kentucky", "Frankfort", 38.197274, -84.86311)
city2 = ("Delaware", "Dover", 39.161921, -75.526755)
city3 = ("Minnesota", "Saint Paul", 44.95, -93.094)
map_in = [city1, city2, city3]


def test_swap_cities_as_expected_1():
    map_out = swap_cities(map_in, 0, 2)[0]

    assert map_in[0] is map_out[2]
    assert map_in[2] is map_out[0]
    assert map_in[1] is map_out[1]


def test_swap_cities_as_expected_2():
    map_out = swap_cities(map_in, 2, 1)[0]

    assert map_in[2] is map_out[1]
    assert map_in[1] is map_out[2]
    assert map_in[0] is map_out[0]


def test_swap_cities_same_city():
    map_out = swap_cities(map_in, 1, 1)[0]

    assert map_in[0] is map_out[0]
    assert map_in[1] is map_out[1]
    assert map_in[2] is map_out[2]


def test_swap_cities_large_map():
    map_in_random = [('state', 'city', random.randint(-90, 90), random.randint(-180, 180)) for x in range(1000)]

    city_1, city_2 = random.randint(0, 999), random.randint(0, 999)

    map_out = swap_cities(map_in_random, city_1, city_2)

    for i in range(1000):
        if i == city_1:
            assert map_out[city_1] is map_in_random[city_2]
        elif i == city_2:
            assert map_out[city_2] is map_in_random[city_1]
        else:
            assert map_out[i] is map_in_random[i]


def test_swap_cities_returns_tuple():
    assert isinstance(swap_cities(map_in, 0, 0), tuple)


def test_swap_cities_returns_iterable_length_2():
    assert len(swap_cities(map_in, 0, 0)) == 2


def test_swap_cities_returns_list_and_float():
    map_out, distance = swap_cities(map_in, 1, 1)
    assert isinstance(map_out, list)
    assert isinstance(distance, float)


def test_swap_cities_returns_list_of_same_length_as_input():
    map_out = swap_cities(map_in, 1, 1)[0]
    assert len(map_out) == len(map_in)


def test_shift_cities():
    # add your tests
    assert 1 == 0
