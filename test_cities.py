import pytest
import types
import collections.abc

from cities import *


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


@pytest.fixture
def road_map_2():
    return [('Mauritania', 'Nouakchott', -20.1, 57.3),
            ('Mayotte', 'Mamoudzou', -12.48, 45.14),
            ('Mexico', 'Mexico', 19.2, -99.1),
            ('Micronesia (Federated States of)', 'Palikir', 6.55, 158.0),
            ('Moldova, Republic of', 'Chisinau', 47.02, 28.5),
            ('Mozambique', 'Maputo', -25.58, 32.32),
            ('Myanmar', 'Yangon', 16.45, 96.2),
            ('Namibia', 'Windhoek', -22.35, 17.04),
            ('Nepal', 'Kathmandu', 27.45, 85.2),
            ('Netherlands', 'Amsterdam', 52.23, 4.54),
            ('Netherlands Antilles', 'Willemstad', 12.05, -69.0),
            ('New Caledonia', 'Noumea', -22.17, 166.3),
            ('New Zealand', 'Wellington', -41.19, 174.4),
            ('Nicaragua', 'Managua', 12.06, -86.2),
            ('Niger', 'Niamey', 13.27, 2.06),
            ('Nigeria', 'Abuja', 9.05, 7.32)]


@pytest.fixture
def length_2():
    return 16


@pytest.fixture
def states_2():
    return ['Mauritania', 'Mayotte', 'Mexico', 'Micronesia (Federated States of)', 'Moldova, Republic of', 'Mozambique',
            'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand',
            'Nicaragua', 'Niger', 'Nigeria']


@pytest.fixture
def cities_2():
    return ['Nouakchott', 'Mamoudzou', 'Mexico', 'Palikir', 'Chisinau', 'Maputo', 'Yangon', 'Windhoek', 'Kathmandu',
            'Amsterdam', 'Willemstad', 'Noumea', 'Wellington', 'Managua', 'Niamey', 'Abuja']


@pytest.fixture
def latitudes_2():
    return [-20.1, -12.48, 19.2, 6.55, 47.02, -25.58, 16.45, -22.35, 27.45, 52.23, 12.05, -22.17, -41.19, 12.06, 13.27,
            9.05]


@pytest.fixture
def longitudes_2():
    return [57.3, 45.14, -99.1, 158.0, 28.5, 32.32, 96.2, 17.04, 85.2, 4.54, -69.0, 166.3, 174.4, -86.2, 2.06, 7.32]


@pytest.fixture
def road_map_3():
    return [('London', 'Hackney', 51.545, -0.0553),
            ('London', 'Hammersmith and Fulham', 51.4927, -0.2339),
            ('London', 'Haringey', 51.6, -0.1119),
            ('London', 'Harrow', 51.5898, -0.3346),
            ('London', 'Havering', 51.5812, 0.1837),
            ('London', 'Hillingdon', 51.5441, -0.476)]


@pytest.fixture
def length_3():
    return 6


@pytest.fixture
def states_3():
    return ['London', 'London', 'London', 'London', 'London', 'London']


@pytest.fixture
def cities_3():
    return ['Hackney', 'Hammersmith and Fulham', 'Haringey', 'Harrow', 'Havering', 'Hillingdon']


@pytest.fixture
def latitudes_3():
    return [51.545, 51.4927, 51.6, 51.5898, 51.5812, 51.5441]


@pytest.fixture
def longitudes_3():
    return [-0.0553, -0.2339, -0.1119, -0.3346, 0.1837, -0.476]


@pytest.fixture
def road_map_4():
    return [('England', 'Wells', 51.209, -2.647),
            ('England', 'Westminster', 51.515457, -0.09214),
            ('England', 'Winchester', 51.063202, -1.308),
            ('England', 'Wolverhampton', 52.59137, -2.110748),
            ('England', 'Worcester', 52.192001, -2.22),
            ('England', 'York', 53.958332, -1.080278),
            ('Scotland', 'Aberdeen', 57.149651, -2.099075),
            ('Scotland', 'Dundee', 56.462002, -2.9707),
            ('Scotland', 'Edinburgh', 55.953251, -3.188267),
            ('Scotland', 'Glasgow', 55.860916, -4.251433),
            ('Scotland', 'Inverness', 57.477772, -4.224721),
            ('Scotland', 'Perth', 56.396999, -3.437),
            ('Scotland', 'Stirling', 56.1166, -3.9369),
            ('Wales', 'Bangor', 53.228, -4.128),
            ('Wales', 'Cardiff', 51.481583, -3.17909),
            ('Wales', 'Newport', 51.58333, -2.98333),
            ('Wales', 'St. Asaph', 53.2667, -3.45),
            ('Wales', 'St. Davids', 51.882, -5.269),
            ('Wales', 'Swansea', 51.621441, -3.943646),
            ('Northern Ireland', 'Armagh', 54.35, -6.6667),
            ('Northern Ireland', 'Belfast', 54.607868, -5.926437),
            ('Northern Ireland', 'Lisburn', 54.5234, -6.03527),
            ('Northern Ireland', 'Newry', 54.175999, -6.349),
            ('Northern Ireland', 'Derry', 54.9958, -7.3074)]


@pytest.fixture
def length_4():
    return 24


@pytest.fixture
def states_4():
    return ['England', 'England', 'England', 'England', 'England', 'England', 'Scotland', 'Scotland', 'Scotland',
            'Scotland', 'Scotland', 'Scotland', 'Scotland', 'Wales', 'Wales', 'Wales', 'Wales', 'Wales', 'Wales',
            'Northern Ireland', 'Northern Ireland', 'Northern Ireland', 'Northern Ireland', 'Northern Ireland']


@pytest.fixture
def cities_4():
    return ['Wells', 'Westminster', 'Winchester', 'Wolverhampton', 'Worcester', 'York', 'Aberdeen', 'Dundee',
            'Edinburgh', 'Glasgow', 'Inverness', 'Perth', 'Stirling', 'Bangor', 'Cardiff', 'Newport', 'St. Asaph',
            'St. Davids', 'Swansea', 'Armagh', 'Belfast', 'Lisburn', 'Newry', 'Derry']


@pytest.fixture
def latitudes_4():
    return [51.209, 51.515457, 51.063202, 52.59137, 52.192001, 53.958332, 57.149651, 56.462002, 55.953251, 55.860916,
            57.477772, 56.396999, 56.1166, 53.228, 51.481583, 51.58333, 53.2667, 51.882, 51.621441, 54.35, 54.607868,
            54.5234, 54.175999, 54.9958]


@pytest.fixture
def longitudes_4():
    return [-2.647, -0.09214, -1.308, -2.110748, -2.22, -1.080278, -2.099075, -2.9707, -3.188267, -4.251433, -4.224721,
            -3.437, -3.9369, -4.128, -3.17909, -2.98333, -3.45, -5.269, -3.943646, -6.6667, -5.926437, -6.03527, -6.349,
            -7.3074]


@pytest.fixture
def road_map_5():
    return [('Paradise', 'Birkbeck', 51.521728, -0.129338)]


@pytest.fixture
def length_5():
    return 1


@pytest.fixture
def states_5():
    return ['Paradise']


@pytest.fixture
def cities_5():
    return ['Birkbeck']


@pytest.fixture
def latitudes_5():
    return [51.521728]


@pytest.fixture
def longitudes_5():
    return [-0.129338]


'''
##################################

read_cities                           

################################## 
'''


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


'''
################################## 

cities_as_string                       

################################## 
'''


def test_cities_as_string_returns_string_1(road_map_1):
    assert isinstance(cities_as_string(road_map_1), str)


def test_cities_as_string_as_expected_1(road_map_1):
    assert cities_as_string(road_map_1) == '''     State                City                  Latitude  Longitude
1    Minnesota            Saint Paul               44.95     -93.09
2    Mississippi          Jackson                  32.32     -90.21
3    Missouri             Jefferson City           38.57     -92.19
4    Montana              Helana                   46.60    -112.03
5    Nebraska             Lincoln                  40.81     -96.68
6    Nevada               Carson City              39.16    -119.75
7    New Hampshire        Concord                  43.22     -71.55
8    New Jersey           Trenton                  40.22     -74.76
9    New Mexico           Santa Fe                 35.67    -105.96
10   New York             Albany                   42.66     -73.78
11   North Carolina       Raleigh                  35.77     -78.64
12   North Dakota         Bismarck                 48.81    -100.78
'''


def test_cities_as_string_as_expected_2(road_map_2):
    assert cities_as_string(road_map_2) == '''     State                City                  Latitude  Longitude
1    Mauritania           Nouakchott              -20.10      57.30
2    Mayotte              Mamoudzou               -12.48      45.14
3    Mexico               Mexico                   19.20     -99.10
4    Micronesia (Federate Palikir                   6.55     158.00
5    Moldova, Republic of Chisinau                 47.02      28.50
6    Mozambique           Maputo                  -25.58      32.32
7    Myanmar              Yangon                   16.45      96.20
8    Namibia              Windhoek                -22.35      17.04
9    Nepal                Kathmandu                27.45      85.20
10   Netherlands          Amsterdam                52.23       4.54
11   Netherlands Antilles Willemstad               12.05     -69.00
12   New Caledonia        Noumea                  -22.17     166.30
13   New Zealand          Wellington              -41.19     174.40
14   Nicaragua            Managua                  12.06     -86.20
15   Niger                Niamey                   13.27       2.06
16   Nigeria              Abuja                     9.05       7.32
'''


def test_cities_as_string_as_expected_3(road_map_3):
    assert cities_as_string(road_map_3) == '''     State                City                  Latitude  Longitude
1    London               Hackney                  51.55      -0.06
2    London               Hammersmith and Fulh     51.49      -0.23
3    London               Haringey                 51.60      -0.11
4    London               Harrow                   51.59      -0.33
5    London               Havering                 51.58       0.18
6    London               Hillingdon               51.54      -0.48
'''


