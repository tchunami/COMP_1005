# Assignment 2, Question 1: User Interface

# 1. Writing text on the file.
def write_file():
    try:
        f = open("assignment2.txt", "w")
        f.write("According to all known laws of aviation, \nthere is no way a bee should be able to fly, \nIts wings are too small to get its fat little body off the ground. \nThe bee, of course, flies anyway \nbecause bees dont care what humans think is impossible. \nYellow, black. Yellow, black. \nYellow, black. Yellow, black. \nOoh, black and yellow!")
        f.close()
        print("\nPreset text has been succesfully written on the file. Choose a task from 2-4.")
    except IOError:
        print("\nError: file cannot be written.")

# 2. Reading data from file.
def read_file():
    try:
        f = open("assignment2.txt", "r")
        print("\nYou are now reading the full text file: ""\n\n",f.read(), "\n\nTo read full text again, enter: 2, to search for string, enter: 3, to Quit, enter: 4.")
    except IOError:
        print("\nError: there is no file to be read.")

#3 Search for string and calculate the number of occurrences.
def search_file():
    f = open("assignment2.txt").read()
    while True:
        word = str(input("\nEnter a string to calculate number of occurances in the text: "))
        count = f.count(word)
        if count == 0:
            print("\nWord not found, try again.")
        else:
            count = f.count(word)
            print("\nThe word chosen, ", word, ", occurs ", count," times. To read full text, enter: 2, or to Quit, enter: 4.")
            break

# User interface (menu)
while True:
    print("""
    1. Write preset text on the file.
    2. Read data from the file.
    3. Search for string and calculate the number of occurances.
    4. Quit.
    """)
    ans = int(input("Choose a task you would like to do from 1-4: "))
    if ans==1:
        # 1. Writes text on the file.
        write_file()
    elif ans==2:
        # 2. Reads the file.
        read_file()
    elif ans==3:
        # 3. String and number of occurances.
        search_file()
    elif ans==4:
        # 4. Quit program.
        print("\n Goodbye!")
        quit()
    else: 
        print("\n Choice not valid. Try again.")
