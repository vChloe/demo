class Shape():
        def __init__(self):
                self.area = 0

        def get_area(self):
                if self.area == 0:
                        self.acumulate_area()
                print (self.area)
                return self.area

class Ellipse(Shape):
        def __init__(self,a,b):
                self._a = a
                self._b = b
                self.area = 0

        def acumulate_area(self):
                self.area = 3.14 * self._a * self._b
                print('椭圆面积')

class Square(Shape):
        def __init__(self,a):
                self._a = a
                self.area = 0

        def acumulate_area(self):
                self.area = self._a * self._a
                print('正方形面积')

class Rectangle(Shape):
        def __init__(self,a,b):
                self._a = a
                self._b = b
                self.area = 0

        def acumulate_area(self):
                self.area = self._a * self._b
                print('矩形面积')

class Circle(Shape):
        def __init__(self,a):
                self._a = a
                self.area = 0

        def acumulate_area(self):
                self.area = 3.14 * self._a * self._a
                print('圆面积')

Shapes = [Ellipse(10,20),Square(15),Circle(5),Rectangle(20,15),Circle(5),Square(15),Ellipse(10,20)]

def compute_area(Shapes):
        s = 0
        for i in range (0,7):
                s+= Shapes[i].get_area()
        return s

total_area = compute_area(Shapes)

print('面积之和：',total_area)










                