def test_cities_as_string_as_expected_4(road_map_4):
    assert cities_as_string(road_map_4) == '''     State                City                  Latitude  Longitude
1    England              Wells                    51.21      -2.65
2    England              Westminster              51.52      -0.09
3    England              Winchester               51.06      -1.31
4    England              Wolverhampton            52.59      -2.11
5    England              Worcester                52.19      -2.22
6    England              York                     53.96      -1.08
7    Scotland             Aberdeen                 57.15      -2.10
8    Scotland             Dundee                   56.46      -2.97
9    Scotland             Edinburgh                55.95      -3.19
10   Scotland             Glasgow                  55.86      -4.25
11   Scotland             Inverness                57.48      -4.22
12   Scotland             Perth                    56.40      -3.44
13   Scotland             Stirling                 56.12      -3.94
14   Wales                Bangor                   53.23      -4.13
15   Wales                Cardiff                  51.48      -3.18
16   Wales                Newport                  51.58      -2.98
17   Wales                St. Asaph                53.27      -3.45
18   Wales                St. Davids               51.88      -5.27
19   Wales                Swansea                  51.62      -3.94
20   Northern Ireland     Armagh                   54.35      -6.67
21   Northern Ireland     Belfast                  54.61      -5.93
22   Northern Ireland     Lisburn                  54.52      -6.04
23   Northern Ireland     Newry                    54.18      -6.35
24   Northern Ireland     Derry                    55.00      -7.31
'''


def test_cities_as_string_as_expected_5(road_map_5):
    assert cities_as_string(road_map_5) == '''     State                City                  Latitude  Longitude
1    Paradise             Birkbeck                 51.52      -0.13
'''


'''
################################## 

distance                           

################################## 
'''


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


def test_distance_zero_for_same_city():
    city1 = ('Michigan', 'Lansing', 42.7335, -84.5467)
    city2 = ('Michigan', 'Lansing', 42.7335, -84.5467)
    assert distance(city1, city2) == pytest.approx(0)


def test_distance_returns_float_1():
    city1 = ('Rhode Island', 'Providence', 41.82355, -71.422132)
    city2 = ('South Carolina', 'Columbia', 34.0, -81.035)
    assert isinstance(distance(city1, city2), float)


def test_distance_returns_float_2():
    city1 = ('Delaware', 'Dover', 39.161921, -75.526755)
    city2 = ('Florida', 'Tallahassee', 30.4518, -84.27277)
    assert isinstance(distance(city1, city2), float)


'''
################################## 

map_as_string                           

################################## 
'''


def test_map_as_string_returns_string(road_map_1):
    assert isinstance(map_as_string(road_map_1), str)


def test_map_as_string_as_expected_1(road_map_1):
    assert map_as_string(road_map_1) == '''Estimated optimal cycle:

          Saint Paul --> Jackson                  12.96
             Jackson --> Jefferson City            6.56
      Jefferson City --> Helana                   21.40
              Helana --> Lincoln                  16.41
             Lincoln --> Carson City              23.14
         Carson City --> Concord                  48.38
             Concord --> Trenton                   4.39
             Trenton --> Santa Fe                 31.54
            Santa Fe --> Albany                   32.93
              Albany --> Raleigh                   8.43
             Raleigh --> Bismarck                 25.70
            Bismarck --> Saint Paul                8.60
                                           -------------
                              Total Distance     240.42
'''


def test_map_as_string_as_expected_2(road_map_2):
    assert map_as_string(road_map_2) == '''Estimated optimal cycle:

          Nouakchott --> Mamoudzou                14.35
           Mamoudzou --> Mexico                  147.68
              Mexico --> Palikir                 257.41
             Palikir --> Chisinau                135.68
            Chisinau --> Maputo                   72.70
              Maputo --> Yangon                   76.47
              Yangon --> Windhoek                 88.16
            Windhoek --> Kathmandu                84.41
           Kathmandu --> Amsterdam                84.38
           Amsterdam --> Willemstad               83.80
          Willemstad --> Noumea                  237.78
              Noumea --> Wellington               20.67
          Wellington --> Managua                 265.98
             Managua --> Niamey                   88.27
              Niamey --> Abuja                     6.74
               Abuja --> Nouakchott               57.86
                                           -------------
                              Total Distance    1722.34
'''


def test_map_as_string_as_expected_3(road_map_3):
    assert map_as_string(road_map_3) == '''Estimated optimal cycle:

             Hackney --> Hammersmith and Fulh      0.19
Hammersmith and Fulh --> Haringey                  0.16
            Haringey --> Harrow                    0.22
              Harrow --> Havering                  0.52
            Havering --> Hillingdon                0.66
          Hillingdon --> Hackney                   0.42
                                           -------------
                              Total Distance       2.17
'''


def test_map_as_string_as_expected_4(road_map_4):
    assert map_as_string(road_map_4) == '''Estimated optimal cycle:

               Wells --> Westminster               2.57
         Westminster --> Winchester                1.30
          Winchester --> Wolverhampton             1.73
       Wolverhampton --> Worcester                 0.41
           Worcester --> York                      2.10
                York --> Aberdeen                  3.35
            Aberdeen --> Dundee                    1.11
              Dundee --> Edinburgh                 0.55
           Edinburgh --> Glasgow                   1.07
             Glasgow --> Inverness                 1.62
           Inverness --> Perth                     1.34
               Perth --> Stirling                  0.57
            Stirling --> Bangor                    2.89
              Bangor --> Cardiff                   1.99
             Cardiff --> Newport                   0.22
             Newport --> St. Asaph                 1.75
           St. Asaph --> St. Davids                2.29
          St. Davids --> Swansea                   1.35
             Swansea --> Armagh                    3.85
              Armagh --> Belfast                   0.78
             Belfast --> Lisburn                   0.14
             Lisburn --> Newry                     0.47
               Newry --> Derry                     1.26
               Derry --> Wells                     6.00
                                           -------------
                              Total Distance      40.72
'''


def test_map_as_string_as_expected_5(road_map_5):
    assert map_as_string(road_map_5) == '''Estimated optimal cycle:

            Birkbeck --> Birkbeck                  0.00
                                           -------------
                              Total Distance       0.00
'''


'''
################################## 

pairwise_circuit                           

################################## 
'''


def test_pairwise_circuit_returns_iterator():
    iterable = [1, 2, 3, 4]
    assert isinstance(pairwise_circuit(iterable), collections.abc.Iterator)


def test_pairwise_circuit_yields_tuples():
    iterable = [1, 2, 3, 4]
    for element in pairwise_circuit(iterable):
        assert isinstance(element, tuple)


def test_pairwise_circuit_yields_pairs():
    iterable = [1, 2, 3, 4]
    for element in pairwise_circuit(iterable):
        assert len(element) == 2


def test_pairwise_circuit_yields_pairs_of_same_type_as_input():
    iterable = [1, 2, 3, 4]
    for element in pairwise_circuit(iterable):
        assert isinstance(element[0], int)
        assert isinstance(element[1], int)


def test_pairwise_circuit_returns_right_length():
    iterable = [1, 2, 3, 4]
    assert len(list(pairwise_circuit(iterable))) == 4


def test_pairwise_circuit_returns_right_length_single_element():
    iterable = [1]
    assert len(list(pairwise_circuit(iterable))) == 1


def test_pairwise_circuit_returns_as_expected_1():
    iterable = [1, 2, 3, 4]
    expected = [(1, 2), (2, 3), (3, 4), (4, 1)]
    received = pairwise_circuit(iterable)
    for (exp_0, exp_1), (rec_0, rec_1) in zip(expected, received):
        assert rec_0 == pytest.approx(exp_0)
        assert rec_1 == pytest.approx(exp_1)


def test_pairwise_circuit_returns_as_expected_with_road_map(road_map_3):
    expected = [(('London', 'Hackney', 51.545, -0.0553), ('London', 'Hammersmith and Fulham', 51.4927, -0.2339)),
                (('London', 'Hammersmith and Fulham', 51.4927, -0.2339), ('London', 'Haringey', 51.6, -0.1119)),
                (('London', 'Haringey', 51.6, -0.1119), ('London', 'Harrow', 51.5898, -0.3346)),
                (('London', 'Harrow', 51.5898, -0.3346), ('London', 'Havering', 51.5812, 0.1837)),
                (('London', 'Havering', 51.5812, 0.1837), ('London', 'Hillingdon', 51.5441, -0.476)),
                (('London', 'Hillingdon', 51.5441, -0.476), ('London', 'Hackney', 51.545, -0.0553))]
    received = pairwise_circuit(road_map_3)
    for (exp_0, exp_1), (rec_0, rec_1) in zip(expected, received):
        assert exp_0[0] == rec_0[0]
        assert exp_1[0] == rec_1[0]
        assert exp_0[1] == rec_0[1]
        assert exp_1[1] == rec_1[1]
        assert exp_0[2] == pytest.approx(rec_0[2])
        assert exp_1[2] == pytest.approx(rec_1[2])
        assert exp_0[3] == pytest.approx(rec_0[3])
        assert exp_1[3] == pytest.approx(rec_1[3])


'''
################################## 

compute_total_distance                           

################################## 
'''


def test_compute_total_distance_single_city():
    road_map = [('Michigan', 'Lansing', 42.7335, -84.5467)]
    assert compute_total_distance(road_map) == pytest.approx(0)


def test_compute_total_distance_repeated_city():
    road_map = [('Michigan', 'Lansing', 42.7335, -84.5467),
                ('Michigan', 'Lansing', 42.7335, -84.5467)]
    assert compute_total_distance(road_map) == pytest.approx(0)


def test_compute_total_distance_calculates_as_expected_1(road_map_1):
    assert compute_total_distance(road_map_1) == pytest.approx(240.4230)


def test_compute_total_distance_calculates_as_expected_2(road_map_2):
    assert compute_total_distance(road_map_2) == pytest.approx(1722.34080)


def test_compute_total_distance_calculates_as_expected_3(road_map_3):
    assert compute_total_distance(road_map_3) == pytest.approx(2.17132)


def test_compute_total_distance_calculates_as_expected_4(road_map_4):
    assert compute_total_distance(road_map_4) == pytest.approx(40.718597)


