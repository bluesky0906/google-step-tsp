from common import format_tour, read_input

import solver_NN
import solver_NN_2opt

CHALLENGES = 7


def choose_mode():
    print('Please choose mode')
    # モードを選ぶ
    mode = input()
    if mode == 'NN':
        solver = solver_NN
        name = mode

    elif mode == 'NN_2opt':
        solver = solver_NN_2opt
        name = mode
    else:
        exit(1)
    return (solver, name)


def generate_sample_output(solver, name):
    for i in range(CHALLENGES):
        print(i)
        cities = read_input(f'input_{i}.csv')
        tour = solver.solve(cities)
        with open(f'my_output/{name}_{i}.csv', 'w') as f:
            f.write(format_tour(tour) + '\n')


if __name__ == '__main__':
    solver, name = choose_mode()
    generate_sample_output(solver, name)
