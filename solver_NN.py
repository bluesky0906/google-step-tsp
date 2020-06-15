# NearestNeighbor法

import sys

import solver_greedy
from common import print_tour, read_input


def solve(cities):
    N = len(cities)
    # まだ探していない都市
    unvisited_cities = set(range(N))

    tour = [0]
    unvisited_cities.remove(0)

    while unvisited_cities:
        dist = [float('inf')] * N
        for i, city in enumerate(unvisited_cities):
            current_city = tour[-1]
            dist[city] = solver_greedy.distance(
                cities[city], cities[current_city])
        next_city = dist.index(min(dist))
        tour.append(next_city)
        unvisited_cities.remove(next_city)
    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
