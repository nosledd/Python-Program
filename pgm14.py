from abc import ABC, abstractmethod
class tourism(ABC):
    room_rent=int(input("Enter the Room Rent: "))
    vehicle_rent=int(input("Enter the vehicle Rent: "))

    def __init__(self,cust_name):
        self.name= cust_name

    @abstractmethod
    def booking(value):
        pass

class guesthouse(tourism):
    def __init__(self,cust_name,no_guest):
        super().__init__(cust_name)
        self.no_guest= no_guest

    def booking(self,value):
        self.no_days= value
        print("\n--Booking Details--")
        print("Customer Name:", self.name)
        print("No of guests:", self.no_guest)
        total= self.no_days * tourism.room_rent * self.no_guest
        print(f"The rent for {self.no_days} days is {total} ")

class vehiclerent(tourism):
    def __init__(self, cust_name):
        super().__init__(cust_name)
    
    def booking(self,value):
        self.no_kms= value
        print("\n--vehicle Rent Details--")
        print("Customer Name: ", self.name)
        if(self.no_kms <= 25):
            rent= 200 + (self.no_kms * tourism.vehicle_rent)
            print(f"The rent for {self.no_kms} kms per hours is {rent} ")
        else:
            rent= 400 + (self.no_kms * tourism.vehicle_rent)
            print(f"The rent for {self.no_kms} kms per hours is {rent} ")


print("\n--Booking Details--")
g=guesthouse(input("Enter Name: "), int(input("Enter No. of guests: ")) )
g.booking(int(input("Enter No of Days: ")))

print("\n--vehicle Rent Details--")
v=vehiclerent(input("Enter Name: "))
v.booking(int(input("Enter No of Kms: ")))