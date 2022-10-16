# Import curve fitting package from scipy
from scipy.optimize import curve_fit
import numpy as np


# source: https://towardsdatascience.com/basic-curve-fitting-of-scientific-data-with-python-9592244a2509
# https://machinelearningmastery.com/curve-fitting-with-python/


def objective(x, a, b):
    return a * x + b


def objectiveQuad(x, a, b, c):
    return a * x + b * np.power(x, 2) + c


# MPC
def fitMPC(x, y):
    # curve_fit(f=exponential, xdata=x_dummy, ydata=y_dummy, p0=[0, 0], bounds=(-np.inf, np.inf)) params: array of
    # parameters from fit (in this case [a, b]) a is the coefficient cov: the estimated covariance of params which
    # can be used to determine the standard deviations of the fitting parameters (square roots of the diagonals)
    params, _ = curve_fit(f=objectiveQuad, xdata=x, ydata=y)
    a, b, c = params
    x_line = np.arange(min(x), max(x), 1)
    y_line = objectiveQuad(x_line, a, b, c)
    return x_line, y_line, params


def fitTTP(x, y):
    params, _ = curve_fit(objective, x, y)
    a, b = params
    x_line = np.arange(min(x), max(x), 1)
    y_line = objective(x_line, a, b)
    return x_line, y_line, params
