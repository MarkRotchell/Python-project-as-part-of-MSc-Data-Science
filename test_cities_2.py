import pytest

from cities import *

''' read_cities '''


def test_read_cities_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_cities('gobblydigook.notatextfile')


def test_read_cities_EOF_Error_for_blank_file():
    with pytest.raises(EOFError):
        read_cities('no-cities.txt')


def test_read_cities_returns_list():
    assert isinstance(read_cities('city-data.txt'), list)


def test_read_cities_returns_collection_of_tuples():
    cities = read_cities('city-data.txt')
    for i in cities:
        assert isinstance(i, tuple)


def test_read_cities_returns_tuples_of_right_size():
    cities = read_cities('city-data.txt')
    for i in cities:
        assert len(i) == 4


def test_read_cities_returns_tuples_with_members_of_right_type():
    cities = read_cities('city-data.txt')
    for city in cities:
        for i in range(4):
            assert isinstance(city[0], str)
            assert isinstance(city[1], str)
            assert isinstance(city[2], float)
            assert isinstance(city[3], float)


def test_read_cities_returns_list_of_right_length():
    assert len(read_cities('city-data.txt')) == 50


def test_read_cities_as_expected_1():
    expected_map = [('London', 'Barking and Dagenham', 51.5607, 0.1557),
                    ('London', 'Barnet', 51.6252, -0.1517),
                    ('London', 'Bexley', 51.4549, 0.1505),
                    ('London', 'Brent', 51.5588, -0.2817),
                    ('London', 'Bromley', 51.4039, 0.0198),
                    ('London', 'Camden', 51.529, -0.1255),
                    ('London', 'City of London', 51.5155, -0.0922),
                    ('London', 'Croydon', 51.3714, -0.0977),
                    ('London', 'Ealing', 51.513, -0.3089),
                    ('London', 'Enfield', 51.6538, -0.0799),
                    ('London', 'Greenwich', 51.4892, 0.0648),
                    ('London', 'Hackney', 51.545, -0.0553),
                    ('London', 'Hammersmith and Fulham', 51.4927, -0.2339),
                    ('London', 'Haringey', 51.6, -0.1119),
                    ('London', 'Harrow', 51.5898, -0.3346),
                    ('London', 'Havering', 51.5812, 0.1837),
                    ('London', 'Hillingdon', 51.5441, -0.476),
                    ('London', 'Hounslow', 51.4746, -0.368),
                    ('London', 'Islington', 51.5416, -0.1022),
                    ('London', 'Kensington and Chelsea', 51.502, -0.1947),
                    ('London', 'Kingston upon Thames', 51.4085, -0.3064),
                    ('London', 'Lambeth', 51.4607, -0.1163),
                    ('London', 'Lewisham', 51.4452, -0.0209),
                    ('London', 'Merton', 51.4014, -0.1958),
                    ('London', 'Newham', 51.5077, 0.0469),
                    ('London', 'Redbridge', 51.559, 0.0741),
                    ('London', 'Richmond upon Thames', 51.4479, -0.326),
                    ('London', 'Southwark', 51.5035, -0.0804),
                    ('London', 'Sutton', 51.3618, -0.1945),
                    ('London', 'Tower Hamlets', 51.5099, -0.0059),
                    ('London', 'Waltham Forest', 51.5908, -0.0134),
                    ('London', 'Wandsworth', 51.4567, -0.191),
                    ('London', 'Westminster', 51.4973, -0.1372)]
    received_map = read_cities('london-boroughs.txt')
    for received, expected in zip(received_map, expected_map):
        assert received[0] == expected[0]
        assert received[1] == expected[1]
        assert received[2] == pytest.approx(expected[2], abs=0.0001)
        assert received[3] == pytest.approx(expected[3], abs=0.0001)


def test_read_cities_as_expected_2():
    expected_map = [('Alabama', 'Montgomery', 32.361538, -86.279118),
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
                    ('Idaho', 'Boise', 43.613739, -116.237651),
                    ('Illinois', 'Springfield', 39.78325, -89.650373),
                    ('Indiana', 'Indianapolis', 39.790942, -86.147685),
                    ('Iowa', 'Des Moines', 41.590939, -93.620866),
                    ('Kansas', 'Topeka', 39.04, -95.69),
                    ('Kentucky', 'Frankfort', 38.197274, -84.86311),
                    ('Louisiana', 'Baton Rouge', 30.45809, -91.140229),
                    ('Maine', 'Augusta', 44.323535, -69.765261),
                    ('Maryland', 'Annapolis', 38.972945, -76.501157),
                    ('Massachusetts', 'Boston', 42.2352, -71.0275),
                    ('Michigan', 'Lansing', 42.7335, -84.5467),
                    ('Minnesota', 'Saint Paul', 44.95, -93.094),
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
                    ('North Dakota', 'Bismarck', 48.813343, -100.779004),
                    ('Ohio', 'Columbus', 39.962245, -83.000647),
                    ('Oklahoma', 'Oklahoma City', 35.482309, -97.534994),
                    ('Oregon', 'Salem', 44.931109, -123.029159),
                    ('Pennsylvania', 'Harrisburg', 40.269789, -76.875613),
                    ('Rhode Island', 'Providence', 41.82355, -71.422132),
                    ('South Carolina', 'Columbia', 34, -81.035),
                    ('South Dakota', 'Pierre', 44.367966, -100.336378),
                    ('Tennessee', 'Nashville', 36.165, -86.784),
                    ('Texas', 'Austin', 30.266667, -97.75),
                    ('Utah', 'Salt Lake City', 40.7547, -111.892622),
                    ('Vermont', 'Montpelier', 44.26639, -72.57194),
                    ('Virginia', 'Richmond', 37.54, -77.46),
                    ('Washington', 'Olympia', 47.042418, -122.893077),
                    ('West Virginia', 'Charleston', 38.349497, -81.633294),
                    ('Wisconsin', 'Madison', 43.074722, -89.384444),
                    ('Wyoming', 'Cheyenne', 41.145548, -104.802042)]
    received_map = read_cities('city-data.txt')
    for received, expected in zip(received_map, expected_map):
        assert received[0] == expected[0]
        assert received[1] == expected[1]
        assert received[2] == pytest.approx(expected[2], abs=0.0001)
        assert received[3] == pytest.approx(expected[3], abs=0.0001)
