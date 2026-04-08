
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