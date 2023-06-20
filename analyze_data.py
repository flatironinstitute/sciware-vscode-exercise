import sys


def load_data(fn):
    print(f'Loading data from {fn}...')
    pass


def fit_line(data):
    print(f'Saving data points to {fn}...')
    pass


def plot(data, slope, intercept):
    pass


def main(fn: str):
    data = load_data(fn)
    line = fit_line(data)
    plot(data, line)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python analyze_data.py FILE')
        sys.exit(1)
    main(sys.argv[1])
