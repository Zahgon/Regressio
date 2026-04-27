import numpy as np
import matplotlib.pyplot as plt
from statistics import NormalDist

class smoother(object):
    """
    Abstract class for all smoothing models. This class can not be instantiated 
    directly and is strictly a parent class.  

    Attributes
    ---------
        residuals (arr[int | float]): stored residuals
        smoothed_ys (arr[int | float]): stored smoothed values
        zscore (dict): dictionary of confidence z-scores

    Raises
    ---------
        Exception: if smoother is instantiated directly
    """
    
    def __init__(self):
        raise NotImplementedError
    
    def get_confidence_interval(self, confidence=0.95):
        """
        Function that bootstraps residuals for standard deviation, and returns a
        band size.
        """
        pass

    def check_instantiation_type(self):
        """
        Function to enforce abstract class type.
        """
        pass

    def check_ci_input(self, ci):
        '''
        Validates confidence interval input.
        '''
        pass

class linear_regression(smoother):
    """Linear regression model. 

    A regression model that models the relationship between a variable x 
    and a variable y using an nth degree polynomial. Degree > 10 is 
    numerically unstable in the OLS calculation. Consider using a natural 
    cubic spline if a degree 10 polynomial underfits.

    Args
    ---------
        degree: the degree of the polynomial

    Attributes
    ---------
        degree (int): the degree of the polynomial
        ws (arr[int]): stored model weights
        range (arr[float]): stored range of the x-values
        rmse (float): stored RMSE from model training
        + attributes from smoother class

    Raises
    ---------
        TypeError: if degree is not a number
        ValueError: if degree is < 0 or > 10

    Example
    ---------
    >>> from regressio.models import linear_regression
    >>> from regressio.datagen import generate_random_walk
    >>> x, y = generate_random_walk(100)
    >>> model = linear_regression(degree=5)
    >>> model.fit(x, y, plot=True, confidence_interval=0.95)
    """

    def __init__(self, degree):
        raise NotImplementedError

    def fit(self, x, y, plot=False, confidence_interval=False):
        '''
        Given input arrays x and y. Fits the model.
        '''
        pass

    def predict(self, x):
        '''
        Given an input array x. Make predictions.
        '''
        pass

    def OLS(self, x, y):
        # Construct features 1, x^1, x^2 .. x^n
        pass

    def MSE(self, x, y):
        '''
        Mean squared error helper function.
        '''
        pass

    def plot_model(self, x, y, MSE, confidence_interval=False):
        '''
        Plot the models hypothetical predictions, MSE, and true data points.
        '''
        pass

    @staticmethod
    def check_degree_input(degree):
        '''
        Validate degree input.
        '''
        pass

class ridge_regression(linear_regression):
    """Ridge regression model.

    Child of the linear_regression class. Differs in that a penalty
    term is added. This penalty term penalizes large squared model 
    weights and reduces the likelihood of overfitting.

    Args
    ---------
        alpha: the magnitude of the penalty term
        degree: the degree of the polynomial

    Attributes
    ---------
        alpha: the magnitude of the penalty term
        + attributes from linear_regression class

    Raises
    ---------
        TypeError: if knots is not a number
        ValueError: if alpha <= 0

    Example
    ---------
    >>> from regressio.models import ridge_regression
    >>> from regressio.datagen import generate_random_walk
    >>> x, y = generate_random_walk(100)
    >>> model = ridge_regression(degree=5, alpha=0.5)
    >>> model.fit(x, y, plot=True, confidence_interval=0.95)
    
    Reference
    ----------
    Li, Bao, (2022). Stat 508: Applied Data Mining, Statistical 
    Learning: Stat Online. PennState: Statistics Online Courses, 
    online.stat.psu.edu/stat508, Accessed July 2022.
    """

    def __init__(self, degree, alpha=0.1):
        raise NotImplementedError

    def OLS(self, x, y):
        # Construct features 1, x^1, x^2 .. x^n
        pass

    @staticmethod
    def check_alpha_input(alpha):
        '''
        Validate alpha input.
        '''
        pass

