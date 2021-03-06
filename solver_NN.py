import sys

# NearestNeighbor法
# greedyと一緒で、探索を始める都市を指定することができる

from common import print_tour, read_input, get_all_distance, get_tour_length


def solve_each(dist, start_city=0):
    N = len(dist[0])

    unvisited_cities = set(range(0, N))
    unvisited_cities.remove(start_city)
    tour = [start_city]
    current_city = start_city

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour


def solve(cities):
    N = len(cities)
    dist = get_all_distance(cities)
    tours = []
    # スタート地点を変えて実行する
    for i in range(N):
        tours.append(solve_each(dist, i))
    tours_length = [get_tour_length(tour, dist) for tour in tours]
    shortest_tour = tours[tours_length.index(min(tours_length))]
    # 一番短い経路を返す
    return shortest_tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
