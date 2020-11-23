m_add = input("Enter your mail adress :")
m_add = str(list)
m_add = m_add.lower()
while True :
  if m_add == "ceng113@example.com" :
    break
  elif m_add != "ceng113@example.com" :
    m_add = input("Enter your mail adress again :")
  else :
    print("Your E-Mail is correct")
    break