def test_compute_total_distance_calculates_as_expected_pole_to_pole():
    road_map = [('The Arctic', 'North Pole', 90, -180),
                ('The Antarctic', 'South Pole', -90, 180)]
    assert compute_total_distance(road_map) == pytest.approx(804.984471899)


def test_compute_total_distance_calculates_as_expected_equatorial_trip():
    road_map = [('No Where', 'No Where', 0.0, 180.0),
                ('No Where', 'No Where', 0.0, -180.0)]
    assert compute_total_distance(road_map) == pytest.approx(720)


def test_compute_total_distance_returns_float(road_map_1):
    assert isinstance(compute_total_distance(road_map_1), float)


'''
################################## 

swap_cities                           

################################## 
'''


def test_swap_cities_returns_tuple(road_map_1):
    assert isinstance(swap_cities(road_map_1, 1, 4), tuple)


def test_swap_cities_returns_two_tuple(road_map_1):
    assert len(swap_cities(road_map_1, 2, 6)) == 2


def test_swap_cities_returns_list_as_first_element(road_map_1):
    result = swap_cities(road_map_1, 4, 1)
    assert isinstance(result[0], list)
    assert isinstance(result[1], float)


def test_swap_cities_returns_collection_of_tuples_as_first_element(road_map_1):
    result = swap_cities(road_map_1, 4, 1)
    for element in result[0]:
        assert isinstance(element, tuple)


def test_swap_cities_returns_float_as_second_element(road_map_1):
    result = swap_cities(road_map_1, 2, 3)
    assert isinstance(result[1], float)


def test_swap_cities_in_place(road_map_1):
    assert swap_cities(road_map_1, 0, 3)[0] is road_map_1


def test_swap_cities_same_index(road_map_1):
    for city_in, city_out in zip(road_map_1, swap_cities(road_map_1[:], 4, 4)[0]):
        assert city_in is city_out


def test_swap_cities_right_length_1(road_map_1, length_1):
    assert len(swap_cities(road_map_1, 0, 2)[0]) == length_1


def test_swap_cities_right_length_2(road_map_2, length_2):
    assert len(swap_cities(road_map_2, 0, 2)[0]) == length_2


def test_swap_cities_right_length_single_city(road_map_5):
    assert len(swap_cities(road_map_5, 0, 0)[0]) == 1


def test_swap_cities_swaps_correct_cities_1(road_map_1):
    expected_map = [('Minnesota', 'Saint Paul', 44.95, -93.094),
                    ('North Carolina', 'Raleigh', 35.771, -78.638),
                    ('Missouri', 'Jefferson City', 38.572954, -92.189283),
                    ('Montana', 'Helana', 46.595805, -112.027031),
                    ('Nebraska', 'Lincoln', 40.809868, -96.675345),
                    ('Nevada', 'Carson City', 39.160949, -119.753877),
                    ('New Hampshire', 'Concord', 43.220093, -71.549127),
                    ('New Jersey', 'Trenton', 40.221741, -74.756138),
                    ('New Mexico', 'Santa Fe', 35.667231, -105.964575),
                    ('New York', 'Albany', 42.659829, -73.781339),
                    ('Mississippi', 'Jackson', 32.32, -90.207),
                    ('North Dakota', 'Bismarck', 48.813343, -100.779004)]
    for received, expected in zip(swap_cities(road_map_1, 1, 10)[0], expected_map):
        assert received == expected


def test_swap_cities_swaps_correct_cities_2(road_map_2):
    expected_map = [('Mauritania', 'Nouakchott', -20.1, 57.3),
                    ('Mayotte', 'Mamoudzou', -12.48, 45.14),
                    ('Mexico', 'Mexico', 19.2, -99.1),
                    ('Micronesia (Federated States of)', 'Palikir', 6.55, 158),
                    ('Moldova, Republic of', 'Chisinau', 47.02, 28.5),
                    ('Nepal', 'Kathmandu', 27.45, 85.2),
                    ('Myanmar', 'Yangon', 16.45, 96.2),
                    ('Namibia', 'Windhoek', -22.35, 17.04),
                    ('Mozambique', 'Maputo', -25.58, 32.32),
                    ('Netherlands', 'Amsterdam', 52.23, 4.54),
                    ('Netherlands Antilles', 'Willemstad', 12.05, -69),
                    ('New Caledonia', 'Noumea', -22.17, 166.3),
                    ('New Zealand', 'Wellington', -41.19, 174.4),
                    ('Nicaragua', 'Managua', 12.06, -86.2),
                    ('Niger', 'Niamey', 13.27, 2.06),
                    ('Nigeria', 'Abuja', 9.05, 7.32)]
    for received, expected in zip(swap_cities(road_map_2, 5, 8)[0], expected_map):
        assert received == expected


def test_swap_cities_swaps_correct_cities_3(road_map_3):
    expected_map = [('London', 'Hackney', 51.545, -0.0553),
                    ('London', 'Haringey', 51.6, -0.1119),
                    ('London', 'Hammersmith and Fulham', 51.4927, -0.2339),
                    ('London', 'Harrow', 51.5898, -0.3346),
                    ('London', 'Havering', 51.5812, 0.1837),
                    ('London', 'Hillingdon', 51.5441, -0.476)]
    for received, expected in zip(swap_cities(road_map_3, 1, 2)[0], expected_map):
        assert received == expected


def test_swap_cities_correct_distance_1(road_map_3):
    assert swap_cities(road_map_3, 0, 4)[1] == pytest.approx(2.17659411)


def test_swap_cities_correct_distance_2(road_map_4):
    assert swap_cities(road_map_4, 1, 5)[1] == pytest.approx(45.6783272)


'''
################################## 

shift_cities                           

################################## 
'''


def test_shift_cities_returns_list(road_map_1):
    assert isinstance(shift_cities(road_map_1), list)


def test_shift_cities_returns_collection_of_tuples(road_map_2):
    for element in shift_cities(road_map_2):
        assert isinstance(element, tuple)


def test_shift_cities_in_place(road_map_3):
    assert road_map_3 is shift_cities(road_map_3)


def test_shift_cities_right_length_1(road_map_1, length_1):
    assert len(shift_cities(road_map_1)) == length_1


def test_shift_cities_right_length_2(road_map_2, length_2):
    assert len(shift_cities(road_map_2)) == length_2


def test_shift_cities_as_expected_1(road_map_1):
    expected_map = [('North Dakota', 'Bismarck', 48.813343, -100.779004),
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
                    ('North Carolina', 'Raleigh', 35.771, -78.638)]
    for received, expected in zip(shift_cities(road_map_1), expected_map):
        assert received == expected


def test_shift_cities_as_expected_2(road_map_2):
    expected_map = [('Nigeria', 'Abuja', 9.05, 7.32),
                    ('Mauritania', 'Nouakchott', -20.1, 57.3),
                    ('Mayotte', 'Mamoudzou', -12.48, 45.14),
                    ('Mexico', 'Mexico', 19.2, -99.1),
                    ('Micronesia (Federated States of)', 'Palikir', 6.55, 158),
                    ('Moldova, Republic of', 'Chisinau', 47.02, 28.5),
                    ('Mozambique', 'Maputo', -25.58, 32.32),
                    ('Myanmar', 'Yangon', 16.45, 96.2),
                    ('Namibia', 'Windhoek', -22.35, 17.04),
                    ('Nepal', 'Kathmandu', 27.45, 85.2),
                    ('Netherlands', 'Amsterdam', 52.23, 4.54),
                    ('Netherlands Antilles', 'Willemstad', 12.05, -69),
                    ('New Caledonia', 'Noumea', -22.17, 166.3),
                    ('New Zealand', 'Wellington', -41.19, 174.4),
                    ('Nicaragua', 'Managua', 12.06, -86.2),
                    ('Niger', 'Niamey', 13.27, 2.06)]
    for received, expected in zip(shift_cities(road_map_2), expected_map):
        assert received == expected


def test_shift_cities_as_expected_3(road_map_3):
    expected_map = [('London', 'Hillingdon', 51.5441, -0.476),
                    ('London', 'Hackney', 51.545, -0.0553),
                    ('London', 'Hammersmith and Fulham', 51.4927, -0.2339),
                    ('London', 'Haringey', 51.6, -0.1119),
                    ('London', 'Harrow', 51.5898, -0.3346),
                    ('London', 'Havering', 51.5812, 0.1837)]
    for received, expected in zip(shift_cities(road_map_3), expected_map):
        assert received == expected


def test_shift_cities_single_city(road_map_5):
    assert road_map_5[0] == shift_cities(road_map_5)[0]


'''
################################## 

Itinerary() constructor and .road_map property                           

################################## 
'''


def test_itinerary_road_map_is_list_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.road_map, list)


def test_itinerary_road_map_is_list_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert isinstance(itinerary.road_map, list)


def test_itinerary_road_map_is_collection_of_tuples_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    for element in itinerary.road_map:
        assert isinstance(element, tuple)


def test_itinerary_road_map_is_collection_of_tuples_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    for element in itinerary.road_map:
        assert isinstance(element, tuple)


def test_itinerary_road_map_has_right_length_1(road_map_1, length_1):
    itinerary = Itinerary(road_map_1)
    assert len(itinerary.road_map) == length_1


def test_itinerary_road_map_has_right_length_2(road_map_2, length_2):
    itinerary = Itinerary(road_map_2)
    assert len(itinerary.road_map) == length_2


def test_itinerary_road_map_is_collection_of_collections_of_length_four_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    for element in itinerary.road_map:
        assert len(element) == 4


def test_itinerary_road_map_is_collection_of_collections_of_length_four_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    for element in itinerary.road_map:
        assert len(element) == 4


def test_itinerary_road_map_is_input_list_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert itinerary.road_map is road_map_1


def test_itinerary_road_map_is_input_list_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert itinerary.road_map is road_map_2


def test_itinerary_road_map_all_values_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    for received, expected in zip(itinerary.road_map, road_map_1):
        assert received[0] == expected[0]
        assert received[1] == expected[1]
        assert received[2] == pytest.approx(expected[2])
        assert received[3] == pytest.approx(expected[3])