class linear_spline(smoother):
    """Linear spline model (aka. piecewise simple linear regression).

    A linear interpolation model that fits a simple linear regression model 
    to a variable x and a variable y, in 2 or more segments. The function in 
    each segment is estimated using ordinary least squares. Values that fall 
    outside the range of the training data are predicted as endpoint 
    values.

    Args
    ---------
        knots: number of linear segments + 1

    Attributes
    ---------
        knots (int): the degree of the polynomial
        slopes (arr[float]): stores piecewise linear model slopes
        last_binvals (arr[float]): stores last y-value of each bin
        knot_vals (arr[float]): stores each knot value
        + attributes from smoother class

    Raises
    ---------
        TypeError: if knots is not a number
        ValueError: if knots < 2

    Example
    ---------
    >>> from regressio.models import linear_spline
    >>> from regressio.datagen import generate_random_walk
    >>> x, y = generate_random_walk(100)
    >>> model = linear_spline(knots=10)
    >>> model.fit(x, y, plot=True, confidence_interval=0.90)
    """

    def __init__(self, knots):
        raise NotImplementedError
        
    def fit(self, x, y, plot=False, confidence_interval=False):
        '''
        Given input arrays x and y. Fits the model.
        '''
        pass

    def predict(self, x):
        '''
        Given a 1-dimenional numpy array, make predictions.
        '''
        pass
        
    def OLS_linear_spline(self, x, y, first=False):
        '''
        Modified OLS. Intercept is constrained for all bins except for the first.
        '''
        pass
        
    def plot_model(self, x, y, confidence_interval=False):
        '''
        Plots the models hypothetical predictions, MSE, and true data points.
        '''
        pass

    @staticmethod
    def check_bin(i, bin_x):
        '''
        Checks each bin to validate before OLS calculation.
        '''
        pass
            
    @staticmethod
    def line(x, slope, intercept):
        '''
        Simple line function.
        '''
        pass

    @staticmethod
    def check_knots_input(knots):
        '''
        Validates input knot parameter.
        '''
        pass

class isotonic_regression(linear_spline):
    """Isotonic regression model (strictly increasing linear spline).

    Child of the linear_spline class. Differs in that the slope
    of each piecewise model must be greater than or equal to 0.

    Args
    ---------
        knots: number of linear segments + 1

    Attributes
    ---------
        knots (int): the degree of the polynomial
        slopes (arr[float]): stores piecewise linear model slopes
        last_binvals (arr[float]): stores last y-value of each bin
        knot_vals (arr[float]): stores each knot value
        + attributes from smoother class

    Raises
    ---------
        TypeError: if knots is not a number
        ValueError: if knots < 2

    Example
    ---------
    >>> from regressio.models import isotonic_regression
    >>> from regressio.datagen import generate_isotonic_sample
    >>> x, y = generate_isotonic_sample(100)
    >>> model = isotonic_regression(knots=12)
    >>> model.fit(x, y, plot=True, confidence_interval=0.99)
    """
    def __init__(self, knots):
        raise NotImplementedError

    def fit(self, x, y, plot=False, confidence_interval=False):
        '''
        Given input arrays x and y. Fits the model.
        '''
        pass

    @staticmethod
    def ISO_OLS(x, y):
        '''
        Isotonic OLS. 
        Returns slope if positive or 0 if not. 
        '''
        pass

