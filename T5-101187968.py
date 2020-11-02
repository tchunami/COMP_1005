# Tutorial 5

# 1. file_write()
def file_write():
    text = input("Write 300-400 words onto the file: ")
    try:
        f = open("textfile.txt", "w")
        f.write(text)
        f.close()
    except IOError:
        print("Error.")

# 2. file_read()
def file_read():
    try:
        f = open("textfile.txt", "r")
        print("You are reading the file: \n\n",f.read())
    except IOError:
        print("Write text first.")

# 3. count_stpwords()
def count_stpwords():
    stpwords = ["about", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also", "although" "among", "amongst", "amount", "an", "and", "another", "any", "anyone", "anything", "anyway", "anywhere"]
    f = open("textfile.txt", "r")
    textfile = (f.read().split())
    dec = dict()

    for word in textfile:
        if word in stpwords:
            if word in dec:
                dec[word] += 1
            else:
                dec[word] = 1
    print(dec)

# 4. main() 
def main():
    while True:
        print("""\nChoose a task you would like to do from 1-3:

        1. Write text on the file.
        2. Read data from the file.
        3. Count frequency of stop words in made file.
        """)
        ans = input("Enter your choice here: ")
        if ans=="1":
            file_write()
        elif ans=="2":
            file_read()
        elif ans=="3":
            count_stpwords()
        else:
            print("Bye.")
            break

main()