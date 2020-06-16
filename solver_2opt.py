import sys

# 改善アルゴリズム 2-opt

from common import print_tour, read_input
import solver_greedy


def solve(cities, solver=solver_greedy):
    # 何かしらのアルゴリズムで解く
    tours = solver.solve(cities)

    N = len(tours)
    can_swap = True
    count = 0
    while can_swap:
        can_swap = False
        # 2つの辺を考えて、入れ替えた方が2つの辺の距離の和が短くなる場合は、入れ替える
        for i in range(count, N - 2):
            dis1 = solver_greedy.distance(
                cities[tours[i]], cities[tours[i+1]])
            for j in range(i+2, N):
                if j == N - 1:
                    dis2 = solver_greedy.distance(
                        cities[tours[j]], cities[tours[0]])
                    dis3 = solver_greedy.distance(
                        cities[tours[i]], cities[tours[j]])
                    dis4 = solver_greedy.distance(
                        cities[tours[i+1]], cities[tours[0]])
                else:
                    dis2 = solver_greedy.distance(
                        cities[tours[j]], cities[tours[j+1]])
                    dis3 = solver_greedy.distance(
                        cities[tours[i]], cities[tours[j]])
                    dis4 = solver_greedy.distance(
                        cities[tours[i+1]], cities[tours[j+1]])
                # 入れ替え
                if dis1 + dis2 > dis3 + dis4:
                    can_swap = True
                    tours[i+1], tours[j] = tours[j], tours[i+1]
                    count = i
                    break
            if can_swap:
                break

    return tours


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
