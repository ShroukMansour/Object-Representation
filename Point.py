from numpy.linalg import det
class Point:
    # 0 for black, 1 for white
    def __init__(self, point, type=1):
        self.x = point[0]
        self.y = point[1]
        self.type = type

    def calc_type(self, point_before, point_after):
        mat = [[point_before[0], point_before[1], 1],[self.x, self.y, 1],[point_after[0], point_after[1], 1]]
        det_val = det(mat)
        if (det_val > 0):
            self.type = 1
        elif (det_val < 0):
            self.type = 0
        return det_val
