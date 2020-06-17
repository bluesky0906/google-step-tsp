from common import format_tour, read_input

import solver_NN
import solver_DNN
import solver_2opt
import solver_1_5opt
import solver_comb

CHALLENGES = 7


def choose_mode():
    origin_solver = None
    print('Please choose mode')
    # モードを選ぶ
    mode = input()
    if mode == 'NN':
        solver = solver_NN
    elif mode == 'DNN':
        solver = solver_DNN
    elif mode == 'NN_2opt':
        solver = solver_2opt
        origin_solver = solver_NN
    elif mode == 'DNN_2opt':
        solver = solver_2opt
        origin_solver = solver_DNN
    elif mode == 'NN_1_5opt':
        solver = solver_1_5opt
        origin_solver = solver_NN
    elif mode == 'NN_comb':
        solver = solver_comb
        origin_solver = solver_NN
    elif mode == 'DNN_comb':
        solver = solver_comb
        origin_solver = solver_NN
    else:
        exit(1)
    return (solver, mode, origin_solver)


def generate_sample_output(solver, name, origin_solver):
    for i in range(CHALLENGES):
        print(i)
        cities = read_input(f'input_{i}.csv')
        # 改善法も実行
        if origin_solver:
            tour = origin_solver.solve(cities)
            tour = solver.solve(cities, tour)
        else:
            tour = solver.solve(cities)
        with open(f'my_output/{name}_{i}.csv', 'w') as f:
            f.write(format_tour(tour) + '\n')


if __name__ == '__main__':
    solver, name, origin_solver = choose_mode()
    generate_sample_output(solver, name, origin_solver)
