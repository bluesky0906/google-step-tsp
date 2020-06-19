import sys

# 改善アルゴリズム 2-opt + oropt法

from common import print_tour, read_input, get_all_distance
import solver_NN_2opt
import solver_NN_oropt


def solve(cities):
    # 全ての距離
    dist = get_all_distance(cities)
    tour = solver_NN_2opt.solve(cities)
    solver_NN_oropt.improve_tour(dist, tour)
    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
