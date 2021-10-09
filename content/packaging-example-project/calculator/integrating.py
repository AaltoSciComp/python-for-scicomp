from scipy import integrate


def integral(function, lower_limit, upper_limit):
    return integrate.quad(function, lower_limit, upper_limit)
