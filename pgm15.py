class rectangle():
    def __init__(self,l,b):
        self.length=l
        self.width=b

    def area(self):
        area_rec= self.length * self.width
        print("Area of Rectangle:", area_rec)
    
    def perimeter(self):
        per= 2 * (self.length + self.width)
        print("Permeter of Rectangle is:", per)

class box(rectangle):
    def __init__(self, h, b, l):
        super().__init__(l, b)
        self.height=h

    def surface_area_box(self):
        box= ((2 * self.length * self.width) +  (2 * self.length * self.height) + (2 * self.width * self.height))
        print("Surface Area of Box:", box)

l,b,h= map(int, input("Enter Length, Height, Width: ").split())    
r= rectangle(l,b)
r.area()
r.perimeter()

b= box(h,b,l)
b.surface_area_box()
        