a = int(input("Enter an Integer :"))
x = a//10
y = a%10
if a<10 :
  print(a)
elif x>10 :
  x = x%10
  print(x + y)
else :
  print(x + y)
  
