class LowIncome(Exception):
    pass

class bank():
    cust_count= 0                # Cust
    def __init__(self,name,id):
        self.name= name
        self.id= id
        bank.cust_count += 1

class loan(bank):
    bank_amount=500000
    loan_given=0
    def __init__(self, name, id,income):
        super().__init__(name, id)
        self.income= income
        self.loan_amount= 0

    def sanctioned(self,amount):
        try:
            if self.income < 25000:
                raise LowIncome
            if (loan.bank_amount - loan.loan_given < amount):
                raise ValueError
            
            self.loan_amount = amount
            loan.loan_given += amount
            print("Loan Sanctioned Successfully")
        except LowIncome:
            print("Loan Reject")
        except ValueError:
            print("Insufficient Bank Fund") 

    def display(self):
        print("Customer Name: ", self.name)
        print("Customer Id:", self.id)
        print("Loan Amount Given:", self.loan_amount)

    @classmethod
    def loan_details(self):
        print("\n--Bank Details--")
        print("No of Customers:", self.cust_count)
        print("Loan Amount:", self.bank_amount)
        print("Sanctioned Amount:", self.loan_given)
        print("Balance Amount:", (self.bank_amount - self.loan_given))

customers=[]
choice="Y"
while(choice.upper() == "Y"):
    name=input("Enter your name: ")
    id=int(input("Enter your Id: "))
    income=int(input("Enter your monthly income: "))
    loann=int(input("Enter your Loan Amount: "))

    cust= loan(name,id,income)
    cust.sanctioned(loann)
    customers.append(cust)
    choice= input("\nDo you want to continue (Y/N): ")

print("\n--Customer Details--")
for c in customers:                             # Customer list stores multiple objects inside it
    c.display()                                 # Displayed as per each object
    print()

loan.loan_details()