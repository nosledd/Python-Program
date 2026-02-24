class sky():
    flight_no=int(input("Enter flight no: "))
    origin=input("Enter origin: ")
    destination=input("Enter destination: ")
    fare=int(input("Enter the fare: "))
    tickets=int(input("Enter the tickets: "))
    food=input("Enter food: ")

    @classmethod
    def display(cls):
        print("--Flight Details--")
        print("Flight No:", getattr(cls,"flight_no"))
        print("Origin:", getattr(cls,"origin"))
        print("Destination:", getattr(cls,"destination"))
        print("Fare:", getattr(cls,"fare"))
        print("Tickets:", getattr(cls,"tickets"))
        print("Food:", getattr(cls,"food"))

    @classmethod
    def baggage(cls):
        setattr(sky,"check-in","12kg")
        setattr(sky,"cabin","10kg")
        print("--Baggage Details--")
        print("Check-in:", getattr(cls,"check-in"))
        print("Cabin:", getattr(cls,"cabin"))

    def book_tickets(self,name,tickets):
        self.name=name
        self.tickets=tickets

        if(self.tickets <= sky.tickets):
            sky.tickets= self.tickets - sky.tickets
            print("-- Booking Details--")
            print("Customer Name:", self.name)
            print("Ticket fare:", (self.tickets * sky.fare ))
        else:
            print("Sorry Tickets are not Available")


sky.display()
s=sky()

print("\n1. Update Fare\n2. Display Baggage\n3. Book Tickets\n4. Exit")
while(True):
    op=int(input("\nSelect the Option: "))
    if(op == 1):
        fare=int(input("Update the Fare: "))
        setattr(sky,"fare",fare)
        print("Updated")
    elif(op == 2):
        sky.baggage()
    elif(op == 3):
        name=input("Enter the Name: ")
        tick=int(input("Enter the No. of Tickets: "))
        s.book_tickets(name,tick)
    elif(op == 4):
        print("Exiting!!")
        exit()
    else:
        print("No such option!! Retry Again")




    
    