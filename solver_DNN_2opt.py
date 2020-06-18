import sys

# DNN + 改善アルゴリズム 2-opt
# 2つの辺ab, cdを考えて、
# ab + cd よりも ac + bdの方が短ければ
# 入れ替える
from common import print_tour, read_input, get_all_distance
import solver_NN_2opt
import solver_DNN


def solve(cities):
    dist = get_all_distance(cities)

    tour = solver_DNN.solve(cities)
    solver_NN_2opt.improve_tour(dist, tour)
    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
