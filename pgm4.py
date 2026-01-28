import datetime as dt

issue_date= input("Enter issue date: ")
year, month, day=map(int, issue_date.split("-"))
date1=dt.date(year,month,day)

due_date= input("Enter due date: ")
year, month, day=map(int, due_date.split("-"))
date2=dt.date(year,month,day)

total_days=(date2-date1).days+1
val = total_days - 15

if(val<=0):
    print("No Fine")

elif(val<=5):
    fine = val * 0.5
    print("Fine of",fine)

elif(val<=10):
    fine = (5 * 0.5) + (val - 5) * 1
    print("Fine of",fine)

elif(val<=30):
    fine = (5 * 0.5) + (5 * 1) + (val - 10) * 5
    print("Fine of",fine)

else:
    print("Subscription Cancelled")
