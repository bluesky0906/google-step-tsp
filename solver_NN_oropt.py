import sys

# NN + 改善アルゴリズム Or-opt
# ある都市Aを他の辺に挿入したとき経路が改善されるならば
# 入れ替える

from common import print_tour, read_input, get_tour_length, get_all_distance
import solver_NN


def swap_path(tour, i, j, dist):
    A = tour[i]
    swaped_tour = tour.copy()
    swaped_tour.remove(A)
    swaped_tour.insert(j, A)
    if get_tour_length(swaped_tour, dist) > get_tour_length(tour, dist):
        tour = swaped_tour


def improve_tour(dist, tour):
    N = len(tour)
    can_improve = True
    while can_improve:
        original_length = get_tour_length(tour, dist)
        for i in range(N):
            for j in range(N):
                swap_path(tour, i, j, dist)
        if get_tour_length(tour, dist) >= original_length:
            can_improve = False


def improve_tour2(dist, tour):
    N = len(tour)
    can_improve = True
    while can_improve:
        original_length = get_tour_length(tour, dist)
        for i in range(N):
            # 閾値を超えている都市にだけ適用
            if dist[i][(i+1) % N] + dist[(i+1) % N][(i+2) % N] < 1500:
                continue
            for j in range(N):
                swap_path(tour, i, j, dist)
        if get_tour_length(tour, dist) >= original_length:
            can_improve = False


def solve_each(dist, start_city=0):
    tour = solver_NN.solve_each(dist, start_city)
    improve_tour2(dist, tour)
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
