class Vector:
    def init(self, d):              #Create d - dimensional vector of zeros
     self.coords =[0]*d
    def len (self):                 #Return the dimension of the vector
     return len(self.coords)
    def getitem (self,j):            #Return jth coordinate of vector
      return self.coords[j]

    def setitem (self,j,val):     #Set jth coordinate of vector to given value.
       self.coords[j] = val

    def __add__(self,other_vec):
        if len(self)!= len(other_vec):
            return Error
        result=Vector()
        for i in range(len(self)):
            result= self[i]+other_vec[i]
        return result
    def __eq__(self,other_vec):
        return self==other_vec

    def __ne__(self, other_vec):
        return self==other_vec

