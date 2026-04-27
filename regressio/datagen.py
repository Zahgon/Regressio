import numpy as np
import matplotlib.pyplot as plt


def generate_random_walk(n, noise=1, plot=False):
    """Given a number n, returns a random walk sample.

    Args
    ---------
        n: the number of data points in the sample
        noise: random walk step size
        plot: boolean to plot result or not

    Returns
    ---------
        x: x values of the data sample
        y: y values of the data sample

    Example
    ---------
    >>> from regressio.models import linear_regression
    >>> from regressio.datagen import generate_random_walk
    >>> x, y = generate_random_walk(100)
    """
    raise NotImplementedError


def generate_isotonic_sample(n, noise=1, plot=False):
    """Given a number n, generates an increasing sample.
    For a strictly increasing sample set noise to 0.

    Args
    ---------
        n: the number of data points in the sample
        noise: random walk step size
        plot: boolean to plot result or not

    Returns
    ---------
        x: x values of the data sample
        y: y values of the data sample

    Example
    ---------
    >>> from regressio.models import linear_regression
    >>> from regressio.datagen import generate_isotonic_sample
    >>> x, y = generate_isotonic_sample(100)
    """

    def gen(x):
        raise NotImplementedError

    raise NotImplementedError


def main():
    return


if __name__ == "__main__":
    main()
