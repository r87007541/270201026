thefile = open("tryouts/sample.txt","r")
lines_all = []
for i in thefile.readlines() :
  lines_all.append(i)
print(lines_all)
username = "ayse;5678;ali,ahmet\n"
username_index = lines_all.index(username)
lines_all[username_index] = lines_all[username_index].replace("\n","")+",ovgu"+"\n"
print(lines_all)
thefile = open("tryouts/sample.txt","w")
thefile.writelines(lines_all)
thefile.close()
thefile = open("tryouts/sample.txt","r")
print(thefile.read())