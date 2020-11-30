names = []
salaries = []
for i in range(5) :
  name = input("Enter the employee's name :\n")
  salary = input("Enter the employee's salary :\n")
  names.append(name)
  salaries.append(salary)
for x,y in zip(names , salaries) :
  print(x)
  print(y)
  employees = {}
  employees[x] = y
print(employees)
