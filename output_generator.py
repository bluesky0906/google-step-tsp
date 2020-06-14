from common import format_tour, read_input

import solver_mysolution
# 進捗バー表示
from tqdm import tqdm

CHALLENGES = 7


def generate_sample_output():
    for i in tqdm(range(CHALLENGES)):
        print(i)
        cities = read_input(f'input_{i}.csv')
        tour = solver_mysolution.solve(cities)
        with open(f'output_{i}.csv', 'w') as f:
            f.write(format_tour(tour) + '\n')


if __name__ == '__main__':
    generate_sample_output()
