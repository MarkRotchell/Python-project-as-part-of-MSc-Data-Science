import pytest
from cities import *


#read_cities tests
def test_read_cities_requires_string():
    with pytest.raises(TypeError):
        read_cities(1)

def test_read_cities_requires_wont_take_list():
    with pytest.raises(TypeError):
        read_cities(['hello world'])

def test_read_cities_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_cities('gobblydigook.notatextfile')

def test_read_cities_returns_list():
    assert type(read_cities('test-city-data.txt')) == type([])

def test_read_cities_returns_list_of_tuples():
    cities = read_cities('test-city-data.txt')
    for i in cities:
        assert type(i) is tuple

def test_read_cities_returns_tuples_of_right_size():
    cities = read_cities('test-city-data.txt')
    for i in cities:
        assert len(i) == 4

def test_read_cities_returns_tuples_with_members_of_right_type():
    cities = read_cities('test-city-data.txt')
    for i in cities:
        assert type(i[0]) is str
        assert type(i[1]) is str
        assert type(i[2]) is float
        assert type(i[3]) is float

def test_read_cities_returns_list_of_right_length():
    assert len(read_cities('test-city-data.txt')) == 3


def test_read_cities_test_data():
    expected_data = [('Alabama', 'Montgomery', 32.361538, -86.279118), \
                     ('Alaska', 'Juneau', 58.301935, -134.41974), \
                     ('Arizona', 'Phoenix', 33.448457, - 112.073844)]
    actual_data = read_cities('test-city-data.txt')
    for i in range(3):
        assert actual_data[i][0] == expected_data[i][0]
        assert actual_data[i][1] == expected_data[i][1]
        assert actual_data[i][2] == pytest.approx(expected_data[i][2])
        assert actual_data[i][3] == pytest.approx(expected_data[i][3])

#TODO: test for situation that file with bad data is passed
#      test for situation that coodirnates aren't valid lat / long
#      test for repeated cities
#      test for multiple cities at the same coordinates
#      test for multiple coords for same city name


'''
#compute_total_distance tests
def test_compute_total_distance_calculates_as_expected():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1)== pytest.approx(9.386+18.496+10.646, 0.01)

def test_compute_total_distance_returns_float():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert type(compute_total_distance(road_map1)) == type(0.0)

def test_compute_total_distance_checks_type():
    with pytest.raises(TypeError):
        compute_total_distance(1)

    #assert 1 == 2
    #add your further tests

def test_swap_cities():
    #add your tests
    assert 1==0

def test_shift_cities():
    #add your tests
    assert 1==0
'''
