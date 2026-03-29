def values(a,b):
    print((sum([a,b])**2))
    
# or this way

def sukm(a,b):
    return(a+b)**2
#____________________________________

# def hill(k,j):
#     if j == 0:
#         return('not defined')
#     else:
#         y = ([k/j])
#         return(y)
   
# print(hill(8,9))
 
 #or

# def kol(k,j):
#     if j != 0:
#         return k / j
    

# print(kol(8,0))
# print(kol(2,4))

#____________________________________

# def hill(k,j):
#     if j == 0:
#         print('not defined')
#     else:
#         y = ([k/j])
#         print(y)
#     return 

# hill(8,9)

# print(len.__doc__)
# print(abs.__doc__)
# print(print.__doc__)

# def sukm(a,b):
#     '''sum the two values and squares the sum'''
#     return(a+b)**2
# print(sukm.__doc__)

# def new_sum(a,b,c):
#     return(sum([a,b,c]))

# print(new_sum(4,5,1)) 

# def main_outer():
#     x = 100
#     def outer():
#         x = 10
#         def inner():
#             nonlocal x          
#             x = 20
#             print(f"inner function, x = {x}")
#         print(f"before inner function, x = {x}")
#         inner()
#         print(f"after inner function, x = {x}")
    
#     outer()


# # how to call
# main_outer()

# def square(x):
#        return x ** 2

# numbers = [1, 2, 3, 4, 5]
# squared_numbers =map(square, numbers)
# print(list(squared_numbers))

# students = [('charlie', 78) , ('alice', 85), ('bob', 90)]
# print(sorted(students))

# def fact(n):
#     digit = 1
#     for i in range(1, n+1):
#         digit = (digit*i)
#     return digit

# a = fact(4)
# print(a)
   
# # via recursion

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)

# print(fact(5))

def countdown(n):
    if n == 0:
        return
    
    countdown(n - 1)
    print(n)
countdown(6)

# import sys
# print(sys.getrecursionlimit())

