# Defines two classes, Point() and NonVerticalLine().
# An object for the second class is created by passing named arguments,
# point_1 and point_2, to its constructor.
# Such an object can be modified by changing one point or both points thanks to the
# function change_point_or_points().
# At any stage, the object maintains correct values for slope and intersect.
#
# Written by Xiaowen Huang


class Point:
    def __init__(self, x=None, y=None):
        if x == None and y == None:
            self.x, self.y = 0, 0
        elif x == None or y == None:
            print('Need two coordinates, point not created.')
        else:
            self.x, self.y = x, y


class NonVerticalLine:
    def __init__(self, point_1, point_2):
        if not self._check_and_initialise(point_1, point_2):
            print('Incorrect input, line not created.')
        else:
            self.p1, self.p2 = point_1, point_2
            self.slope = (point_1.y - point_2.y)/(point_1.x - point_2.x)
            self.intercept = point_1.y - self.slope * point_1.x

    def _check_and_initialise(self, point_1, point_2):
        if point_1.x and point_1.y and point_2.x and point_2.x:
            if point_1.x != point_2.x:
                return True
            else:
                return False
        else:
            return False

    def check(self, point_1, point_2):
        if point_1 is None and point_2 is not None:
            if point_2.x == self.p1.x:
                return False
        elif point_2 is None and point_1 is not None:
            if point_1.x == self.p2.x:
                return False
        elif point_1 and point_2:
            if point_1.x == point_2.x:
                return False
        return True

    def change_point_or_points(self, point_1=None, point_2=None):
        if self.check(point_1, point_2):
            if point_1:
                self.p1 = point_1
            if point_2:
                self.p2 = point_2
            self.slope = (self.p1.y - self.p2.y)/(self.p1.x - self.p2.x) + 0.0
            self.intercept = self.p1.y - self.slope * self.p1.x
        else:
            print('Could not perform this change.')
