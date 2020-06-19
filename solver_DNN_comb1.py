import sys

# 改善アルゴリズム 2-opt + oropt法

from common import print_tour, read_input, get_all_distance
import solver_DNN
import solver_NN_2opt
import solver_NN_oropt


def solve(cities):
    N = len(cities)
    # 全ての距離
    dist = get_all_distance(cities)
    if N == 2048:
        with open('my_output/DNN_2opt_6.csv') as f:
                lines = f.readlines()
                assert lines[0].strip() == 'index'
                tour = [int(i.strip()) for i in lines[1:N + 1]]
    else:
        tour = solver_DNN.solve(cities)
    solver_NN_2opt.improve_tour(dist, tour)
    # challenge4からは閾値ありで実行
    if N >= 128:
        solver_NN_oropt.improve_tour2(dist, tour)
    else:
        solver_NN_oropt.improve_tour(dist, tour)
    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
