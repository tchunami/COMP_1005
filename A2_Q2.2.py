# Assignment 2, Question 2: Stars
spaces = [" " * 69, " " * 68, " " * 66, " " * 62, " " * 54]
stars = ["* ", "* " * 2, "* " * 4, "* " * 8, "* " * 16]

i=0 # List Index
for x in spaces:
    print(x,stars[i])
    i+=1