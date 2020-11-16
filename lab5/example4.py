password = "fth123"
while True :
  user_pass = input("Enter the Password : ")
  if user_pass == "help" :
    print(password[0])
  elif password != user_pass :  
    print("Wrong")
  else :
    print("Welcome")
    break
