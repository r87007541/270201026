def reverse_list(list) :
  n = len(list)
  reversed_list = []
  for i in list[n::-1] :
    reversed_list.append(i)
  return reversed_list
list = [1,2,3,4]
print(reverse_list(list))