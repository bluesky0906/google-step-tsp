import sys
import random

# 改善アルゴリズム 2-opt + oropt法
# 点を選んでそれを改善し、最終的に総距離の短いものを選ぶ

from common import print_tour, read_input, get_all_distance, get_tour_length
import solver_NN
import solver_NN_2opt
import solver_NN_oropt


def improve_tour(dist, tour):
    solver_NN_2opt.improve_tour(dist, tour)
    solver_NN_oropt.improve_tour(dist, tour)


def solve_each(dist, start_city=0):
    tour = solver_NN.solve_each(dist, start_city)
    improve_tour(dist, tour)
    return tour


def solve(cities):
    N = len(cities)
    start_points = range(N)
    # challenge4からはランダムな点で実行
    if N >= 128:
        start_points = [random.randint(0, N) for _ in range(70)]
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
