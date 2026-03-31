Password = "Hello@123"

total_attempt=3
while  total_attempt>0 :
  password_fill=input("Enter your password-: ")
 
  total_attempt -=1
  if password_fill != Password:
    print("incorrect Password.")
    print(f" remaining {total_attempt} attempts")
  else:
    print("Access granted.")
    break
if total_attempt == 0:
    print("Access denied")
 

