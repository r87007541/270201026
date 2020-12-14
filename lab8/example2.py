int_1 = int(input("Enter the first integer :"))
int_2 = int(input("Enter the second integer :"))
def print_primes_between(int_1,int_2) :
  primes_between = []
  for i in range(int_1,int_2) :
    for _ in range(2,i) :
      if i % _ == 0 :
        continue
      else :
        primes_between.append(i)
  return primes_between
print(print_primes_between(int_1,int_2))