class bin_regression(smoother):
    """Bin regression model.

    Bin regression is when a data sample is divided into intervals, and the prediction
    for each interval is the mean value of data points in the bin.

    Args
    ---------
        bins: the number of bins

    Attributes
    ---------
        bins (int): the number of bins
        bin_ys (arr[float]): the mean value of each bin
        bin_vals (arr[float]): the endpoints of each bin
        + attributes from smoother class

    Raises
    ---------
        TypeError: if bins is not a number
        ValueError: if bins < 2

    Example
    ---------
    >>> from regressio.models import bin_regression
    >>> from regressio.datagen import generate_random_walk
    >>> x, y = generate_random_walk(150)
    >>> model = bin_regression(bins=8)
    >>> model.fit(x, y, plot=True, confidence_interval=0.99)
    """

    def __init__(self, bins):
        raise NotImplementedError

    def fit(self, x, y, plot=False, confidence_interval=False):
        '''
        Given input arrays x and y. Fits the model.
        '''
        pass

    def predict(self, x):
        '''
        Given a 1-dimenional numpy array, make predictions.
        '''
        pass
        
    def plot_model(self, x, y, confidence_interval=False):
        '''
        Plot the models hypothetical predictions, MSE, and true data points.
        '''
        pass

    @staticmethod
    def check_bin(i, bin_x):
        '''
        Checks each bin has at least one data point.
        '''
        pass
    
    @staticmethod
    def check_bins_input(bins):
        '''
        Validates input bin parameter.
        '''
        pass

class cubic_spline(smoother):
    """Cubic spline model.

    Cubic spline is a spline constructed of multiple cubic piecewise 
    polynomials. Where two polynomials meet, the 1st and 2nd derivatives are equal. 
    This makes for a smooth fitting line. Cubic spline is better than high degree 
    polynomials as it oscillates less at its endpoints and between values 
    (ie. mitigates Runge's phenomenon).

    Args
    ---------
        pieces: the number of segments

    Attributes
    ---------
        pieces (int): the degree of the polynomial
        knot_xvals (arr[float]): knot x values
        knot_yvals (arr[float]): knot y values
        ws (arr[float]): piecewise model weights
        + attributes from smoother class

    Raises
    ---------
        TypeError: if pieces is not an integer
        ValueError: if pieces < 2

    Example
    ---------
    >>> from regressio.models import cubic_spline
    >>> from regressio.datagen import generate_random_walk
    >>> x, y = generate_random_walk(150)
    >>> model = cubic_spline(pieces=15)
    >>> model.fit(x, y, plot=True, confidence_interval=0.90)

    Reference
    ----------
    Kong, Qingkai, et al. Python Programming and Numerical Methods: A Guide for 
    Engineers and Scientists. Academic Press, an Imprint of Elsevier, 
    pythonnumericalmethods.berkeley.edu, Accessed July 2022. 
    """

    def __init__(self, pieces):
        raise NotImplementedError

    def fit(self, x, y, plot=False, confidence_interval=False):
        '''
        Given input arrays x and y. Fits the model.
        '''
        pass

    def calc_piecewise_weights(self, x, y):
        '''
        Given x, y, returns the weights for the piecewise polynomials. Constructs 
        system of equations in matrix form, and solves.
        '''
        pass

    def predict(self, xs):
        '''
        Given a set of x values, makes predictions.
        '''
        pass

    def plot_model(self, x, y, confidence_interval=False):
        '''
        Plots the models hypothetical predictions, MSE, and true data points.
        '''
        pass

    @staticmethod
    def find_knots(knot_vals, xs, ys):
        '''
        Helper function to find the y-value for each knot in xs.
        '''
        pass

    @staticmethod
    def polynomial(values, weights):
        '''
        Given a set of values and weights, returns the values after being passed through
        a polynomial with the given weights.
        '''
        pass

    @staticmethod
    def check_input_pieces(pieces):
        '''
        Validates input pieces.
        '''
        pass

