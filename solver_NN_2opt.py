import sys
import math
import random
# NN + 改善アルゴリズム 2-opt
# 2つの辺ab, cdを考えて、
# ab + cd よりも ac + bdの方が短ければ
# 入れ替える
from common import print_tour, read_input, get_all_distance, get_tour_length
import solver_NN


def get_negibor(N):
    neighbor = int(10 * math.log2(N))
    if neighbor > N:
        neighbor = N//2
    return neighbor


# ある都市の近傍都市を選ぶ
def get_neighbor_city(dist_i):
    N = len(dist_i)
    sort_dist_i = sorted(dist_i)
    # 近傍の求め方
    neighbor = get_negibor(N)
    neighbor_city = set([dist_i.index(city)
                         for city in sort_dist_i][:neighbor])
    return neighbor_city


# ab + cd よりも ac + bdの方が短ければ交換
def swap_path(tour, i, j, dist):
    N = len(tour)
    A, B, C, D = tour[i], tour[i+1], tour[j], tour[(j+1) % N]
    if dist[A][B] + dist[C][D] > dist[A][C] + dist[B][D]:
        tour[i+1:j+1] = reversed(tour[i+1:j+1])


# 近傍都市だけ探索しようとしたが、時間があまり削減されなかったため不採用
def improve_tour2(dist, tour):
    N = len(tour)
    can_improve = True
    while can_improve:
        original_length = get_tour_length(tour, dist)
        for i in range(N):
            # 計算量削減のため近傍都市(かつ経路でiより後ろの都市)のみ探索
            neighbor_city = get_neighbor_city(dist[i])
            remaining_tour = set(tour[i+1:])
            neighbor_city_index = [
                tour.index(city) for city in neighbor_city & remaining_tour]
            for j in neighbor_city_index:
                # for j in range(i+2, N):
                swap_path(tour, i, j, dist)
        if get_tour_length(tour, dist) >= original_length:
            can_improve = False


def improve_tour(dist, tour):
    N = len(tour)
    can_improve = True
    while can_improve:
        original_length = get_tour_length(tour, dist)
        for i in range(N):
            # 計算量削減のため近傍都市(かつ経路でiより後ろの都市)のみ探索
            neighbor_city = get_neighbor_city(dist[i])
            remaining_tour = set(tour[i+1:])
            neighbor_city_index = [
                tour.index(city) for city in neighbor_city & remaining_tour]
            for j in neighbor_city_index:
                # for j in range(i+2, N):
                swap_path(tour, i, j, dist)
        if get_tour_length(tour, dist) >= original_length:
            can_improve = False


def solve_each(dist, start_city=0):
    tour = solver_NN.solve_each(dist, start_city)
    improve_tour(dist, tour)
    return tour


def solve(cities):
    N = len(cities)
    start_points = range(N)
    # challenge4からはランダムな点で実行
    if N >= 2048:
        start_points = [random.randint(0, N) for _ in range(600)]
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
