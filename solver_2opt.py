import sys

# 改善アルゴリズム 2-opt
# 2つの辺ab, cdを考えて、
# ab + cd よりも ac + bdの方が短ければ
# 入れ替える
from common import print_tour, read_input
import solver_NN


def solve(cities, tour=None):
    N = len(cities)

    if not tour:
        tour = solver_NN.solve(cities)

    # 全ての距離
    dist = solver_NN.all_distance(cities)

    while True:
        count = 0
        for i in range(N-2):
            a = tour[i]
            b = tour[i+1]
            ab = dist[a][b]
            for j in range(i+2, N):
                c = tour[j]
                if j == N - 1:
                    d = tour[0]
                else:
                    d = tour[j+1]
                cd = dist[c][d]
                ac = dist[a][c]
                bd = dist[b][d]
                # 入れ替え
                if ab + cd > ac + bd:
                    tour[i+1], tour[j] = tour[j], tour[i+1]
                    count += 1
        if not count:
            break

    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
