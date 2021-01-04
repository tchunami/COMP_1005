# Tutorial 9 - Interative and recursive
import array as arr

# array with ten elements
my_array = arr.array('u', ['m', 'i', 'n', 'e', 'c', 'r', 'a', 'f', 't', '!'])

def print_interative(my_array):
    for i in my_array:
        print(i) 

def print_recursive(my_array):
    if len(my_array) == 1:
        print(*my_array) # prints the last element of the array
    else:
        print(my_array[0]) # prints the first till second last element of the array
        print_recursive(my_array[1:])
        
def main():
    print("Interative:")
    print_interative(my_array)
    print("Recursive:")
    print_recursive(my_array)

if __name__ == "__main__":  
    main()