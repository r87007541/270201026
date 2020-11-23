students_number = int(input("How many students :"))
grades = []
x = 0
for i in range(students_number) :
  print ("Student" , str(i+1))
  mid_1 = int(input("enter your 1st midterm :"))
  mid_2 = int(input("enter your 2nd midterm :"))
  final = int(input("enter your final exam :"))
  grades.append([mid_1,mid_2,final])
print(grades)
average_gr = []
for sub in grades :
  average_gr.append(sub[0]*0.3 + sub[1]*0.3 + sub[2]*0.4)
print(average_gr)
