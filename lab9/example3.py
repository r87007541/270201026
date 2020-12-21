def number_evens(list) :
  count = 0
  if len(list) == 0 :
    return 0
  if list.pop() % 2 == 0 :
    count += 1
  return count + number_evens(list)
print(number_evens([0,1,2,3,4,5,6,7]))
  
    