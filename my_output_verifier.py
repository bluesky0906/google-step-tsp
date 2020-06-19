#!/usr/bin/env python3
import math
import shutil
from common import read_input

# それぞれの点数を表示
# 一番いいスコアを表示用にする

CHALLENGES = 7
PREFIXES = ('NN', 'DNN', 'NN_2opt', 'DNN_2opt', 'NN_comb1',
            'DNN_comb1', 'NN_comb2')


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def get_path_length(output_file, cities):
    N = len(cities)
    path_length = None
    try:
        f = open(output_file)
    except OSError as e:
        print(e)
    else:
        lines = f.readlines()
        assert lines[0].strip() == 'index'
        tour = [int(i.strip()) for i in lines[1:N + 1]]
        assert set(tour) == set(range(N))
        path_length = sum(
            distance(cities[tour[i]], cities[tour[(i + 1) % N]])
            for i in range(N))
    return path_length


def verify_output():
    for challenge_number in range(CHALLENGES):
        print(f'Challenge {challenge_number}')
        cities = read_input(f'input_{challenge_number}.csv')
        output_files = []
        lengths = []
        for output_prefix in PREFIXES:
            output_file = f'my_output/{output_prefix}_{challenge_number}.csv'
            path_length = get_path_length(output_file, cities)
            if path_length:
                output_files.append(output_file)
                lengths.append(path_length)
                print(f'{output_prefix:16}: {path_length:>10.2f}')
        best_output = output_files[lengths.index(min(lengths))]
        print(best_output)
        shutil.copyfile(f'{best_output}', f'output_{challenge_number}.csv')
        print()


if __name__ == '__main__':
    verify_output()
