books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
unique_numbers = []
a = 0
n = len(books)
while a <= n :
  for i in books[a] :
    a += 1
    if i not in unique_numbers :
      unique_numbers.append(i)
print(unique_numbers)