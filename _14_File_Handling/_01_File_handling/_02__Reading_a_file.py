
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
