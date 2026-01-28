bank=int(input("Money to be returned: "))

if (bank%5==0):
  num1 = bank // 500    
  temp = bank % 500       

  num2 = temp // 200          
  temp = temp % 200        

  num3 = temp // 100          
  temp = temp % 100 

  num4 = temp // 50          
  temp = temp % 50 

  num5 = temp // 20          
  temp = temp % 20

  num6 = temp // 10           

  print("Number of 500 notes:", num1)
  print("Number of 200 notes :", num2)
  print("Number of 100 notes :", num3)
  print("Number of 50 notes :", num4)
  print("Number of 20 notes :", num5)
  print("Number of 10 notes :", num6)

else: 
   print("Error") 
