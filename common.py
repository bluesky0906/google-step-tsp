import math


def read_input(filename):
    with open(filename) as f:
        cities = []
        for line in f.readlines()[1:]:  # Ignore the first line.
            xy = line.split(',')
            cities.append((float(xy[0]), float(xy[1])))
        return cities


def format_tour(tour):
    return 'index\n' + '\n'.join(map(str, tour))


def print_tour(tour):
    print(format_tour(tour))


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def get_all_distance(cities):
    N = len(cities)
    dist = [[float('inf')] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(
                cities[i], cities[j])
    return dist


# 経路長
def get_tour_length(tour, dist):
    N = len(tour)
    length = 0
    for i in range(N):
        length += dist[tour[i]][tour[(i+1) % N]]
    return length
