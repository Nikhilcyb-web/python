balance=0
while True:
  print(1,"CHECK BALANCE")
  print(2,"Deposit money")
  print(3,"withdraw money")
  print(4,exit)
  balance +=0
  user_input=int(input("CHOOSE BETWEEN 1 TO 4-: "))
  if user_input==1:
    print(balance)
  elif user_input==2:
    deposit=int(input("\nhow much money you want to deposit-: "))
    balance = balance + deposit
    print("\ndeposit successful")
    print("\nAfter deposite the balance is -: ",balance)
  elif user_input==3:
    withdraw_money=int(input("How much money you want to withdraw-: "))
    if withdraw_money>balance:
      print("Insufficiant amount..")
    else:
      balance = balance-withdraw_money
      print("\nAfter withdraw the total balance is-: ",balance)
  elif user_input==4:
    print("\nThankyou.")
    break
  else:
    print("invalid choose... Try again")