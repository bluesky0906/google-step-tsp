import sys

# DivisionNearestNeighbor法

import solver_NN
from common import print_tour, read_input, get_all_distance


# 与えられた2点から直線を返す
# (x=数値) or (y=mx+n)
def make_linear_function(city1, city2):
    line = {}
    # y座標に垂直なグラフ
    if city1[0] == city2[0]:
        line['x'] = city1[0]
    else:
        line['m'] = (city1[1] - city2[1])/(city1[0] - city2[0])
        line['n'] = city1[1] - (line['m'] * city1[0])
    return line


def solve(cities):
    N = len(cities)

    # 最も離れた都市を求める
    dist = get_all_distance(cities)
    max_value = 0
    max_city1 = 0
    for i in range(N):
        local_max = max(dist[i])
        if max_value < local_max:
            max_value = local_max
            max_city1 = i
    max_city2 = dist[max_city1].index(max_value)
    # 2つの都市を通る直線で２つに分ける
    line = make_linear_function(cities[max_city1], cities[max_city2])
    group1 = [max_city1]
    group2 = [max_city2]
    # yに垂直な直線の時(右か左かで分ける)
    if 'x' in line:
        for i in range(N):
            if i in {max_city1, max_city2}:
                continue
            # 直線よりも左側に点がある時
            if cities[i][0] < line['x']:
                group1.append(i)
            # 直線よりも右側に点がある時
            else:
                group2.append(i)
    # 上か下かで分ける
    else:
        for i in range(N):
            if i in {max_city1, max_city2}:
                continue
            # 直線よりも下側に点がある時
            if cities[i][1] < line['m']*cities[i][0] + line['n']:
                group1.append(i)
            # 直線よりも上側に点がある時
            else:
                group2.append(i)

    # max_city1を開始都市として、group1に対してNN法を行う
    group1_cities = [cities[city] for city in group1]
    group1_dist = get_all_distance(group1_cities)
    tour1 = solver_NN.solve_each(group1_dist, 0)
    # max_city2を開始都市として、group2に対してNN法を行う
    group2_cities = [cities[city] for city in group2]
    group2_dist = get_all_distance(group2_cities)
    tour2 = solver_NN.solve_each(group2_dist, 0)
    # それぞれをつなげる
    tour = [group1[i] for i in tour1] + [group2[i] for i in tour2]
    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
