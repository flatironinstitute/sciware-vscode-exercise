import sys


def gen_data(N: int):
    print(f'Generating {N} data points...')
    pass


def save_data(data, fn):
    print(f'Saving data points to {fn}...')
    pass


def main(N: int):
    data = gen_data(N)
    save_data(data, 'data.csv')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python generate_data.py [N]')
        sys.exit(1)
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    else:
        N = 100
    main(N)
