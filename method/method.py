from method.figure.figure import Figure
from method.figure.point.point import Point
from Helpers.Multiprocessor import Multiprocessor
import sympy as sym
import multiprocessing as np
import numpy as np

N_PROCESS = 4

class MonteCarlo:
    @staticmethod
    def calculating_area(figure: Figure,
                           square: list[Point],
                           N: int = 0,
                           points: list[Point] | None =  None
                           ) -> float:
        
        if points is None:
            points = MonteCarlo._get_points(N, (square[0].x, square[1].x))
        
        multiprocessor = Multiprocessor()
        
        for k in range(N_PROCESS):
            multiprocessor.run(
                MonteCarlo._throw_dots,
                figure, points[int(k / N_PROCESS * N):
                               int((k+1) / N_PROCESS * N)]
            )
            
        K = sum(multiprocessor.wait())
        
        return (K / N) * (abs(square[1].x - square[0].x)**2 + abs(square[1].y - square[0].y)**2) / 2
        
    
    @staticmethod
    def integrate(func: str, limits: tuple[float, float], N: int = 10, square: list[Point] | None = None) -> float:
        figure = Figure([f"x <= y", f"x >= 0"])
        if square is None:
            square = [Point(limits[0], limits[0]), Point(limits[1], limits[1])]
        points = MonteCarlo._get_points(N, limits)
        x = sym.symbols('x')
        F = sym.sympify(func)
        mean_x = np.linspace(limits[0], limits[1], N + 1)
        for i in range(len(points)):
            points[i].y = abs(F.subs(x, mean_x[i]))
        
        return MonteCarlo.calculating_area(
            figure,
            square,
            N=N,
            points=points
            )
        
    @staticmethod
    def _throw_dots(figure: Figure, points: list[Point]) -> int:
        k = 0
        for point in points:
            if figure.checking_location_point(point):
                k +=1
        return k
    
    @staticmethod
    def _get_points(N: int, limits: tuple[float, float]) -> list[Point]:
        points = np.random.uniform(low=limits[0], high=limits[1], size=(N + 1, 2))
        points = [Point(x[0], x[1]) for x in points]
        return points
    