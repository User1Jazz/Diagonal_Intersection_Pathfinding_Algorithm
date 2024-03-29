def get_intersection_point(p1, p2, p3, p4):
    # Calculate the slopes (m1, m2) of the two lines
    m1 = (p2.y - p1.y) / (p2.x - p1.x) if p2.x != p1.x else float('inf')
    m2 = (p4.y - p3.y) / (p4.x - p3.x) if p4.x != p3.x else float('inf')
    
    # If the slopes are equal, the lines are parallel (or coincident) and have no intersection
    if m1 == m2:
        return None  # No intersection
    
    # Calculate the y-intercepts (b1, b2) of the lines
    b1 = p1.y - m1 * p1.x
    b2 = p3.y - m2 * p3.x
    
    # If one of the lines is vertical, calculate x based on the other line's equation
    if m1 == float('inf'):
        x = p1.x
        y = m2 * x + b2
    elif m2 == float('inf'):
        x = p3.x
        y = m1 * x + b1
    else:
        # Calculate the intersection point (x, y)
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
    
    return point(x, y)

class point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def values(self):
        return (self.x, self.y)