

f = open("sample.txt", "w")
f.write("This function will overwrite the data of the file \n that is will remove the the " \
         "existing data and will replace it \n with the new data")
f.close()



#                      OR



# with keyword (by default it automatically closes the file after all Operations)

with open("sample.txt", "r") as f:        #['f' is just a variable for file a general format, can be anyother also ]
    print(f.read())
