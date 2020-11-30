names = []
salaries = []
employees = {}
for i in range(5) :
  name = input("Enter the employee's name :\n")
  salary = int(input("Enter the employee's salary :\n"))
  names.append(name)
  salaries.append(salary)
for x,y in zip(names , salaries) :
  print(x)
  print(y)
  employees[x] = y
sorted_salaries = sorted(employees.values())
for x in employees.keys() :
  if employees[x] in sorted_salaries[2:] :
    print(x)
    print(employees[x])