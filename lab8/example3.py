import random
def get_rand_list(b,e,n) :
  list = []
  for i in range(n) :
    x = random.randint(b,e)
    list.append(x)
  return list
b , e , n = 0 , 10 , 5
list1 = get_rand_list(b,e,n)
list2 = get_rand_list(b,e,n)
def intersection(list1, list2): 
    lst3 = [value for value in list1 if value in list2] 
    return lst3 
print(intersection(list1,list2))