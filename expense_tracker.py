expenses=[]
total=0
while True:
    print("\n1.Add expense")
    print("2.view Expenses")
    print("3.exit")
    choice=input("enter your choice:")
    if choice=="1":
      expense=input("enter expense name:")
      amount=float(input("enter amount:")  )
      category=input("enter category:")
      total=total+amount
      expenses.append([expense,category,amount])
      print("expense added!")
    elif choice=="2":
      print("\nAll expenses:")
      for item in expenses:
       print("Name:",item[0])
       print("category:",item[1])
       print("Amount:",item[2])
       print("--------------")
    elif choice=="3":
       print("Thank You!")
       break  
else :
    print("invalid choice!") 

