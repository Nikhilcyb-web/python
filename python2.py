secret = 8
count=0
max_guess=5
while count < max_guess:
  guess=int(input("GUESS THE NUMBER-: "))
  count+=1


 
  if guess> secret:
    print("Too High.")
    print("the remaining attempts are -:", max_guess-count)
   
  elif guess< secret:
    print("Too less.")
    print("the remaining attempts are -:", max_guess-count)
  

  else:
    
 
    print("Guess number is correct. in ",count,"times.")
    print("the remaining attempts are -:", max_guess-count)
    break
if max_guess==count  and guess != secret :
  print("game over ,Try again")

