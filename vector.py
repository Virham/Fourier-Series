import math



class Vector:
    def __init__(self, x=None, y=None):
        self.x = x if isinstance(x, int) or isinstance(x, float) else 0
        self.y = y if isinstance(y, int) or isinstance(y, float) else 0
        self.returned = 0

    def __getitem__(self, item):
        if item == 0:
            return self.x

        if item == 1:
            return self.y

        print("didn't return anything")

    def __iter__(self):
        yield self.x
        yield self.y

    def __len__(self):
        return 2

    def __repr__(self):
        return "Vector(x=%s, y=%s)" % (self.x, self.y)

    def __add__(self, other):
        """
        returns the vector added with another vector or number

        :param other: number or vector
        :return:
        """
        try:
            return Vector(x=self.x + other.x, y=self.y + other.y)

        except AttributeError:
            return Vector(x=self.x + other, y=self.y + other)

    def __iadd__(self, other):
        """
        adds another vector to current vector, or adds a number to current vector

        :param other: number or vector
        :return:
        """
        return self + other

    def __sub__(self, other):
        """
        define the subtract operation

        :param other: number or vector
        :return: added vector
        """
        try:
            return Vector(x=self.x - other.x, y=self.y - other.y)

        except AttributeError:
            return Vector(x=self.x - other, y=self.y - other)

    def __isub__(self, other):
        """
        subtracts another vector to current vector, or subtracts a number to current vector

        :param other: number or vector
        :return:
        """
        return self - other

    def __mul__(self, other):
        """
        define the multiply operation
        :param other: number or vector
        :return:
        """
        try:
            return Vector(x=self.x * other.x, y=self.y * other.y)

        except AttributeError:
            return Vector(x=self.x * other, y=self.y * other)

    def __imul__(self, other):
        """
        adds another vector to current vector, or add a number to current vector

        :param other: number or vector
        :return:
        """
        return self * other

    def __truediv__(self, other):
        """
        define the divide operation

        :param other: number or vector
        :return:
        """

        try:
            return Vector(x=self.x / other.x, y=self.y / other.y)

        except AttributeError:
            return Vector(x=self.x / other, y=self.y / other)

    def __itruediv__(self, other):
        """
        divides vector by another vector or divides vector by number

        :param other:
        :return:
        """
        return self / other

    def __round__(self, n=None):

        return Vector(round(self.x), round(self.y))


    @property
    def sqrt_magnitude(self):
        return pow(self.x, 2) + pow(self.y, 2)

    @property
    def magnitude(self):
        magnitude = math.sqrt(self.sqrt_magnitude)
        #return magnitude if magnitude % 1 != 0 else int(magnitude)
        if magnitude % 1 != 0:
            return magnitude
        return int(magnitude)

    @magnitude.setter
    def magnitude(self, length):
        unit = self.unit
        vector = unit * length
        self.x = vector.x if vector.x % 1 != 0 else int(vector.x)
        self.y = vector.y if vector.y % 1 != 0 else int(vector.y)

    @property
    def unit(self):
        return self / self.magnitude

    @property
    def list(self):
        return [self.x, self.y]