def test_itinerary_road_map_all_values_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    for received, expected in zip(itinerary.road_map, road_map_2):
        assert received[0] == expected[0]
        assert received[1] == expected[1]
        assert received[2] == pytest.approx(expected[2])
        assert received[3] == pytest.approx(expected[3])


def test_itinerary_road_map_setter_changes_road_map_1(road_map_1, road_map_2):
    itinerary = Itinerary(road_map_1)
    itinerary.road_map = road_map_2
    assert itinerary.road_map is road_map_2


def test_itinerary_road_map_setter_changes_road_map_2(road_map_3, road_map_4):
    itinerary = Itinerary(road_map_3)
    itinerary.road_map = road_map_4
    assert itinerary.road_map is road_map_4


'''
################################## 

itinerary.latitude_max()                           

################################## 
'''


def test_itinerary_latitude_max_is_float_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.latitude_max, float)


def test_itinerary_latitude_max_is_float_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert isinstance(itinerary.latitude_max, float)


def test_itinerary_latitude_max_expected_value_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert itinerary.latitude_max == pytest.approx(48.813343)


def test_itinerary_latitude_max_expected_value_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert itinerary.latitude_max == pytest.approx(52.23)


def test_itinerary_latitude_max_expected_value_3(road_map_3):
    itinerary = Itinerary(road_map_3)
    assert itinerary.latitude_max == pytest.approx(51.6)


def test_itinerary_latitude_max_expected_value_4(road_map_4):
    itinerary = Itinerary(road_map_4)
    assert itinerary.latitude_max == pytest.approx(57.477772)


def test_itinerary_latitude_max_expected_value_5(road_map_5):
    itinerary = Itinerary(road_map_5)
    assert itinerary.latitude_max == pytest.approx(51.521728)


def test_itinerary_latitude_max_correct_after_updated_road_map(road_map_1, road_map_2):
    itinerary = Itinerary(road_map_1)
    itinerary.road_map = road_map_2
    assert itinerary.latitude_max == pytest.approx(52.23)


'''
################################## 

itinerary.latitude_min()                           

################################## 
'''


def test_itinerary_latitude_min_is_float_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.latitude_min, float)


def test_itinerary_latitude_min_is_float_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert isinstance(itinerary.latitude_min, float)


def test_itinerary_latitude_min_expected_value_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert itinerary.latitude_min == pytest.approx(32.32)


def test_itinerary_latitude_min_expected_value_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert itinerary.latitude_min == pytest.approx(-41.19)


def test_itinerary_latitude_min_expected_value_3(road_map_3, ):
    itinerary = Itinerary(road_map_3)
    assert itinerary.latitude_min == pytest.approx(51.4927)


def test_itinerary_latitude_min_expected_value_4(road_map_4):
    itinerary = Itinerary(road_map_4)
    assert itinerary.latitude_min == pytest.approx(51.063202)


def test_itinerary_latitude_min_expected_value_5(road_map_5):
    itinerary = Itinerary(road_map_5)
    assert itinerary.latitude_min == pytest.approx(51.521728)


def test_itinerary_latitude_min_correct_after_updated_road_map(road_map_1, road_map_2):
    itinerary = Itinerary(road_map_1)
    itinerary.road_map = road_map_2
    assert itinerary.latitude_min == pytest.approx(-41.19)


'''
################################## 

itinerary.longitude_max()                           

################################## 
'''


def test_itinerary_longitude_max_is_float_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.longitude_max, float)


def test_itinerary_longitude_max_is_float_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert isinstance(itinerary.longitude_max, float)


def test_itinerary_longitude_max_expected_value_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert itinerary.longitude_max == pytest.approx(-71.549127)


def test_itinerary_longitude_max_expected_value_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert itinerary.longitude_max == pytest.approx(174.4)


def test_itinerary_longitude_max_expected_value_3(road_map_3):
    itinerary = Itinerary(road_map_3)
    assert itinerary.longitude_max == pytest.approx(0.1837)


def test_itinerary_longitude_max_expected_value_4(road_map_4):
    itinerary = Itinerary(road_map_4)
    assert itinerary.longitude_max == pytest.approx(-0.09214)


def test_itinerary_longitude_max_expected_value_5(road_map_5):
    itinerary = Itinerary(road_map_5)
    assert itinerary.longitude_max == pytest.approx(-0.129338)


def test_itinerary_longitude_max_correct_after_updated_road_map(road_map_1, road_map_2):
    itinerary = Itinerary(road_map_1)
    itinerary.road_map = road_map_2
    assert itinerary.longitude_max == pytest.approx(174.4)


'''
################################## 

itinerary.longitude_min()                           

################################## 
'''


def test_itinerary_longitude_min_is_float_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.longitude_min, float)


def test_itinerary_longitude_min_is_float_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert isinstance(itinerary.longitude_min, float)


def test_itinerary_longitude_min_expected_value_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert itinerary.longitude_min == pytest.approx(-119.753877)


def test_itinerary_longitude_min_expected_value_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert itinerary.longitude_min == pytest.approx(-99.1)


def test_itinerary_longitude_min_expected_value_3(road_map_3):
    itinerary = Itinerary(road_map_3)
    assert itinerary.longitude_min == pytest.approx(-0.476)


def test_itinerary_longitude_min_expected_value_4(road_map_4):
    itinerary = Itinerary(road_map_4)
    assert itinerary.longitude_min == pytest.approx(-7.3074)


def test_itinerary_longitude_min_expected_value_5(road_map_5):
    itinerary = Itinerary(road_map_5)
    assert itinerary.longitude_min == pytest.approx(-0.129338)


def test_itinerary_longitude_min_correct_after_updated_road_map(road_map_1, road_map_2):
    itinerary = Itinerary(road_map_1)
    itinerary.road_map = road_map_2
    assert itinerary.longitude_min == pytest.approx(-99.1)


'''
################################## 

itinerary.is_single_point                           

################################## 
'''


