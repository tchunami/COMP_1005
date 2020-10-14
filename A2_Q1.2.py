# Assignment 2, Question 1: User Interface (taking user input)

# Functions:
# 1. Writing text on the file.
def write_file():
    # preset questions to guarantee a 6 line user input text
    text1 = input("\nEnter your NAME, SCHOOL, PROGRAM: ")
    text2 = input("Why did you choose your selected SCHOOL? ")
    text3 = input("Why did you choose your selected PROGRAM? ")
    text4 = input("What would be your next choice for school? Why? ")
    text5 = input("What would be your next choice for program? Why? ")
    text6 = input("What is the meaning of life? ")
    try:
        # opens the .txt file to write
        f = open("assignment2.txt", "w")
        # writes the user input onto .txt file
        f.write(text1 + "\n")
        f.write(text2 + "\n")
        f.write(text3 + "\n")
        f.write(text4 + "\n")
        f.write(text5 + "\n")
        f.write(text6)
        # closes the .txt file
        f.close()
        print("\nText has been succesfully written on the file. \n\n\nYou are now back on the main menu.")
    except IOError:
        print("\nError: file cannot be written.")

# 2. Reading data from file.
def read_file():
    try:
        # opens .txt file to read all contents of the file
        f = open("assignment2.txt", "r")
        print("\nYou are now reading the full text file: \n\n" + f.read(), "\n\nEnd of text. \n\n\nYou are now back on the main menu.")
    except IOError:
        print("\nError: there is no file to be read.")

#3 Search for string and calculate the number of occurences.
def search_file():
    # opens .txt file to read text then start search and figure out the number of occurances.
    f = open("test.txt", "r")
    # reads the lines from the file into a list
    lines = f.readlines()
    while True:
        # get user input and convert to lowercase
        word = input("\nEnter a string to calculate number of occurances in the text: ").lower()
        # initialize count variable
        count = 0
        
        # check each line for occurences and add to count
        for line in lines:
            count += line.lower().count(word)
        
        # no specific text is found on file
        if count == 0:
            print("\nWord not found, try again.")
        # found text on file
        else:
            print("\nThe text chosen,", word, ", occurs", count, "times. \n\n\nYou are now back on the main menu.")
            break

# User interface (menu)
print("Welcome")
while True:
    # menu options
    print("""\nChoose a task you would like to do from 1-4:

    1. Write text on the file.
    2. Read data from the file.
    3. Search for string and calculate the number of occurances.
    4. Quit.
    """)
    ans = input("Enter your choice here: ")
    if ans=="1":
        # 1. Writes text on the file.
        write_file()
    elif ans=="2":
        # 2. Reads the file.
        read_file()
    elif ans=="3":
        # 3. String and number of occurances.
        search_file()
    elif ans=="4":
        # 4. Quit program.
        print("\nGoodbye!")
        quit()
    else: 
        print("\nChoice not valid. Try again.")
