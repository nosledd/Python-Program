class student():
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno

    def mark(self,m1,m2,m3,m4):
        self.marks={"Python:": m1,
                    "Php:": m2,
                    "SE:": m3,
                    "Cona:": m4}
    
    def calculate(self):
        self.total=sum(self.marks.values())
        self.percentage= self.total / len(self.marks)
        if(self.percentage >= 85):
            self.re= "Dstinction"
        elif(self.percentage >= 65):
            self.re= "First Class"
        elif(self.percentage >= 45):
            self.re= "Second Class"
        elif(self.percentage >= 35):
            self.re= "Third Class"
        else:
            self.re= "Fail"

    def display(self):
        print("\n--Student Record--")
        print("Name:", self.name)
        print("RegNo:", self.regno)
        print("Marks:", self.marks)
        print("Total Marks:", self.total)
        print("Percentage:", self.percentage)
        print("Result:", self.re)

s=student(input("Enter your Name: "), int(input("Enter your RegNo: ")))

print("Enter marks for: Python, PHP, SE, Cona")
s.mark(int(input()), int(input()), int(input()), int(input()))
s.calculate()
s.display()       
