while True:
  username=input("Enter you username-: ")
  list1=[1,2,3,4,5]
  if len(username)<6:
    print("username must be equal and greater then character.")
    continue
  if username[0] >='0' and username[0]<='9':
    print("username must not start with a number. ")
    continue
  valid = True
  for ch in username:
    if not(
          (ch >= 'a' and ch <= 'z') or
          (ch >= 'A' and ch <= 'Z') or
          (ch >= '0' and ch <= '9')
        ):
            print("Invalid: username must contain only letters and numbers")
            valid = False
            break

  if valid:
        print("Username accepted")
        break  
  
    