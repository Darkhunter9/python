class Building(object):
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height
    
    def corners(self):
        north_west = [self.south+self.width_NS, self.west]
        north_east = [self.south+self.width_NS, self.west+self.width_WE]
        south_west = [self.south, self.west]
        south_east = [self.south, self.west+self.width_WE]
        corner = {"north-west": north_west, "north-east": north_east, "south-west": south_west, "south-east": south_east}
        return corner
    
    def area(self):
        return self.width_NS*self.width_WE
    
    def volume(self):
        return self.area()*self.height
    
    def __repr__(self):
        return "Building({0}, {1}, {2}, {3}, {4})".format(self.south, self.west, self.width_WE, self.width_NS, self.height)