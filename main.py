from method.method import MonteCarlo
from method.figure.figure import Figure
from method.figure.point.point import Point
import numpy as np

if __name__ == "__main__":
    figure = Figure([
        "-x**2 + y**3 < 2",
        "x - y < 1",
        ])
    func = "cos(x)"
    limits = [-np.pi/2, np.pi/2]
    N = 10**4
    I = MonteCarlo.integrate(func, limits, N=N)
    print(I)