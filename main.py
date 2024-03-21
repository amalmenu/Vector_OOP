class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overloading the '+' operator"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Overloading the '-' operator"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Overloading the '*' operator for scalar multiplication"""
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        """Overloading the '==' operator for equality comparison"""
        return self.x == other.x and self.y == other.y

    def __str__(self):
        """String representation of the vector"""
        return f"({self.x}, {self.y})"


# Creating instances of Vector class
v1 = Vector(2, 3)
v2 = Vector(5, 7)

# Testing operator overloading
print("v1 =", v1)
print("v2 =", v2)
print("v1 + v2 =", v1 + v2)
print("v2 - v1 =", v2 - v1)
print("v1 * 2 =", v1 * 2)

# Testing equality comparison
print("v1 == v2:", v1 == v2)