def test_itinerary_is_single_point_returns_boolean(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert isinstance(itinerary.is_single_point, bool)


def test_itinerary_is_single_point_expected_false_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    assert not itinerary.is_single_point


def test_itinerary_is_single_point_expected_false_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    assert not itinerary.is_single_point


def test_itinerary_is_single_point_single_city_1(road_map_5):
    itinerary = Itinerary(road_map_5)
    assert itinerary.is_single_point


def test_itinerary_is_single_point_single_city_2():
    itinerary = Itinerary([('Awesomeville', 'pop-1-module', -1, 10)])
    assert itinerary.is_single_point


def test_itinerary_is_single_point_repeated_city():
    itinerary = Itinerary([('Awesomeville', 'pop-1-module', -1, 10),
                           ('Awesomeville', 'pop-1-module', -1, 10)])
    assert itinerary.is_single_point


def test_itinerary_is_single_point_overlapping_city():
    itinerary = Itinerary([('Awesomeville', 'pop-1-module', -1, 10),
                           ('Amazingtown', 'python', -1, 10)])
    assert itinerary.is_single_point


'''
################################## 

itinerary.coordinates()                           

################################## 
'''


def test_itinerary_coordinates_returns_generator(road_map_1):
    assert isinstance(Itinerary(road_map_1).coordinates, types.GeneratorType)


def test_itinerary_coordinates_generates_tuples(road_map_1):
    for element in Itinerary(road_map_1).coordinates:
        assert isinstance(element, tuple)


def test_itinerary_coordinates_generates_correct_number_of_tuples(road_map_1, length_1):
    assert len(list(Itinerary(road_map_1).coordinates)) == length_1


def test_itinerary_coordinates_generates_pairs(road_map_1):
    for element in Itinerary(road_map_1).coordinates:
        assert len(element) == 2


def test_itinerary_coordinates_generates_pairs_of_floats(road_map_1):
    for element in Itinerary(road_map_1).coordinates:
        assert isinstance(element[0], float)
        assert isinstance(element[1], float)


def test_itinerary_coordinates_right_length_1(road_map_1, length_1):
    assert len(list(Itinerary(road_map_1).coordinates)) == length_1


def test_itinerary_coordinates_right_length_2(road_map_2, length_2):
    assert len(list(Itinerary(road_map_2).coordinates)) == length_2


def test_itinerary_coordinates_right_length_single_city(road_map_5):
    assert len(list(Itinerary(road_map_5).coordinates)) == 1


def test_itinerary_coordinates_as_expected_1(road_map_1):
    expected_coords = [(44.95, -93.094),
                       (32.32, -90.207),
                       (38.572954, -92.189283),
                       (46.595805, -112.027031),
                       (40.809868, -96.675345),
                       (39.160949, -119.753877),
                       (43.220093, -71.549127),
                       (40.221741, -74.756138),
                       (35.667231, -105.964575),
                       (42.659829, -73.781339),
                       (35.771, -78.638),
                       (48.813343, -100.779004)]
    for (lat_received, long_received), (lat_expected, long_expected) in zip(Itinerary(road_map_1).coordinates,
                                                                            expected_coords):
        assert lat_received == pytest.approx(lat_expected)
        assert long_received == pytest.approx(long_expected)


def test_itinerary_coordinates_as_expected_2(road_map_2):
    expected_coords = [(-20.1, 57.3),
                       (-12.48, 45.14),
                       (19.2, -99.1),
                       (6.55, 158.0),
                       (47.02, 28.5),
                       (-25.58, 32.32),
                       (16.45, 96.2),
                       (-22.35, 17.04),
                       (27.45, 85.2),
                       (52.23, 4.54),
                       (12.05, -69.0),
                       (-22.17, 166.3),
                       (-41.19, 174.4),
                       (12.06, -86.2),
                       (13.27, 2.06),
                       (9.05, 7.32)]
    for (lat_received, long_received), (lat_expected, long_expected) in zip(Itinerary(road_map_2).coordinates,
                                                                            expected_coords):
        assert lat_received == pytest.approx(lat_expected)
        assert long_received == pytest.approx(long_expected)


def test_itinerary_coordinates_as_expected_3(road_map_3):
    expected_coords = [(51.545, -0.0553),
                       (51.4927, -0.2339),
                       (51.6, -0.1119),
                       (51.5898, -0.3346),
                       (51.5812, 0.1837),
                       (51.5441, -0.476)]
    for (lat_received, long_received), (lat_expected, long_expected) in zip(Itinerary(road_map_3).coordinates,
                                                                            expected_coords):
        assert lat_received == pytest.approx(lat_expected)
        assert long_received == pytest.approx(long_expected)


def test_itinerary_coordinates_as_expected_4(road_map_4):
    expected_coords = [(51.209, -2.647),
                       (51.515457, -0.09214),
                       (51.063202, -1.308),
                       (52.59137, -2.110748),
                       (52.192001, -2.22),
                       (53.958332, -1.080278),
                       (57.149651, -2.099075),
                       (56.462002, -2.9707),
                       (55.953251, -3.188267),
                       (55.860916, -4.251433),
                       (57.477772, -4.224721),
                       (56.396999, -3.437),
                       (56.1166, -3.9369),
                       (53.228, -4.128),
                       (51.481583, -3.17909),
                       (51.58333, -2.98333),
                       (53.2667, -3.45),
                       (51.882, -5.269),
                       (51.621441, -3.943646),
                       (54.35, -6.6667),
                       (54.607868, -5.926437),
                       (54.5234, -6.03527),
                       (54.175999, -6.349),
                       (54.9958, -7.3074)]
    for (lat_received, long_received), (lat_expected, long_expected) in zip(Itinerary(road_map_4).coordinates,
                                                                            expected_coords):
        assert lat_received == pytest.approx(lat_expected)
        assert long_received == pytest.approx(long_expected)


def test_itinerary_coordinates_as_expected_5(road_map_5):
    expected_coords = [(51.521728, -0.129338)]
    for (lat_received, long_received), (lat_expected, long_expected) in zip(Itinerary(road_map_5).coordinates,
                                                                            expected_coords):
        assert lat_received == pytest.approx(lat_expected)
        assert long_received == pytest.approx(long_expected)


'''
################################## 

itinerary.legs                           

################################## 
'''


def test_itinerary_legs_returns_iterator(road_map_1):
    assert isinstance(Itinerary(road_map_1).legs, collections.abc.Iterator)


def test_itinerary_legs_generates_tuples(road_map_1):
    for element in Itinerary(road_map_1).legs:
        assert isinstance(element, tuple)


def test_itinerary_legs_generates_correct_number_of_tuples(road_map_1, length_1):
    assert len(list(Itinerary(road_map_1).legs)) == length_1


def test_itinerary_legs_generates_pairs(road_map_1):
    for element in Itinerary(road_map_1).legs:
        assert len(element) == 2


def test_itinerary_legs_generates_pairs_of_tuples(road_map_1):
    for element in Itinerary(road_map_1).legs:
        assert isinstance(element[0], tuple)
        assert isinstance(element[1], tuple)


def test_itinerary_legs_generates_pairs_of_pairs(road_map_1):
    for element in Itinerary(road_map_1).legs:
        assert len(element[0]) == 2
        assert len(element[1]) == 2


def test_itinerary_legs_generates_pairs_of_pairs_of_floats(road_map_1):
    for element in Itinerary(road_map_1).legs:
        assert isinstance(element[0][0], float)
        assert isinstance(element[0][1], float)
        assert isinstance(element[1][0], float)
        assert isinstance(element[1][1], float)


def test_itinerary_legs_right_length_1(road_map_1, length_1):
    assert len(list(Itinerary(road_map_1).legs)) == length_1


def test_itinerary_legs_right_length_2(road_map_2, length_2):
    assert len(list(Itinerary(road_map_2).legs)) == length_2


def test_itinerary_legs_right_length_single_city(road_map_5, length_5):
    assert len(list(Itinerary(road_map_5).legs)) == length_5


def test_itinerary_legs_as_expected_1(road_map_1):
    expected_legs = [((44.95, -93.094), (32.32, -90.207)),
                     ((32.32, -90.207), (38.572954, -92.189283)),
                     ((38.572954, -92.189283), (46.595805, -112.027031)),
                     ((46.595805, -112.027031), (40.809868, -96.675345)),
                     ((40.809868, -96.675345), (39.160949, -119.753877)),
                     ((39.160949, -119.753877), (43.220093, -71.549127)),
                     ((43.220093, -71.549127), (40.221741, -74.756138)),
                     ((40.221741, -74.756138), (35.667231, -105.964575)),
                     ((35.667231, -105.964575), (42.659829, -73.781339)),
                     ((42.659829, -73.781339), (35.771, -78.638)),
                     ((35.771, -78.638), (48.813343, -100.779004)),
                     ((48.813343, -100.779004), (44.95, -93.094))]
    for received, expected in zip(Itinerary(road_map_1).legs, expected_legs):
        assert received[0][0] == pytest.approx(expected[0][0])
        assert received[0][1] == pytest.approx(expected[0][1])
        assert received[1][0] == pytest.approx(expected[1][0])
        assert received[1][1] == pytest.approx(expected[1][1])


def test_itinerary_legs_as_expected_2(road_map_2):
    expected_legs = [((-20.1, 57.3), (-12.48, 45.14)),
                     ((-12.48, 45.14), (19.2, -99.1)),
                     ((19.2, -99.1), (6.55, 158.0)),
                     ((6.55, 158.0), (47.02, 28.5)),
                     ((47.02, 28.5), (-25.58, 32.32)),
                     ((-25.58, 32.32), (16.45, 96.2)),
                     ((16.45, 96.2), (-22.35, 17.04)),
                     ((-22.35, 17.04), (27.45, 85.2)),
                     ((27.45, 85.2), (52.23, 4.54)),
                     ((52.23, 4.54), (12.05, -69.0)),
                     ((12.05, -69.0), (-22.17, 166.3)),
                     ((-22.17, 166.3), (-41.19, 174.4)),
                     ((-41.19, 174.4), (12.06, -86.2)),
                     ((12.06, -86.2), (13.27, 2.06)),
                     ((13.27, 2.06), (9.05, 7.32)),
                     ((9.05, 7.32), (-20.1, 57.3))]
    for received, expected in zip(Itinerary(road_map_2).legs, expected_legs):
        assert received[0][0] == pytest.approx(expected[0][0])
        assert received[0][1] == pytest.approx(expected[0][1])
        assert received[1][0] == pytest.approx(expected[1][0])
        assert received[1][1] == pytest.approx(expected[1][1])


def test_itinerary_legs_as_expected_3(road_map_3):
    expected_legs = [((51.545, -0.0553), (51.4927, -0.2339)),
                     ((51.4927, -0.2339), (51.6, -0.1119)),
                     ((51.6, -0.1119), (51.5898, -0.3346)),
                     ((51.5898, -0.3346), (51.5812, 0.1837)),
                     ((51.5812, 0.1837), (51.5441, -0.476)),
                     ((51.5441, -0.476), (51.545, -0.0553))]
    for received, expected in zip(Itinerary(road_map_3).legs, expected_legs):
        assert received[0][0] == pytest.approx(expected[0][0])
        assert received[0][1] == pytest.approx(expected[0][1])
        assert received[1][0] == pytest.approx(expected[1][0])
        assert received[1][1] == pytest.approx(expected[1][1])


def test_itinerary_legs_as_expected_4(road_map_4):
    expected_legs = [((51.209, -2.647), (51.515457, -0.09214)),
                     ((51.515457, -0.09214), (51.063202, -1.308)),
                     ((51.063202, -1.308), (52.59137, -2.110748)),
                     ((52.59137, -2.110748), (52.192001, -2.22)),
                     ((52.192001, -2.22), (53.958332, -1.080278)),
                     ((53.958332, -1.080278), (57.149651, -2.099075)),
                     ((57.149651, -2.099075), (56.462002, -2.9707)),
                     ((56.462002, -2.9707), (55.953251, -3.188267)),
                     ((55.953251, -3.188267), (55.860916, -4.251433)),
                     ((55.860916, -4.251433), (57.477772, -4.224721)),
                     ((57.477772, -4.224721), (56.396999, -3.437)),
                     ((56.396999, -3.437), (56.1166, -3.9369)),
                     ((56.1166, -3.9369), (53.228, -4.128)),
                     ((53.228, -4.128), (51.481583, -3.17909)),
                     ((51.481583, -3.17909), (51.58333, -2.98333)),
                     ((51.58333, -2.98333), (53.2667, -3.45)),
                     ((53.2667, -3.45), (51.882, -5.269)),
                     ((51.882, -5.269), (51.621441, -3.943646)),
                     ((51.621441, -3.943646), (54.35, -6.6667)),
                     ((54.35, -6.6667), (54.607868, -5.926437)),
                     ((54.607868, -5.926437), (54.5234, -6.03527)),
                     ((54.5234, -6.03527), (54.175999, -6.349)),
                     ((54.175999, -6.349), (54.9958, -7.3074)),
                     ((54.9958, -7.3074), (51.209, -2.647))]
    for received, expected in zip(Itinerary(road_map_4).legs, expected_legs):
        assert received[0][0] == pytest.approx(expected[0][0])
        assert received[0][1] == pytest.approx(expected[0][1])
        assert received[1][0] == pytest.approx(expected[1][0])
        assert received[1][1] == pytest.approx(expected[1][1])


def test_itinerary_legs_as_expected_5(road_map_5):
    expected_legs = [((51.521728, -0.129338), (51.521728, -0.129338))]
    for received, expected in zip(Itinerary(road_map_5).legs, expected_legs):
        assert received[0][0] == pytest.approx(expected[0][0])
        assert received[0][1] == pytest.approx(expected[0][1])
        assert received[1][0] == pytest.approx(expected[1][0])
        assert received[1][1] == pytest.approx(expected[1][1])


'''
################################## 

ItineraryDrawer() constructor and associated properties                          

################################## 
'''


def test_itinerarydrawer_default_constructor_type():
    assert isinstance(ItineraryDrawer(), ItineraryDrawer)


def test_itinerarydrawer_default_constructor_parameters():
    drawer = ItineraryDrawer()
    assert drawer.drawable_size_px == 700
    assert drawer.margin_px == 50
    assert drawer.min_grid_lines == 5
    assert drawer.grid_line_colour == 'lightblue1'
    assert drawer.grid_line_thickness == 1
    assert drawer.leg_line_colour == 'red'
    assert drawer.leg_line_thickness == 1
    assert drawer.city_radius == 2
    assert drawer.city_fill == 'white'
    assert drawer.city_line_colour == 'black'
    assert drawer.city_line_thickness == 1
    assert drawer.label_font == ('purisa', 8)
    assert drawer.degrees_to_show_for_single_point == 1.0


def test_itinerarydrawer_constructor_parameters_1():
    drawer = ItineraryDrawer(drawable_size_px=500, margin_px=100, min_grid_lines=10, grid_line_colour='red',
                             grid_line_thickness=2, leg_line_colour='white', leg_line_thickness=3, city_radius=5,
                             city_fill='red', city_line_colour='red', city_line_thickness=3,
                             label_font=('Times', 9), degrees_to_show_for_single_point=10.0)
    assert drawer.drawable_size_px == 500
    assert drawer.margin_px == 100
    assert drawer.min_grid_lines == 10
    assert drawer.grid_line_colour == 'red'
    assert drawer.grid_line_thickness == 2
    assert drawer.leg_line_colour == 'white'
    assert drawer.leg_line_thickness == 3
    assert drawer.city_radius == 5
    assert drawer.city_fill == 'red'
    assert drawer.city_line_colour == 'red'
    assert drawer.city_line_thickness == 3
    assert drawer.label_font == ('Times', 9)
    assert drawer.degrees_to_show_for_single_point == pytest.approx(10.0)


def test_itinerarydrawer_constructor_parameters_2():
    drawer = ItineraryDrawer(drawable_size_px=500, margin_px=10, min_grid_lines=7)
    assert drawer.drawable_size_px == 500
    assert drawer.margin_px == 10
    assert drawer.min_grid_lines == 7


def test_itinerarydrawer_constructor_parameters_converts_floats_to_ints():
    drawer = ItineraryDrawer(drawable_size_px=100.1, margin_px=0.25, min_grid_lines=2.7)
    assert drawer.drawable_size_px == 100
    assert drawer.margin_px == 0
    assert drawer.min_grid_lines == 3


def test_itinerarydrawer_constructor_floors_at_one_gridline():
    drawer = ItineraryDrawer(drawable_size_px=9999, margin_px=300, min_grid_lines=-9)
    assert drawer.drawable_size_px == 9999
    assert drawer.margin_px == 300
    assert drawer.min_grid_lines == 1


def test_itinerarydrawer_constructor_floors_at_zero_pixels():
    drawer = ItineraryDrawer(drawable_size_px=-12, margin_px=-3, min_grid_lines=1)
    assert drawer.drawable_size_px == 0
    assert drawer.margin_px == 0
    assert drawer.min_grid_lines == 1


def test_itinerarydrawer_parameters_setters_1():
    drawer = ItineraryDrawer()

    drawer.drawable_size_px = 60
    drawer.margin_px = 10
    drawer.min_grid_lines = 1

    assert drawer.drawable_size_px == 60
    assert drawer.margin_px == 10
    assert drawer.min_grid_lines == 1


def test_itinerarydrawer_parameters_setters_2():
    drawer = ItineraryDrawer()

    drawer.drawable_size_px = 1254
    drawer.margin_px = 200
    drawer.min_grid_lines = 80

    assert drawer.drawable_size_px == 1254
    assert drawer.margin_px == 200
    assert drawer.min_grid_lines == 80


def test_itinerarydrawer_parameters_setters_converts_floats_to_ints():
    drawer = ItineraryDrawer()

    drawer.drawable_size_px = 10.3
    drawer.margin_px = 20.1
    drawer.min_grid_lines = 7.88

    assert drawer.drawable_size_px == 10
    assert drawer.margin_px == 20
    assert drawer.min_grid_lines == 8


def test_itinerarydrawer_parameters_setters_floors_at_one_gridline():
    drawer = ItineraryDrawer()

    drawer.drawable_size_px = 100
    drawer.margin_px = 10
    drawer.min_grid_lines = 0

    assert drawer.drawable_size_px == 100
    assert drawer.margin_px == 10
    assert drawer.min_grid_lines == 1


def test_itinerarydrawer_parameters_setters_floors_at_zero_pixels():
    drawer = ItineraryDrawer()

    drawer.drawable_size_px = -888.88
    drawer.margin_px = -88.8
    drawer.min_grid_lines = 10

    assert drawer.drawable_size_px == 0
    assert drawer.margin_px == 0
    assert drawer.min_grid_lines == 10


'''
################################## 

ItineraryDrawer._lat_to_y                        

################################## 
'''


def test_itinerarydrawer_lat_to_y_returns_int():
    drawer = ItineraryDrawer()
    assert isinstance(drawer._lat_to_y(80.1, 12.8, 81.3), int)


def test_itinerarydrawer_lat_to_y_as_expected_1():
    drawer = ItineraryDrawer()
    assert drawer._lat_to_y(80.1, 12.8, 81.3) == 65


def test_itinerarydrawer_lat_to_y_as_expected_2():
    drawer = ItineraryDrawer()
    assert drawer._lat_to_y(-10.3, 2.5, -1.2) == 73


def test_itinerarydrawer_lat_to_y_as_expected_3():
    drawer = ItineraryDrawer()
    assert drawer._lat_to_y(0.01, 10, 1.0) == 60


def test_itinerarydrawer_lat_to_y_as_expected_4():
    drawer = ItineraryDrawer(margin_px=5)
    assert drawer._lat_to_y(0.01, 20, 1.0) == 25


def test_itinerarydrawer_lat_to_y_as_expected_5():
    drawer = ItineraryDrawer(margin_px=20)
    assert drawer._lat_to_y(-70, 0.01, 21.4) == 21


'''
################################## 

ItineraryDrawer._long_to_x                        

################################## 
'''


def test_itinerarydrawer_long_to_x_returns_int():
    drawer = ItineraryDrawer()
    assert isinstance(drawer._long_to_x(80.1, 12.8, 61.3), int)


def test_itinerarydrawer_long_to_x_as_expected_1():
    drawer = ItineraryDrawer()
    assert drawer._long_to_x(80.1, 12.8, 61.3) == 291


def test_itinerarydrawer_long_to_x_as_expected_2():
    drawer = ItineraryDrawer()
    assert drawer._long_to_x(-10.3, 2.5, -20.2) == 75


def test_itinerarydrawer_long_to_x_as_expected_3():
    drawer = ItineraryDrawer()
    assert drawer._long_to_x(0.01, 10, -0.05) == 51


def test_itinerarydrawer_long_to_x_as_expected_4():
    drawer = ItineraryDrawer(margin_px=5)
    assert drawer._long_to_x(0.01, 2000, -0.01) == 45


def test_itinerarydrawer_long_to_x_as_expected_5():
    drawer = ItineraryDrawer(margin_px=20)
    assert drawer._long_to_x(70, 10, 21.4) == 506


'''
################################## 

ItineraryDrawer._points                        

################################## 
'''


def test_itinerarydrawer_points_returns_generator(road_map_1):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_1)
    received_points = drawer._points(itinerary)
    assert isinstance(received_points, types.GeneratorType)


