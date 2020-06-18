import sys

# DNN + 改善アルゴリズム 1.5-opt
# ある隣接した都市(A),(B)と、単一の都市(C)を選択する。 都市(C)の巡回路上での前の都市を(P)、次の都市を(N)とする。
# もし、都市間の距離 AC + CB + PNが AB + PC + CN よりも小さいならば
# PとNを繋ぎ、CをAーB間に挿入する

from common import print_tour, read_input, get_all_distance
import solver_NN_1_5opt
import solver_DNN


def solve(cities):
    dist = get_all_distance(cities)

    tour = solver_DNN.solve(cities)
    tour = solver_NN_1_5opt.improve_tour(dist, tour)
    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
