'''
analyze_data.py

Loads (x,y) data points from a given file, fits a line, and plots the results.
'''

import sys

import numpy as np
import numpy.typing as npt

def load_data(fn: str) -> npt.NDArray[np.float64]:
    print(f'Loading data from {fn}...')

    data = np.loadtxt(fn)
    return data


def fit_line(data) -> Tuple[float,float]:
    print('Fitting line...')
    pass


def plot(data, slope, intercept):
    print('Plotting fit...')
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