def test_itinerarydrawer_points_generates_tuples(road_map_1):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_1)
    for element in drawer._points(itinerary):
        assert isinstance(element, tuple)


def test_itinerarydrawer_points_generates_pairs(road_map_1):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_1)
    for element in drawer._points(itinerary):
        assert len(element) == 2


def test_itinerarydrawer_points_generates_pairs_of_ints(road_map_1):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_1)
    for element in drawer._points(itinerary):
        assert isinstance(element[0], int)
        assert isinstance(element[1], int)


def test_itinerarydrawer_points_right_length_1(road_map_1, length_1):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_1)
    received_points = drawer._points(itinerary)
    assert len(list(received_points)) == length_1


def test_itinerarydrawer_points_right_length_2(road_map_2, length_2):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_2)
    received_points = drawer._points(itinerary)
    assert len(list(received_points)) == length_2


def test_itinerarydrawer_points_right_length_single_city(road_map_5, length_5):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_5)
    received_points = drawer._points(itinerary)
    assert len(list(received_points)) == length_5


def test_itinerarydrawer_points_as_expected_1(road_map_1):
    expected_points = [(437, 106), (479, 290), (450, 199), (162, 82), (385, 166), (50, 190), (750, 131), (703, 175),
                       (250, 241), (718, 139), (647, 239), (326, 50)]
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_1)
    received_points = drawer._points(itinerary)
    for received, expected in zip(received_points, expected_points):
        assert received[0] == expected[0]
        assert received[1] == expected[1]


def test_itinerarydrawer_points_as_expected_2(road_map_2):
    expected_points = [(450, 235), (419, 216), (50, 135), (708, 167), (377, 63), (386, 249), (550, 142), (347, 241),
                       (522, 113), (315, 50), (127, 153), (729, 240), (750, 289), (83, 153), (309, 150), (322, 161)]
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_2)
    received_points = drawer._points(itinerary)
    for received, expected in zip(received_points, expected_points):
        assert received[0] == expected[0]
        assert received[1] == expected[1]


def test_itinerarydrawer_points_as_expected_3(road_map_3):
    expected_points = [(496, 108), (307, 164), (436, 50), (200, 61), (750, 70), (50, 109)]
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_3)
    received_points = drawer._points(itinerary)
    for received, expected in zip(received_points, expected_points):
        assert received[0] == expected[0]
        assert received[1] == expected[1]


