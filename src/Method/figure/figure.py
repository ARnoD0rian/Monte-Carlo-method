from Method.figure.point.point import Point
import sympy as sym

class Figure:
    def __init__(self, conditions: list[str]) -> None:
        self.x, self.y = sym.symbols('x y')
        self._conditions = [sym.sympify(condition)
                           for condition in conditions
                           ]
    
    def checking_location_point(self, point: Point) -> bool:
        for condition in self._conditions:
            if not condition.subs({self.x: point.x, self.y: point.y}):
                return False  
        return True
    
    @property
    def conditions(self):
        return '\n'.join([str(x) for x in self._conditions])
    
if __name__ == "__main__":
    conditions = [
        "x < 2.0",
        "y < 2.0",
        "x**2 - y > 1.0"
    ]
    fig = Figure(conditions)
    print(fig.conditions)
    point = Point(1.5, -1)
    print(fig.checking__location_point(point))
        
        