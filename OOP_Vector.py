class Vector:
    def init(self, d):
#Create d - dimensional vector of zeros
        self.coords = [0]*d
    def len (self):
#Return the dimension of the vector
     return len(self.coords)