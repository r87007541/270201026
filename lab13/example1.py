def selec_sort(list) :
  for i in range(len(list)): 
      
    min_value_index = i 
    for index in range(i+1, len(list)): 
        if list[min_value_index] > list[index]: 
            min_value_index = index
                      
    list[i], list[min_value_index] = list[min_value_index], list[i]
  return list 

list = [55,25,78,2,17,98,13,5]
print(selec_sort(list))