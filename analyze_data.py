'''
analyze_data.py

Loads (x,y) data points from a given file, fits a line, and plots the results.
'''

import sys

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt


def load_data(fn: str) -> npt.NDArray[np.float64]:
    print(f'Loading data from {fn}...')

    data = np.loadtxt(fn)
    return data


def fit_line(data: npt.NDArray[np.float64]) -> tuple[float,float]:
    print('Fitting line...')
    slope = ((data[0] - data[0].mean())*(data[1] - data[1].mean())).sum() \
        / ((data[0] - data[0].mean())**2).sum()
    intercept = data[1].mean() - slope * data[0].mean()

    return (slope,intercept)


def plot(data: npt.NDArray[np.float64],
         slope: float,
         intercept: float,
         ):
    print('Plotting fit...')
    plt.plot(data[0], data[1], 'x')
    pltx = np.linspace(0, 1, 100)
    plt.plot(pltx, pltx*slope + intercept)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig('plot.png')


def main(fn: str):
    ### YOUR CODE HERE ###
    ### Call load_data(), fit_line(), and plot()
    pass


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python analyze_data.py FILE')
        sys.exit(1)
    main(sys.argv[1])
