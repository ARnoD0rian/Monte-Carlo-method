class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
    @property
    def coodinate(self):
        return (self.x, self.y)
    
    def __repr__(self) -> str:
        return f"{self.coodinate}"