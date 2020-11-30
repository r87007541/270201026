eq1 = input("Enter the first equation:\n")
eq1 = list(eq1)
b_eq1 = eq1.index("=")
les_eq1 = []
res_eq1 = []
eq1_res_str = ""
eq1_les_str = ""
for _ in eq1[:b_eq1] :
    les_eq1.append(_)
for i in les_eq1 :
    eq1_les_str += i
print("Equation 1's Left-End side is :" , eq1_les_str)
for _ in eq1[b_eq1:] :
    res_eq1.append(_)
for i in res_eq1 :
    eq1_res_str += i
    eq1_res_str = eq1_res_str.replace("=" , "")
print("Equation 1's Right-End side is : " , eq1_res_str)
x_index_eq1 = eq1_les_str.index("x")
y_index_eq1 = eq1_les_str.index("y")
coeff_x_eq1 = ""
for i in eq1_les_str[x_index_eq1::-1] :
  coeff_x_eq1 += i
  if i == "+"  or i == "-" :
    break
coeff_x_eq1 = list(coeff_x_eq1)
coeff_x_eq1.remove("x")
coeff_x_eq1.reverse()
coeff_x_eq1_f = ""
for i in coeff_x_eq1 :
  coeff_x_eq1_f += i
print("In equation 1 coefficient of X is : " , coeff_x_eq1_f)
coeff_y_eq1 = ""
for i in eq1_les_str[y_index_eq1::-1] :
  coeff_y_eq1 += i
  if i == "+" or i == "-" :
    break
coeff_y_eq1 = list(coeff_y_eq1)
coeff_y_eq1.remove("y")
coeff_y_eq1.reverse()
coeff_y_eq1_f = ""
for i in coeff_y_eq1 :
  coeff_y_eq1_f += i
print("In equation 1 coefficient of Y is : " , coeff_y_eq1_f)