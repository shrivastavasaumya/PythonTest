# USUAL CODE STRUCTURE

squares = []

for i in range (6):
    squares.append(i*i)

print(squares)


#                                                                    LIST COMPREHENSION 
#                                                       Syntax =    output + iteratble + condition

# WITHOUT CONDITION     
#-------------------

# (Example - 1)

#    output +      iteratble +           condition
#       |               |                   |
sq =   [i*i      for i in range(6)  ]   #(nil)
print(sq)




# WITH CONDITION         
# ----------------
 
# (Example 2 - For odd numbers)
 
sq =   [i*i      for i in range(6)      if i/2 != 0 ]   
print(sq)


# (Example - 3)

nums = [-2, -3, 3, 4, -1, 7] 
nums = [0 if val < 0 else val for val in nums]          # to replace all 'numbers <0' with 'o'
print(nums) 


words = ["hello ", "python", "language"]
words = [val.upper() for val in words]                  # to capitalize each word in a list
print(words)