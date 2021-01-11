def sum_of_a_list(a_list) :
  if a_list == [] :
    return 0
  elif isinstance(a_list.pop(),list) :
    