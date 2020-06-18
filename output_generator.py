from common import format_tour, read_input

import solver_NN
import solver_DNN
import solver_NN_2opt
import solver_DNN_2opt
import solver_NN_1_5opt
import solver_NN_comb1

# outputファイルをmy_outputに出力

CHALLENGES = 7


def choose_mode():
    print('Please choose mode')
    # モードを選ぶ
    mode = input()
    if mode == 'NN':
        solver = solver_NN
    elif mode == 'DNN':
        solver = solver_DNN
    elif mode == 'NN_2opt':
        solver = solver_NN_2opt
    elif mode == 'DNN_2opt':
        solver = solver_DNN_2opt
    elif mode == 'NN_1_5opt':
        solver = solver_NN_1_5opt
    elif mode == 'DNN_1_5opt':
        solver = solver_NN_1_5opt
    elif mode == 'NN_comb1':
        solver = solver_NN_comb1
    else:
        exit(1)
    return (solver, mode)


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
