N = int(input("How many numbers you want to display :"))
evens = 0
for i in range(N) :
  x = int(input("Enter an Integer : "))
  if x % 2 == 0 :
    evens += 1

print(evens/N * 100 , "%")