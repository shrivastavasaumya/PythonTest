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
