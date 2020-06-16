import shutil

from my_output_generator import choose_mode

# どの自分の解放をoutputにするか選ぶ

CHALLENGES = 7


def generate_sample_output(name):
    for i in range(CHALLENGES):
        shutil.copyfile(f'my_output/{name}_{i}.csv', f'output_{i}.csv')


if __name__ == '__main__':
    _, name, _ = choose_mode()
    generate_sample_output(name)
