
'''weight = int(input(18))
if weight >= 15:
    print("Hello Arvind")
    print("sit here")
else : print("Hey unknown")'''



# height = int(input())cd
# if height >= 165:
#    print('you are tall')
# else : print('drink more milk')

# temp = 15175

# is_snowing = True

# if temp < 10:
#     print('It is freezing')
#     print('Wear a heavy coat')
#     if is_snowing:
#      print('And don\'t forget your boots!')
# print('Have a nice day!')

# WHILE LOOP
# (My code)
# x = 1 
# while x <= 500:
#     print("Radhe Radhe", x)
#     x += 1
#     if x == 252:
#         break

#                            {OR}

# x = 1
# while x <= 500:
#     if x == 11:
#         break
#     print("Radhe Radhe", x)
#     x += 1

# x = 10
# while x >= 1:
#     print(x)
#     x -= 1

# for i in range(5):
#     print("Hey Shinchan", i)
# i = 10
# for i in range(11,1,-1):
#     print("Hey Shinchan", i)

# print(list(range(10)))
                                                
                                                          
                                                          
                                                          #ASSIGNMENT 1
# name = input(" enter name: ")
# age = input(" enter age:  ")                      Q1 
# stmt =  "Hello "+  name + ", you are " + age +" years old !"
# print(stmt)




# a = input(" enter a: ")
# b = input(" enter b: ")                           Q2

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)



# d = float(input(" enter integer_1: "))
# f = float(input(" enter integer_2: "))          Q3
# e = float(input(" enter float: "))

# avg = (d+e+f)/3
# print(avg)


# b = input("enter the value: ")                   Q4

# print(int(b))
# print(bool(b))
# print(str(b))


# x = 10 + 3 * 2 ** 2                              Q5 
# print(x)                 (BODMAS AND PEMDAS)


# x = input("enter the value: ")
# y = input("enter the value: ")

# temp = x                                           Q6 ****
# x = y
# y = temp

# print(x)
# print(y)


# temp = float(input("enter value in celsius: "))    Q7 ****
# FahrenheitTemp = (temp*(9/5))+ 32
# print(FahrenheitTemp)



# radius = int(input('enter value of radius: '))     Q8 **** 
# area = 3.14 * radius*radius
# print(area)

# radius = int(input('enter value of radius: '))       
# area = 3.14 * radius**2                         (Here, the input which was in the form of string can't be converted
# print(area)                                   in float or int, so we wrote int() additionally to convert the final string value)



# p = float(input("enter value of principal : " ))
# r = float(input("enter value of rate : " ))
# t = float(input("enter value of time : " ))          Q9

# SI = (p*r*t)/ 100
# print(SI)


# k = float(input("enter a float value : " ))

# print(int(k))

# decNum = (float(k))-(int(k))
# print(f"{decNum:.2f}")                               Q10



                                           #    ASSIGNMENT 2
# salary = int(input("enter your salary: "))
# if salary < 30000:
#     print('5%')
# elif ( salary >= 30000 and salary < 70000) :                 Q1 ****
#     print('15%')
# else:
#     print('25%')

# def work():
#     print("hello chan !")

# work()



# def series(a = 0, b = 0):
#     for i in range(a, b + 1):                       **** Q2  used built in function and return in loop
#      if i % 2 == 0:
#       print(i)         
    
# series(a= 1, b = 10) 



# def number(n):
#  for ch in str(n):                                     **** Q3 We have to convert 'n' to a string because integers cannot be iterated in a loop, but strings can.
#     print(ch)


# #call
# number(98750)



# def count(word):
#     count = 0 
#     for ch in str(word) :                              **** Q4 How to add a string which' = answer' with count output
#        count += 1
#     print(count)


# count(45280)
# print('answer')



# def sum_of_digits(n):
#     s = 0
#     for digit in str(n):                                **** Q5  (mistake made- Wrong loop)
#         s = s + int(digit)
#     return s

# print(sum_of_digits(1234))



# for i in range (1, 101):
#     if i % 3 == 0 and i % 5 == 0:                        ****Q6
#      print(i)




# x = 1
# while int(input(" user's input ")) >= 1:
#     print('positive')                                   ERROR CODE
#     if str(input) == 'Quit':
#      break
# else:
#     print("negative")




# while True:
#     user_input = input("Enter a number or Quit: ")

#     if user_input == "Quit":
#         break                                                  ***** Q7

#     num = int(user_input)

#     if num >= 0:
#         print("Positive")
#     else:
#         print("Negative")


# def calculator(a, b, operation):
#     if operation == '+':
#         return a+b
#     elif operation == '-':
#         return a -b
#     elif operation == '*':                                     **** Q8
#         return a *b
#     elif operation == '/':
#         return a / b
#     else :
#         return ' incorrect operation '
    
# print(calculator(4,5,'*'))
 



# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return "True at ", i                           **** Q9
#     return 'False'


# print(is_prime(n = 29))
# print(is_prime(n = 94))




# i = int(input(" enter the value: "))

# if i  > 45 :
#     print("Too high")                  **** Q10 
# if i  < 45:
#     print("Too low")
# if i == 45:
#     print("Correct!")
 

# i = int(input(" enter the value: "))

# if i  > 45 :
#     print("Too high")                 
# elif i  < 45:
#     print("Too low")
# else:
#     print("Correct!")
