import sys

# NN + 改善アルゴリズム 1.5-opt
# ある隣接した都市(A),(B)と、単一の都市(C)を選択する。 都市(C)の巡回路上での前の都市を(P)、次の都市を(N)とする。
# もし、都市間の距離 AC + CB + PNが AB + PC + CN よりも小さいならば
# PとNを繋ぎ、CをAーB間に挿入する

from common import print_tour, read_input, get_tour_length, get_all_distance
import solver_NN


# もし、都市間の距離 AC + CB + PNが AB + PC + CN よりも小さいならば
# PとNを繋ぎ、CをAーB間に挿入する
def swap_path(tour, i, j, dist):
    A, B = tour[i], tour[i+1]
    C, P, N = tour[j], tour[j-1], tour[(j+1) % len(tour)]
    # ac + cb + pn
    dis1 = dist[A][C] + dist[C][B] + dist[P][N]
    # ab + pc + cn
    dis2 = dist[A][B] + dist[P][C] + dist[C][N]
    if dis1 < dis2:
        tour.remove(C)
        tour.insert(i+1, C)


def improve_tour(dist, tour):
    N = len(tour)
    can_improve = True
    while can_improve:
        original_length = get_tour_length(tour, dist)
        for i in range(N):
            for j in range(i+3, N):
                swap_path(tour, i, j, dist)
        if get_tour_length(tour, dist) >= original_length:
            can_improve = False


def solve_each(dist, start_city=0):
    tour = solver_NN.solve_each(dist, start_city)
    improve_tour(dist, tour)
    return tour


def solve(cities):
    N = len(cities)

    # 全ての距離
    dist = get_all_distance(cities)
    tours = []
    # スタート地点を変えて実行する
    for i in range(N):
        tours.append(solve_each(dist, i))
    tours_length = [get_tour_length(tour, dist) for tour in tours]
    shortest_tour = tours[tours_length.index(min(tours_length))]
    # 一番短い経路を返す
    return shortest_tour
    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
