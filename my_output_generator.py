from common import format_tour, read_input

import solver_NN
import solver_DNN
import solver_2opt

CHALLENGES = 7


def choose_mode():
    origin_solver = None
    print('Please choose mode')
    # モードを選ぶ
    mode = input()
    if mode == 'NN':
        solver = solver_NN
        name = mode
    elif mode == 'DNN':
        solver = solver_DNN
        name = mode
    elif mode == 'NN_2opt':
        solver = solver_2opt
        origin_solver = solver_NN
        name = mode
    else:
        exit(1)
    return (solver, name, origin_solver)


def generate_sample_output(solver, name, origin_solver):
    for i in range(CHALLENGES):
        print(i)
        cities = read_input(f'input_{i}.csv')
        # 改善法も実行
        if origin_solver:
            tour = solver.solve(cities, origin_solver)
        else:
            tour = solver.solve(cities)
        with open(f'my_output/{name}_{i}.csv', 'w') as f:
            f.write(format_tour(tour) + '\n')


if __name__ == '__main__':
    solver, name, origin_solver = choose_mode()
    generate_sample_output(solver, name, origin_solver)
