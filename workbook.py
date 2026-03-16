# city = (input("Enter city: "))
# temp = (input("Enter temp: "))
# print("The temperature in " + str(city) +  " is " + str(temp) + " degrees ")


# vegetable = input("name of vegetable :")
# if vegetable == 'Onion':
#     print('Healthy salad option')
# elif vegetable == 'Potato':
#     print('includes starch')
# else :
#     print('fine!')
    

# name = input('name : ')
# if name == 'manu':
#     print('right name')
# else:
#     print('recheck the name')

#________________________________________________________________________________________________
# i = 1
# while (i <= 10):
#     if ( i % 2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1


# i = 1
# while (i <= 10):
#     if (i % 2 != 0):
#         print(i)
#         i += 1



# word = "The United States of America"
# count = 0
# for ch in word:
#         if( ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'U'):
#             count += 1
# print(count)




# value = int(input("enter the value : "))
# sum = 0   
# for i in range ( 1 ,value+1 ):           
#     sum += i
# print(sum)



age = int(input("enter your age : "))


if age >= 18:
    if (age>=20) :
        print("You can enter.")
    else:
        print("ID required.")
else:
    print("You are underage.")


    def minus (a,b):
    neg = a-b
    print(neg)

minus(9,6)


# bgyjkhu = minus(98,65)
# print(bgyjkhu)


def sum (a, b):
    sum = a + b
    print(sum)
    return sum
    
# unsaved
sum(9,18)

# save
ans = sum(7,9)
print(ans)

