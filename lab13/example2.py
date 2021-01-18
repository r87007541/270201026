def binary_search(list,low,high,value) :
  if high >= low :
    mid = (high+low) // 2 

    if list[mid] == value :
      return list.index(list[mid])
    
    elif list[mid] > value :
      return binary_search(list,low,mid-1,value)

    elif list[mid] < value  :
      return binary_search(list,mid+1,high,value)

  else :
    return -1 
    

list = [ 2, 3, 4, 10, 40 ]

print(binary_search(list,0,len(list)-1,5))