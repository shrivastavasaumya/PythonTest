Assignment 3





# word = str(input("enter the word:         "))       #Q1
# if word == word [::-1]:
#     print("yes")
# else :
#     print("no")


# values = [25, 28, 10, 12, 11]
# s = ((sum(values))/len(values))                        #Q2
# print(s)
# print(type(values))


# line_1 =  [11, 12, 13, 10, 9, 8]    
# line_2 =   [14, 10, 9, 7, 5, 4]                          #Q3                           

# s = set(line_1)
# p = set(line_2)

# k = s.union(p)
# print(k)


# a = set(input("enter the list:         ").split())
# b = set(input("enter the list:         ").split())


# n = a.union(b)
# print(n)

# ------------------------------------------------------------------------- 

# values = (1, 3, 5, 8, 9, 10, 14, 15, 16, 11, 20)             #Q4
# # print(type(values))
# even = []    #----> used list as they are mutable whereas tuples() are not
# odd = []
# for i in values:
#     if i % 2 == 0:
#          even.append(i)  #------> used to add elements one by one into a list while looping.
    
#     else:
#         odd.append(i)

# print("even numbers", even)
# print("odd numbers" , odd)

# ----------------------------------------------------------------
# elements = {

#                                    #Q5
#  "aka": "97",
#  "ana": "84",
#  "nanu": "94",
#  "lalu": "92",                      not done
#  "balu": "86"

# }

# student_names = elements.keys()
# # print(student_names)
# marks = elements.values()
# # print(marks)

# A = elements.update({ input()})
# # B = marks.update({ })

# # C = student_names.get(input())
# D = elements.items() 

# print(A)
# ------------------------------------------------------------------

# words = ["apple", "banana", "kiwi", "cherry", "mango"]

# r = {}                                            #Q6     result[i] = value	Adds/updates dictionary
#                                                                len()  =	Finds length of string
# # for i in words:
#     r[i] = len(i)
# print(r)

# -----------------------------------------------------------------------


# content = input( "enter the string:     ")
# count = content.count(" ")                           #Q7
# print(count)


#  .count(" ")	    Counts spaces
#      " "	        represents a space
# isspace()	        checks if entire string is only spaces
# # she is a new employee, but very punctual.
# -------------------------------------------------------------------------


# list1 = [1, 2, 3, 4] 
# list2 = [5, 6, 7, 8]
# s = set(list1)
# l = set(list2)

# m = s.union(l)
# print(m)                       #Q8

# u = s.intersection(l)
# print(bool(u))

# listp = [1, 2, 3] 
# listj = [3, 4]

# h = set(listj)
# f = set(listp)

# y = h.intersection(f)
# print(bool(y))
# ---------------------------------------------------------------

# z = [1, 7, 5, 8, 9, 5, 5, 7, 1, 0, 2, 3, 2, 3, 4]
# g = set(z)                                                   #Q9  took help from gpt for duplicate part
# duplicates = [i for i in g if z.count(i) > 1]

# print(duplicates)
# -----------------------------------------------------------

# s = input( "enter the string:     ") 

# freq = {}                                  
#                                     #   freq = {}
#                                     #    This will store character counts

#                                     #    Format: {character: frequency}
#                                                                                      #Q10  took help from gpt for duplicate part
                                                                                    
# for ch in s:
#     freq[ch] = freq.get(ch, 0) + 1      
#                                         # freq[ch] → stores count of that character
# print("Unique characters:")
# for ch in freq:
#     if freq[ch] == 1:
#         print(ch)

