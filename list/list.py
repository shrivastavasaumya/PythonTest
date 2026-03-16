fruits = ["apple", "banana", "mango"] 
fruits2 = ["mango" , "kiwi"]
fruits.extend(fruits2)
print(fruits)

fruits = ["apple", "banana", "mango"] 
fruits2 = ("mango" , "kiwi")
fruits.extend(fruits2)
print(fruits)

fruits = ["apple", "banana", "mango"] 
fruits2 = ("mango" , "kiwi")
fruits.append(fruits2)    # here in 'append' you are inserting fruits2 as a whole new list ['apple', 'banana', 'mango', ('mango', 'kiwi')]
print(fruits)


res = []
for i in range (1, 11):
    res.append(i ** 2)
print(res)


text = "Python list comprehension is powerful and consise"
if len(i) in text > 5:
    print(i.upper)


tree = ['Pepal', 'Neem', 'Banyan', 'Banana', 'Apple']
x = 'Banana'
idx = 0 
for name in tree:
    if (name == x):
        print(x, "at index" idx)
        break
    idx += 1















