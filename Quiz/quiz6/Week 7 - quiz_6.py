# Defines two classes, Point() and NonVerticalLine().
# An object for the second class is created by passing named arguments,
# point_1 and point_2, to its constructor.
# Such an object can be modified by changing one point or both points thanks to the
# function change_point_or_points().
# At any stage, the object maintains correct values for slope and intersect.
#
# Written by *** and Eric Martin for COMP9021


class Point():
    def __init__(self, x = None, y = None):
        if x == None and y == None:
            self.x = 0
            self.y = 0
        elif x == None or y == None:
            print('Need two coordinates, point not created.')
        else:
            self.x = x
            self.y = y


class NonVerticalLine:
    def __init__(self, *, point_1, point_2):
        if not self._check_and_initialise(point_1, point_2):
            print('Incorrect input, line not created.')
            return
        else:
            self.point_1 = point_1
            self.point_2 = point_2
            self.slope = float((self.point_1.y - self.point_2.y)/(self.point_1.x-self.point_2.x))
            self.intercept = float(self.point_1.y - self.slope * self.point_1.x)
            if self.slope == -0.0:
                self.slope = 0.0

    def change_point_or_points(self, *, point_1 = None, point_2 = None):
        if not self._change_point_or_points(point_1, point_2):
            print('Could not perform this change.')
            return
        else:
            if point_1:
                self.point_1 = point_1
            if point_2:
                self.point_2 = point_2
            self.slope = float((self.point_1.y - self.point_2.y) / (self.point_1.x - self.point_2.x))
            self.intercept = float(self.point_1.y - self.slope * self.point_1.x)
            if self.slope == -0.0:
                self.slope = 0.0

    def _check_and_initialise(self, p1, p2):
        pass
        # Replace this comment with your code
        if p1.x == p2.x :
            return False
        else:
            return True

    def _change_point_or_points(self, p1, p2):
        pass
        # Replace this comment with your code
        if p1:
            self.point_1 = p1
        if p2:
            self.point_2 = p2
        if self.point_1.x == self.point_2.x:
            return False
        else:
            return True
    # Possibly define other functions



            
            