class natural_cubic_spline(cubic_spline):
    """Natural cubic spline model.

    Child of the cubic_spline class. Differs in that the spline extrapolates 
    linearly beyond its knot boundaries.

    Args
    ---------
        pieces: the number of segments

    Attributes
    ---------
        pieces (int): the degree of the polynomial
        knot_xvals (arr[float]): knot x values
        knot_yvals (arr[float]): knot y values
        ws (arr[float]): piecewise model weights
        + attributes from smoother class

    Raises
    ---------
        TypeError: if pieces is not an integer
        ValueError: if pieces < 2

    Example
    ---------
    >>> from regressio.models import natural_cubic_spline
    >>> from regressio.datagen import generate_random_walk
    >>> x, y = generate_random_walk(200)
    >>> model = natural_cubic_spline(pieces=10)
    >>> model.fit(x, y, plot=True, confidence_interval=0.95)
    """
    def __init__(self, pieces):
        raise NotImplementedError

    def predict(self, xs):
        '''
        Given a set of x values, makes predictions.
        '''
        pass
    
    @staticmethod
    def line(x, slope, intercept):
        pass

class exp_moving_average(smoother):
    """Exponential moving average.

    An iterative model that make predictions based on the weighted moving average of past 
    predictions with exponentially decreasing weight.

    This model uses mean initialization for the first forecast value. This has no 
    significant effect compared to MSE optimization when len(y) >= 10. See more on initial
    forecasting values in the reference below.

    Args
    ---------
        alpha: the starting weight of previous value

    Attributes
    ---------
        alpha: the starting weight of previous value
        + attributes from smoother class

    Raises
    ---------
        TypeError: if alpha is not a floating point
        ValueError: if alpha is not >0 and <1

    Example
    ---------
    >>> from regressio.models import exp_moving_average
    >>> from regressio.datagen import generate_random_walk
    >>> x, y = generate_random_walk(200)
    >>> model = exp_moving_average(alpha=0.1)
    >>> model.fit(x, y, plot=True, confidence_interval=0.99)

    Reference
    ----------
    Hyndman, R.J., & Athanasopoulos, G. (2021) Forecasting: principles and practice, 
    3rd edition, OTexts: Melbourne, Australia. OTexts.com/fpp3. Accessed July 2022.
    """
    
    def __init__(self, alpha=0.2):
        raise NotImplementedError

    def fit(self, x, y, plot=False, confidence_interval=False):
        '''
        Given arrays x and y, computes exponentially smoothed y values.
        '''
        pass

    def plot_model(self, x, y, confidence_interval=False):
        '''
        Plots the smoothed model, MSE, and true data points and an 
        optional confidence interval.
        '''
        pass

    @staticmethod
    def check_alpha(alpha):
        '''
        Validate alpha input.
        '''
        pass

class gaussian_kernel(smoother):
    """Gaussian kernel.

    Kernel smoothing: For each value in a given array, each smoothed value is 
    calculated as some function applied to the original value and its surrounding points. 
    
    For the gaussian kernel, we center the gaussian distribution around each point and
    take the sum of the weighted values over all the data. The smoothness of the function is
    tuned by the full width half maximum parameter. For a complete description of the kernel 
    function see the reference below.

    Args
    ---------
        fwhm: width of kernel at 1/2 max height of the gaussian distribution

    Attributes
    ---------
        fwhm: width of kernel at 1/2 max height of the gaussian distribution
        + attributes from smoother class

    Raises
    ---------
        TypeError: if fwhm is not a float or int

    Example
    ---------
    >>> from regressio.models import gaussian_kernel
    >>> from regressio.datagen import generate_random_walk
    >>> x, y = generate_random_walk(100)
    >>> model = gaussian_kernel(fwhm=4)
    >>> model.fit(x, y, plot=True, confidence_interval=0.90)

    Reference
    ----------
    Brett, M. (2014, October 26). An introduction to smoothing. 
    Tutorials on imaging, computing and mathematics. matthew-brett.github.io/teaching, 
    Accessed July 2022.
    """
    def __init__(self, fwhm=None):
        raise NotImplementedError

    def fit(self, x, y, plot=False, confidence_interval=False):
        """
        Given arrays x and y, computes smoothed y values.
        """
        pass

    def plot_model(self, x, y, confidence_interval=False):
        '''
        Plots the models hypothetical predictions, MSE, and true data points.
        '''
        pass

    def fwhm_to_sigma(self, fwhm):
        """
        The FWHM is the full width of the kernel at half the maximum height 
        of the Gaussian function. For a Gaussian function with standard deviation 
        1, the maximum height is ~0.4. The width of the kernel at 0.2 to 0.2 (on the Y axis) 
        is the FWHM.

        This function takes in a FWHM value and returns sigma (a standard deviation).

        Formula: https://en.wikipedia.org/wiki/Full_width_at_half_maximum
        """
        pass

    def kernel_at_position(self, x, x_position, sigma):
        """
        At a given index denoted x_position, returns the kernel 
        weights over array x.

        Formula: https://en.wikipedia.org/wiki/Gaussian_filter
        """
        pass

    @staticmethod
    def check_fwhm(fwhm):
        '''
        Validate fwhm input.
        '''
        pass

