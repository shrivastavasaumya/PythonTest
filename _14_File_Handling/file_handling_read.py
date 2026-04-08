
#                                                File input & output
#                                                [ File operators ]

#                                                  To read the whole file together
#                                                 --------------------------------
f = open("sample.txt", "r")                       
data = f.read()
print(data)
f.close                          # close the file properly



# OUTPUT :-

# This is a sample document
# for the topic of file input and output
# to understand how to open and close a file
# in python language and to learn 
# reading and overwriting on it 


#------------------------------------------------------------------------------------------------------

f = open("sample.txt", "r")
data = f.readline()                           # reading line-by-line
print(data)          # @ 1st call               ---------------------

data = f.readline()                            # no. of times the lines are called = that much lines will get printed
print(data)          # @ 2nd call              # here we called it 3 times so 3 lines got printed

data = f.readline()
print(data)          # @ 3rd call


f.close

#-------------------------------------------------------------------------------------------------------
# OUTPUT :-

# This is a sample document

# for the topic of file input and output

# to understand how to open and close a file

#-------------------------------------------------------------------------------------------------------

#                                                Word search
#                                                ------------

data = True          #  [have to initialize a value here, which will give 'true' at the start]
line = 1             #  line number at starting
word = "python"

with open ("sample.txt", 'r') as f:
    while data :
        data = f.readline()
        
        if( word in data):
            print(f"{word} found at line {line}")

        line += 1         #line updater


# OUTPUT :-
# python found at line 4   [Note- python is a case sensitive language, so be careful of the casing of the word searched]

#-------------------------------------------------------------------------------------------------------

#                                                        Exception handling
#                                                       --------------------

#  When we run a code we often gets error & cause of which the code stops, but sometimes we can predict the error python can encounter
#  i.e which error can happen
#  based on different inputs [try, except, else, finally]



try:                                                    # try + except = writes any possible exception under head except
    x = int(input("enter x : "))
    ans = 10 / x


except ZeroDivisionError:                               # except = checks particular exceptions which can occur and how to handle that error
    print(f"Division by 0 : not possible")
# division by '0' can raise an error

except ValueError:                                      # division by a 'string' can raise an error  
    print("Invalid input")

else:                                                   # if no error occurs then, else 
    print(f"answer = {ans}") 

finally:                                                # prints irrespective of whether the exception/error has been thrown or not
    print("End of the program")
