import sys

# NN + 改善アルゴリズム 2-opt
# 2つの辺ab, cdを考えて、
# ab + cd よりも ac + bdの方が短ければ
# 入れ替える
from common import print_tour, read_input, get_all_distance, get_tour_length
import solver_NN


# ab + cd よりも ac + bdの方が短ければ交換
def swap_path(tour, i, j, dist):
    N = len(tour)
    A, B, C, D = tour[i], tour[i+1], tour[j], tour[(j+1) % N]
    if dist[A][B] + dist[C][D] > dist[A][C] + dist[B][D]:
        tour[i+1:j+1] = reversed(tour[i+1:j+1])


def improve_tour(dist, tour):
    N = len(tour)
    can_improve = True
    while can_improve:
        original_length = get_tour_length(tour, dist)
        for i in range(N):
            for j in range(i+2, N):
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
