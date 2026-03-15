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
