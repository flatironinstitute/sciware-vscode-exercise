'''
generate_data.py

Generates N (x,y) data points that follow a line, with Gaussian noise.
The data points are written to a CSV file.
'''

import sys

import numpy as np
import numpy.typing as npt


def gen_data(N: int,
             slope: float = 2.0,
             intercept: float = 1.0,
             sigma: float = 0.1,
             ) -> npt.NDArray[np.float64]:
    print(f'Generating {N} data points...')

    ### YOUR CODE HERE ###
    ### Generate N linearly spaced data points between 0 and 1 using np.linspace()
    # X = ???

    rng = np.random.default_rng()
    ### YOUR CODE HERE ###
    ### Generate normally-distributed noise with a mean of using rng.normal()
    # sigma = ???

    Y = slope*X + intercept + sigma

    data = np.vstack((X,Y))
    return data


def save_data(data: npt.NDArray[np.float64],
              fn: str,
              ):
    print(f'Saving data points to {fn}...')

    ### YOUR CODE HERE ###
    ### Save the `data` array as a text file using Numpy's `np.savetxt()`
    # np.savetxt(???)


def main(N: int):
    # data = gen_data(N)
    # save_data(data, 'data.csv')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python generate_data.py [N]')
        sys.exit(1)
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    else:
        N = 100
    main(N)