class knn_kernel(smoother):
    """KNN kernel. 
    
    The KNN kernel is applied to each data point. The smoothed value is
    the average of the N nearest points. The smoothness of the function is
    determined by the size of N. The larger N is, the smoother the function.

    If the boundary of the training data is reached before we get to N
    data points, then we compute the smoothed values with less than N
    points. This results in a smooth fitting line.

    Args
    ---------
        n: the number of nearest points used in KNN calculation

    Attributes
    ---------
        n: the number of nearest points used in KNN calculation
        + attributes from smoother class

    Raises
    ---------
        ValueError: if n is <= 0 | n >= len(x)
        TypeError: if n is not an integer

    Example
    ---------
    >>> from regressio.models import knn_kernel
    >>> from regressio.datagen import generate_random_walk
    >>> x, y = generate_random_walk(100)
    >>> model = knn_kernel(n=6)
    >>> model.fit(x, y, plot=True, confidence_interval=0.90)
    """
    def __init__(self, n):
        raise NotImplementedError

    def fit(self, x, y, plot=False, confidence_interval=False):
        """
        Given arrays x and y, computes smoothed y values.
        """
        pass

    def plot_model(self, x, y, confidence_interval=False):
        '''
        Plots the models hypothetical predictions, MSE, and true data points.
        '''
        pass

    def find_closest_n_points(self, x, y):
        """
        Calculates KNN for all points in array y given x and y.
        """
        pass

    @staticmethod
    def check_n_input(n):
        '''
        Validate n parameter.
        '''
        pass

class weighted_average_kernel(smoother):
    """Weighted average kernel. 
    
    The Weighted average kernel is applied to each data point. The smoothed value is
    the weighted average of points within a specified distance. The smoothness of the 
    function is determined by the size of the distance. The larger the distance, the
    smoother the line.

    Args
    ---------
        dist: the max distance for points to be in order to be in kernel

    Attributes
    ---------
        dist: the max distance for points to be in order to be in kernel
        + attributes from smoother class

    Raises
    ---------
        ValueError: if dist is <= 0
        TypeError: if dist is not an integer

    Example
    ---------
    >>> from regressio.models import weighted_average_kernel
    >>> from regressio.datagen import generate_random_walk
    >>> x, y = generate_random_walk(100)
    >>> model = weighted_average_kernel(dist=6)
    >>> model.fit(x, y, plot=True, confidence_interval=0.90)
    """
    def __init__(self, dist):
        raise NotImplementedError

    def fit(self, x, y, plot=False, confidence_interval=False):
        """
        Given arrays x and y, computes smoothed y values.
        """
        pass

    def plot_model(self, x, y, confidence_interval=False):
        '''
        Plots the models hypothetical predictions, MSE, and true data points.
        '''
        pass

    def find_close_points(self, x, y):
        """
        Calculates weighted average for all points in array y given x and y.
        """
        pass

    @staticmethod
    def check_dist_input(dist):
        '''
        Validate dist parameter.
        '''
        pass

if __name__ == '__main__':
    main()