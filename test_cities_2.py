import pytest

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
            ('Niger', 'Niamey', 13.27, 2.06),
            ('Nigeria', 'Abuja', 9.05, 7.32)]


@pytest.fixture
def length_2():
    return 16


@pytest.fixture
def states_2():
    return ['Mayotte', 'Mexico', 'Micronesia (Federated States of)', 'Moldova, Republic of', 'Mozambique', 'Myanmar',
            'Namibia', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua',
            'Niger', 'Nigeria']


@pytest.fixture
def cities_2():
    return ['Mamoudzou', 'Mexico', 'Palikir', 'Chisinau', 'Maputo', 'Yangon', 'Windhoek', 'Kathmandu', 'Amsterdam',
            'Willemstad', 'Noumea', 'Wellington', 'Managua', 'Niamey', 'Abuja']


@pytest.fixture
def latitudes_2():
    return [-12.48, 19.2, 6.55, 47.02, -25.58, 16.45, -22.35, 27.45, 52.23, 12.05, -22.17, -41.19, 12.06, 13.27, 9.05]


@pytest.fixture
def longitudes_2():
    return [45.14, -99.1, 158, 28.5, 32.32, 96.2, 17.04, 85.2, 4.54, -69, 166.3, 174.4, -86.2, 2.06, 7.32]


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