def test_itinerarydrawer_points_as_expected_4(road_map_4):
    expected_points = [(502, 658), (750, 628), (632, 672), (554, 524), (544, 563), (654, 391), (555, 82), (471, 149),
                       (450, 198), (346, 207), (349, 50), (425, 155), (377, 182), (358, 462), (451, 632), (470, 622),
                       (424, 459), (248, 593), (376, 618), (112, 353), (184, 328), (173, 337), (143, 370), (50, 291)]
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_4)
    received_points = drawer._points(itinerary)
    for received, expected in zip(received_points, expected_points):
        assert received[0] == expected[0]
        assert received[1] == expected[1]


def test_itinerarydrawer_points_as_expected_single_city(road_map_5):
    expected_points = [(400, 400)]
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_5)
    received_points = drawer._points(itinerary)
    for received, expected in zip(received_points, expected_points):
        assert received[0] == expected[0]
        assert received[1] == expected[1]


def test_itinerarydrawer_points_as_expected_single_city_non_default_drawer(road_map_5):
    expected_points = [(510, 510)]
    drawer = ItineraryDrawer(margin_px=10, drawable_size_px=1000)
    itinerary = Itinerary(road_map_5)
    received_points = drawer._points(itinerary)
    for received, expected in zip(received_points, expected_points):
        assert received[0] == expected[0]
        assert received[1] == expected[1]


'''
################################## 

ItineraryDrawer._points_pairs                   

################################## 
'''


def test_itinerarydrawer_point_pairs_returns_generator(road_map_1):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_1)
    received_points = drawer._point_pairs(itinerary)
    assert isinstance(received_points, types.GeneratorType)


def test_itinerarydrawer_point_pairs_generates_tuples(road_map_1):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_1)
    for element in drawer._point_pairs(itinerary):
        assert isinstance(element, tuple)


def test_itinerarydrawer_point_pairs_generates_pairs(road_map_1):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_1)
    for element in drawer._point_pairs(itinerary):
        assert len(element) == 2


def test_itinerarydrawer_point_pairs_generates_pairs_of_tuples(road_map_1):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_1)
    for element in drawer._point_pairs(itinerary):
        assert isinstance(element[0], tuple)
        assert isinstance(element[1], tuple)


def test_itinerarydrawer_point_pairs_generates_pairs_of_pairs_of_ints(road_map_1):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_1)
    for element in drawer._point_pairs(itinerary):
        assert isinstance(element[0][0], int)
        assert isinstance(element[0][1], int)
        assert isinstance(element[1][0], int)
        assert isinstance(element[1][1], int)


def test_itinerarydrawer_point_pairs_right_length_1(road_map_1, length_1):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_1)
    received_points = drawer._point_pairs(itinerary)
    assert len(list(received_points)) == length_1


def test_itinerarydrawer_point_pairs_right_length_2(road_map_2, length_2):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_2)
    received_points = drawer._point_pairs(itinerary)
    assert len(list(received_points)) == length_2


def test_itinerarydrawer_point_pairs_right_length_single_city(road_map_5, length_5):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_5)
    received_points = drawer._point_pairs(itinerary)
    assert len(list(received_points)) == length_5


def test_itinerarydrawer_point_pairs_as_expected_1(road_map_1):
    expected_points = [((437, 106), (479, 290)),
                       ((479, 290), (450, 199)),
                       ((450, 199), (162, 82)),
                       ((162, 82), (385, 166)),
                       ((385, 166), (50, 190)),
                       ((50, 190), (750, 131)),
                       ((750, 131), (703, 175)),
                       ((703, 175), (250, 241)),
                       ((250, 241), (718, 139)),
                       ((718, 139), (647, 239)),
                       ((647, 239), (326, 50)),
                       ((326, 50), (437, 106))]
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_1)
    received_points = drawer._point_pairs(itinerary)
    for received, expected in zip(received_points, expected_points):
        assert received[0] == expected[0]
        assert received[1] == expected[1]


def test_itinerarydrawer_point_pairs_as_expected_2(road_map_2):
    expected_points = [((450, 235), (419, 216)),
                       ((419, 216), (50, 135)),
                       ((50, 135), (708, 167)),
                       ((708, 167), (377, 63)),
                       ((377, 63), (386, 249)),
                       ((386, 249), (550, 142)),
                       ((550, 142), (347, 241)),
                       ((347, 241), (522, 113)),
                       ((522, 113), (315, 50)),
                       ((315, 50), (127, 153)),
                       ((127, 153), (729, 240)),
                       ((729, 240), (750, 289)),
                       ((750, 289), (83, 153)),
                       ((83, 153), (309, 150)),
                       ((309, 150), (322, 161)),
                       ((322, 161), (450, 235))]
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_2)
    received_points = drawer._point_pairs(itinerary)
    for received, expected in zip(received_points, expected_points):
        assert received[0] == expected[0]
        assert received[1] == expected[1]


def test_itinerarydrawer_point_pairs_as_expected_3(road_map_3):
    expected_points = [((496, 108), (307, 164)),
                       ((307, 164), (436, 50)),
                       ((436, 50), (200, 61)),
                       ((200, 61), (750, 70)),
                       ((750, 70), (50, 109)),
                       ((50, 109), (496, 108))]
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_3)
    received_points = drawer._point_pairs(itinerary)
    for received, expected in zip(received_points, expected_points):
        assert received[0] == expected[0]
        assert received[1] == expected[1]


def test_itinerarydrawer_point_pairs_as_expected_4(road_map_4):
    expected_points = [((502, 658), (750, 628)),
                       ((750, 628), (632, 672)),
                       ((632, 672), (554, 524)),
                       ((554, 524), (544, 563)),
                       ((544, 563), (654, 391)),
                       ((654, 391), (555, 82)),
                       ((555, 82), (471, 149)),
                       ((471, 149), (450, 198)),
                       ((450, 198), (346, 207)),
                       ((346, 207), (349, 50)),
                       ((349, 50), (425, 155)),
                       ((425, 155), (377, 182)),
                       ((377, 182), (358, 462)),
                       ((358, 462), (451, 632)),
                       ((451, 632), (470, 622)),
                       ((470, 622), (424, 459)),
                       ((424, 459), (248, 593)),
                       ((248, 593), (376, 618)),
                       ((376, 618), (112, 353)),
                       ((112, 353), (184, 328)),
                       ((184, 328), (173, 337)),
                       ((173, 337), (143, 370)),
                       ((143, 370), (50, 291)),
                       ((50, 291), (502, 658))]
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_4)
    received_points = drawer._point_pairs(itinerary)
    for received, expected in zip(received_points, expected_points):
        assert received[0] == expected[0]
        assert received[1] == expected[1]


def test_itinerarydrawer_point_pairs_as_expected_5(road_map_5):
    expected_points = [((50, 50), (50, 50))]
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_5)
    received_points = drawer._point_pairs(itinerary)
    for received, expected in zip(received_points, expected_points):
        assert received[0] == expected[0]
        assert received[1] == expected[1]


'''
################################## 

ItineraryDrawer._canvas_dimensions                   

################################## 
'''


