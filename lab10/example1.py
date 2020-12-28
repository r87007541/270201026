def basicmultiplicaiton(n,m) :
  if m == 0 :
    return n*m
  else :
    return n + basicmultiplicaiton(n,m-1)
print(basicmultiplicaiton(6,3))