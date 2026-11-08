class Point2D():

    def __init__(self, x, y):

        self.x = x
        self.y = y


    def __add__(self, other):

        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):

        return Point2D(self.x - other.x, self.y - other.y)

    def __abs__(self):

        return (self.x**2 + self.y**2)**0.5

    def __lt__(self, other):

        return abs(self) < abs(other)

    def __repr__(self):

        return (f"Point2D(x={self.x} y={self.y})")

    def __eq__(self, other):

        return (self.x == other.x and self.y == other.y)
    
point1 = Point2D(5,10)            
point2 = Point2D(0,4)    
point3 = point1 + point2
print ("Неизменяемость:", point1, point2, point3)
print ("Удаленность от начала координат:",abs(point1), abs(point2))
points = [point1, point2, point3]
print ("Сортировка:",sorted(points))
print ("Равенство точек:", point1 == point2, point1 == point1)

