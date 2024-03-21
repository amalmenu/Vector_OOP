
class Vector:
    def __init__(self, d):  # Create d-dimensional vector of zeros
        self.coords = [0] * d

    def __len__(self):  # Return the dimension of the vector
        return len(self.coords)

    def __getitem__(self, j):  # Return jth coordinate of vector
        return self.coords[j]

    def __setitem__(self, j, val):  # Set jth coordinate of vector to given value.
        self.coords[j] = val

    def __add__(self, other_vec):
        if len(self) != len(other_vec):
            raise ValueError("Vectors must have the same dimension for addition")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other_vec[i]
        return result

    def __eq__(self, other_vec):
        if not isinstance(other_vec, Vector):
            return False
        return self.coords == other_vec.coords


# Test the Vector class
v1 = Vector(2)
v2= Vector(2)
v1.__setitem__(0,1)
v2.__setitem__(0,2)
v1.__setitem__(1,1)
v2.__setitem__(1,1)
print(v1.__getitem__(0))
print(v1.__len__())
print(v1.__eq__(v2))