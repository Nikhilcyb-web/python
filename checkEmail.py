print("RULES")
print("Must contain exactly one @")
print("Must have at least one character before @")
print("Must have at least one . after @")
print("Must NOT start with @")
print("Must NOT end with @")
while True:
    email = input("Enter email: ")

    
    count = 0
    for ch in email:
        if ch == '@':
            count += 1

    if count != 1:
        print("Invalid: email must contain exactly one '@'")
        continue

    
    if email[0] == '@' or email[-1] == '@':
        print("Invalid: '@' cannot be at start or end")
        continue

    
    index = 0
    for i in range(len(email)):
        if email[i] == '@':
            index = i
            break

    if index == 0:
        print("Invalid: no characters before '@'")
        continue

    
    dot = False
    for i in range(index + 1, len(email)):
        if email[i] == '.':
            dot = True
            break

    if not dot:
        print("Invalid: must contain '.' after '@'")
        continue

    print("Email accepted")
    break
