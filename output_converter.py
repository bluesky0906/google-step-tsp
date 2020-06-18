import shutil

from output_generator import choose_mode

# my_output/ 以下のファイルを解法として表示するか

CHALLENGES = 7


def generate_sample_output(name):
    for i in range(CHALLENGES):
        shutil.copyfile(f'my_output/{name}_{i}.csv', f'output_{i}.csv')


if __name__ == '__main__':
    _, name = choose_mode()
    generate_sample_output(name)
