class coordinate (object):
    def __init__(self, x, y):
        """gonna return the x and y values of coordinate class"""
            
        self.x_coordinate  = x 
        self.y_cordinate = y
        
    def __str__ (self):
        return "[" + str(self.x_coordinate) + "," + str(self.y_cordinate)+ "]"
    
    def euclidian_dist(self, other):
        """calculate the euclidian distance between 2 points i.e babu and origin"""
        x_distance = (self.x_coordinate-other.x_coordinate) **2 
        y_distance = (self.y_cordinate- other.y_cordinate) **2
        euclidian_distance = x_distance - y_distance ** 0.5 
        return "Eucledian distance =" + str(euclidian_distance)

      
        
babu = coordinate(25, 97)
print (babu)
origin = coordinate(0,0)
print (origin)
print(coordinate.euclidian_dist(babu,origin))
print(babu.euclidian_dist(origin))

