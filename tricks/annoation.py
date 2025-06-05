class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
        self.area = 0
    
def area(radius:float) -> float:
    "compute area of a circle with given radius"
    pass

print(area.__annotations__)  # {'para':'para type', 'return':'return type'}