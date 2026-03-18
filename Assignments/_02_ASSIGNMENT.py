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
