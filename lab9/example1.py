def harmonic_sum(n) :
  x=0
  for i in range(1,n+1):
    i = 1/i
    x += i
  print(x)
n = int(input("Enter an integer :"))
harmonic_sum(n)
