class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y

    def compute_distance(self, point) -> float:
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return distance


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def compute_length(self):
        return self.start.compute_distance(self.end)

    def compute_slope(self):
        x_1, y_1 = self.start.x, self.start.y
        x_2, y_2 = self.end.x, self.end.y

        if x_1 - x_2 == 0:
            slope = "Infinite slope, vertical line"
        else:
            slope = (y_2 - y_1) / (x_2 - x_1)

        return slope

    def compute_horizontal_cross(self):
        return self.start.y * self.end.y <= 0

    def compute_vertical_cross(self):
        return self.start.x * self.end.x <= 0


class Rectangle:
    def __init__(self):
        self.width = None
        self.height = None
        self.center = None
        self.bottom_left = None
        self.upper_right = None

    def method1(self, point: Point, width: float, height: float):
        self.bottom_left = point
        self.width = width
        self.height = height
        self.compute_center()

    def method2(self, point: Point, width: float, height: float):
        self.center = point
        self.width = width
        self.height = height
        self.compute_corners()

    def method3(self, bottom_left: Point, upper_right: Point):
        self.bottom_left = bottom_left
        self.upper_right = upper_right
        self.compute_width_height()
        self.compute_center()

    def method4(self, left: Line, right: Line, top: Line, bottom: Line):
        self.bottom_left = left.start
        self.upper_right = right.end
        self.width = right.start.x - left.start.x
        self.height = top.start.y - bottom.start.y
        self.compute_center()

    def compute_center(self):
        self.center = Point(self.bottom_left.x + self.width / 2, self.bottom_left.y + self.height / 2)

    def compute_corners(self):
        half_width = self.width / 2
        half_height = self.height / 2
        self.bottom_left = Point(self.center.x - half_width, self.center.y - half_height)
        self.upper_right = Point(self.center.x + half_width, self.center.y + half_height)

    def compute_width_height(self):
        self.width = self.upper_right.x - self.bottom_left.x
        self.height = self.upper_right.y - self.bottom_left.y

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self):
        super().__init__()

    def initialize_square(self, point: Point, side_length: float):
        super().method2(point, side_length, side_length)

    def compute_interference_point(self, point: Point):
        if self.bottom_left.x <= point.x <= self.upper_right.x and \
                self.bottom_left.y <= point.y <= self.upper_right.y:
            return True
        return False
