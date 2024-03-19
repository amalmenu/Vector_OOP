class Vector:
    def init(self, d):
#Create d - dimensional vector of zeros
        self.coords =[0]*d
    def len (self):
#Return the dimension of the vector
     return len(self.coords)
    def getitem (self,j):
#Return jth coordinate of vector
     return self.coords[j]

    def setitem (self,j,val):
#Set jth coordinate of vector to given value.
     self.coords[j] = val