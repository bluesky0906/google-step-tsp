import sys
import random

# NN + 改善アルゴリズム 2-opt + oropt法
# NN + 2-opt + oropt法を探索のスタート位置を変えて実行

from common import print_tour, read_input, get_all_distance, get_tour_length
import solver_NN
import solver_NN_2opt
import solver_NN_oropt


def solve_each(dist, start_city):
    tour = solver_NN.solve_each(dist, start_city)
    solver_NN_2opt.improve_tour(dist, tour)
    solver_NN_oropt.improve_tour(dist, tour)
    return tour


def solve(cities):
    N = len(cities)
    start_points = range(N)
    # challenge6はランダムな点一つで実行
    if N >= 2048:
        start_points = [random.randint(0, N-1)]
    # 全ての距離
    dist = get_all_distance(cities)
    tours = []
    # スタート地点を変えて実行する
    for i in start_points:
        tours.append(solve_each(dist, i))
    tours_length = [get_tour_length(tour, dist) for tour in tours]
    shortest_tour = tours[tours_length.index(min(tours_length))]
    # 一番短い経路を返す
    return shortest_tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
