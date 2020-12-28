def hailstone(x) :
  str_x = str(x)
  if x == 1 :
    return str_x
  elif x % 2 == 0:
    return str_x + "," + hailstone(x//2)
  else:
    return str_x + "," + hailstone(3*x + 1)
print(hailstone(5))