def test_itinerarydrawer_canvas_dimensions_2_returns_tuple(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    assert isinstance(drawer._canvas_dimensions(itinerary), tuple)


def test_itinerarydrawer_canvas_dimensions_2_returns_pair(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    assert len(drawer._canvas_dimensions(itinerary)) == 2


def test_itinerarydrawer_canvas_dimensions_2_returns_pair_of_ints(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    width, height = drawer._canvas_dimensions(itinerary)
    assert isinstance(width, int)
    assert isinstance(height, int)


def test_itinerarydrawer_canvas_dimensions_2_as_expected_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    width, height = drawer._canvas_dimensions(itinerary)
    assert (width, height) == (800, 340)


def test_itinerarydrawer_canvas_dimensions_2_as_expected_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    drawer = ItineraryDrawer(drawable_size_px=400, margin_px=20)
    width, height = drawer._canvas_dimensions(itinerary)
    assert (width, height) == (440, 177)


def test_itinerarydrawer_canvas_dimensions_2_as_expected_3():
    itinerary = Itinerary([('a', 'b', 10, 5), ('c', 'd', -10, -5)])
    drawer = ItineraryDrawer()
    drawer.drawable_size_px = 500
    drawer.margin_px = 10
    width, height = drawer._canvas_dimensions(itinerary)
    assert (width, height) == (270, 520)


def test_itinerarydrawer_canvas_dimension_2_as_expected_single_city(road_map_5):
    itinerary = Itinerary(road_map_5)
    drawer = ItineraryDrawer()
    width, height = drawer._canvas_dimensions(itinerary)
    assert (width, height) == (800, 800)


def test_itinerarydrawer_canvas_dimension_2_as_expected_single_city_with_non_default_params(road_map_5):
    itinerary = Itinerary(road_map_5)
    drawer = ItineraryDrawer(drawable_size_px=300, margin_px=100)
    width, height = drawer._canvas_dimensions(itinerary)
    assert (width, height) == (500, 500)


'''
################################## 

ItineraryDrawer._max_range                   

################################## 
'''


def test_itinerarydrawer_max_range_returns_float(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    assert isinstance(drawer._max_range(itinerary), float)


def test_itinerarydrawer_max_range_as_expected_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    assert drawer._max_range(itinerary) == pytest.approx(48.20475)


def test_itinerarydrawer_max_range_as_expected_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    drawer = ItineraryDrawer()
    assert drawer._max_range(itinerary) == pytest.approx(273.5)


def test_itinerarydrawer_max_range_as_expected_3(road_map_3):
    itinerary = Itinerary(road_map_3)
    drawer = ItineraryDrawer()
    assert drawer._max_range(itinerary) == pytest.approx(0.6597)


def test_itinerarydrawer_max_range_as_expected_4(road_map_4):
    itinerary = Itinerary(road_map_4)
    drawer = ItineraryDrawer()
    assert drawer._max_range(itinerary) == pytest.approx(7.21526)


def test_itinerarydrawer_max_range_as_expected_single_city(road_map_5):
    itinerary = Itinerary(road_map_5)
    drawer = ItineraryDrawer()
    assert drawer._max_range(itinerary) == pytest.approx(1.0)


def test_itinerarydrawer_max_range_as_expected_single_city_non_default_size(road_map_5):
    itinerary = Itinerary(road_map_5)
    drawer = ItineraryDrawer(degrees_to_show_for_single_point=22.3)
    assert drawer._max_range(itinerary) == pytest.approx(22.3)


'''
################################## 

ItineraryDrawer._pixels_per_degree                   

################################## 
'''


def test_itinerarydrawer_pixels_per_degree_returns_float(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    assert isinstance(drawer._pixels_per_degree(itinerary), float)


def test_itinerarydrawer_pixels_per_degree_as_expected_1(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    assert drawer._pixels_per_degree(itinerary) == pytest.approx(14.52139)


def test_itinerarydrawer_pixels_per_degree_as_expected_2(road_map_2):
    itinerary = Itinerary(road_map_2)
    drawer = ItineraryDrawer()
    assert drawer._pixels_per_degree(itinerary) == pytest.approx(2.5594149)


def test_itinerarydrawer_pixels_per_degree_as_expected_3(road_map_3):
    itinerary = Itinerary(road_map_3)
    drawer = ItineraryDrawer()
    assert drawer._pixels_per_degree(itinerary) == pytest.approx(1061.0883)


def test_itinerarydrawer_pixels_per_degree_as_expected_4(road_map_4):
    itinerary = Itinerary(road_map_4)
    drawer = ItineraryDrawer()
    assert drawer._pixels_per_degree(itinerary) == pytest.approx(97.016600)


def test_itinerarydrawer_pixels_per_degree_as_expected_single_city(road_map_5):
    itinerary = Itinerary(road_map_5)
    drawer = ItineraryDrawer()
    assert drawer._pixels_per_degree(itinerary) == pytest.approx(700.0)


def test_itinerarydrawer_pixels_per_degree_as_expected_single_city_non_default_size(road_map_5):
    itinerary = Itinerary(road_map_5)
    drawer = ItineraryDrawer(degrees_to_show_for_single_point=22.3)
    assert drawer._pixels_per_degree(itinerary) == pytest.approx(31.390134)


'''
################################## 

ItineraryDrawer._grid_line_spacing                   

################################## 
'''


def test_itinerarydrawer_grid_line_spacing_returns_float(road_map_1):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_1)
    assert isinstance(drawer._grid_line_spacing(itinerary), float)


def test_itinerarydrawer_grid_line_spacing_as_expected_1(road_map_1):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_1)
    assert drawer._grid_line_spacing(itinerary) == pytest.approx(5.0, abs=1e-10)


def test_itinerarydrawer_grid_line_spacing_as_expected_2(road_map_2):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_2)
    assert drawer._grid_line_spacing(itinerary) == pytest.approx(50.0, abs=1e-10)


def test_itinerarydrawer_grid_line_spacing_as_expected_3(road_map_3):
    drawer = ItineraryDrawer(min_grid_lines=100)
    itinerary = Itinerary(road_map_3)
    assert drawer._grid_line_spacing(itinerary) == pytest.approx(0.005, abs=1e-10)


def test_itinerarydrawer_grid_line_spacing_as_expected_4(road_map_4):
    drawer = ItineraryDrawer(min_grid_lines=100)
    itinerary = Itinerary(road_map_4)
    assert drawer._grid_line_spacing(itinerary) == pytest.approx(0.05, abs=1e-10)


def test_itinerarydrawer_grid_line_spacing_as_expected_single_city(road_map_5):
    drawer = ItineraryDrawer()
    itinerary = Itinerary(road_map_5)
    assert drawer._grid_line_spacing(itinerary) == pytest.approx(0.2, abs=1e-10)


def test_itinerarydrawer_grid_line_spacing_as_expected_single_city_2(road_map_5):
    drawer = ItineraryDrawer(degrees_to_show_for_single_point=20)
    itinerary = Itinerary(road_map_5)
    assert drawer._grid_line_spacing(itinerary) == pytest.approx(2.0, abs=1e-10)


'''
################################## 

ItineraryDrawer._grid_lines                   

################################## 
'''


def test_itinerarydrawer_grid_lines_returns_generator_lat(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    assert isinstance(drawer._grid_lines(itinerary, is_latitude=True), types.GeneratorType)


def test_itinerarydrawer_grid_lines_yields_tuples_lat(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    assert isinstance(next(drawer._grid_lines(itinerary, is_latitude=True)), tuple)


def test_itinerarydrawer_grid_lines_yields_str_and_int_lat(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    for degrees, pixels in drawer._grid_lines(itinerary, is_latitude=True):
        assert isinstance(degrees, str)
        assert isinstance(pixels, int)


def test_itinerarydrawer_grid_lines_right_length_1_lat(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    grid_lines = drawer._grid_lines(itinerary, is_latitude=True)
    assert len(list(grid_lines)) == 5


def test_itinerarydrawer_grid_lines_as_expected_1_lat(road_map_1):
    expected = [('30', 323), ('35', 251), ('40', 178), ('45', 105), ('50', 33)]
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    received = drawer._grid_lines(itinerary, is_latitude=True)
    for (exp_degrees, exp_pixels), (rec_degrees, rec_pixels) in zip(expected, received):
        assert rec_degrees == exp_degrees
        assert rec_pixels == pytest.approx(exp_pixels)


def test_itinerarydrawer_grid_lines_right_length_2_lat(road_map_2):
    itinerary = Itinerary(road_map_2)
    drawer = ItineraryDrawer()
    grid_lines = drawer._grid_lines(itinerary, is_latitude=True)
    assert len(list(grid_lines)) == 3


def test_itinerarydrawer_grid_lines_as_expected_2_lat(road_map_2):
    expected = [('-50', 312), ('0', 184), ('50', 56)]
    itinerary = Itinerary(road_map_2)
    drawer = ItineraryDrawer()
    received = drawer._grid_lines(itinerary, is_latitude=True)
    for (exp_degrees, exp_pixels), (rec_degrees, rec_pixels) in zip(expected, received):
        assert rec_degrees == exp_degrees
        assert rec_pixels == pytest.approx(exp_pixels)


def test_itinerarydrawer_grid_lines_right_length_single_city_lat(road_map_5):
    itinerary = Itinerary(road_map_5)
    drawer = ItineraryDrawer()
    grid_lines = drawer._grid_lines(itinerary, is_latitude=True)
    assert len(list(grid_lines)) == 6


def test_itinerarydrawer_grid_lines_as_expected_single_city_lat(road_map_5):
    expected = [('51.0', 765), ('51.2', 625), ('51.4', 485), ('51.6', 345), ('51.8', 205), ('52.0', 65)]
    itinerary = Itinerary(road_map_5)
    drawer = ItineraryDrawer()
    received = drawer._grid_lines(itinerary, is_latitude=True)
    for (exp_degrees, exp_pixels), (rec_degrees, rec_pixels) in zip(expected, received):
        assert rec_degrees == exp_degrees
        assert rec_pixels == pytest.approx(exp_pixels)


def test_itinerarydrawer_grid_lines_returns_generator_long(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    assert isinstance(drawer._grid_lines(itinerary, is_latitude=False), types.GeneratorType)


def test_itinerarydrawer_grid_lines_yields_tuples_long(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    assert isinstance(next(drawer._grid_lines(itinerary, is_latitude=False)), tuple)


def test_itinerarydrawer_grid_lines_yields_str_and_int_long(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    for degrees, pixels in drawer._grid_lines(itinerary, is_latitude=False):
        assert isinstance(degrees, str)
        assert isinstance(pixels, int)


def test_itinerarydrawer_grid_lines_right_length_1_long(road_map_1):
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    grid_lines = drawer._grid_lines(itinerary, is_latitude=False)
    assert len(list(grid_lines)) == 11


def test_itinerarydrawer_grid_lines_as_expected_1_long(road_map_1):
    expected = [('-120', 46), ('-115', 119), ('-110', 192), ('-105', 264), ('-100', 337), ('-95', 409), ('-90', 482),
                ('-85', 555), ('-80', 627), ('-75', 700), ('-70', 772)]
    itinerary = Itinerary(road_map_1)
    drawer = ItineraryDrawer()
    received = drawer._grid_lines(itinerary, is_latitude=False)
    for (exp_degrees, exp_pixels), (rec_degrees, rec_pixels) in zip(expected, received):
        assert rec_degrees == exp_degrees
        assert rec_pixels == pytest.approx(exp_pixels)


def test_itinerarydrawer_grid_lines_right_length_2_long(road_map_2):
    itinerary = Itinerary(road_map_2)
    drawer = ItineraryDrawer()
    grid_lines = drawer._grid_lines(itinerary, is_latitude=False)
    assert len(list(grid_lines)) == 6


def test_itinerarydrawer_grid_lines_as_expected_2_long(road_map_2):
    expected = [('-100', 48), ('-50', 176), ('0', 304), ('50', 432), ('100', 560), ('150', 688)]
    itinerary = Itinerary(road_map_2)
    drawer = ItineraryDrawer()
    received = drawer._grid_lines(itinerary, is_latitude=False)
    for (exp_degrees, exp_pixels), (rec_degrees, rec_pixels) in zip(expected, received):
        assert rec_degrees == exp_degrees
        assert rec_pixels == pytest.approx(exp_pixels)


def test_itinerarydrawer_grid_lines_right_length_single_city_long(road_map_5):
    itinerary = Itinerary(road_map_5)
    drawer = ItineraryDrawer()
    grid_lines = drawer._grid_lines(itinerary, is_latitude=False)
    assert len(list(grid_lines)) == 6


def test_itinerarydrawer_grid_lines_as_expected_single_city_long(road_map_5):
    expected = [('-0.6', 71), ('-0.4', 211), ('-0.2', 351), ('0.0', 491), ('0.2', 631), ('0.4', 771)]
    itinerary = Itinerary(road_map_5)
    drawer = ItineraryDrawer()
    received = drawer._grid_lines(itinerary, is_latitude=False)
    for (exp_degrees, exp_pixels), (rec_degrees, rec_pixels) in zip(expected, received):
        assert rec_degrees == exp_degrees
        assert rec_pixels == pytest.approx(exp_pixels)
