# Assignment 4 - Merge Sort (no recursion)

import array # Call for array module to create arrays

# Write, read, and storing Math Grades
def create_MathGrades():
    try: 
        math = open("math.txt", "w")
        math.write("66,69,70,73,80,85,90,92,95,99 ")
        math = open("math.txt", "r")
        for i in math:
            math_integer = [] # stores the grades into list
            for j in i [0:-1].split(","): # individualizes each grade using ','
                math_integer.append(int(j)) # makes sures that the appended grades into the list are integers and not string
            print(f"Math list: {math_integer}")
        math.close()

        return math_integer

    except IOError:
        print("Error: creating math grades text file unsuccessful.")

# Write, read, and storing Science Grades
def create_ScienceGrades():
    try:
        science = open("science.txt", "w")
        science.write("60,67,68,72,77,82,89,91,97,98 ")
        science = open("science.txt", "r")
        for i in science:
            sci_integer =[] # stores the grades into list 
            for j in i [0:-1].split(","): # individualizes each grade using ','
                sci_integer.append(int(j)) # appending grades into the list as integers and not string
            print(f"Science List: {sci_integer}")
        science.close()

        return sci_integer
        
    except IOError:
        print("Error: creating science grades text file unsuccessful.")


# Converting both grades lists into arrays
def convert_array(math_list, science_list):
    try:

        math_array = array.array("i", math_list)
        print(f"Math array: {math_array}")

        sci_array = array.array("i", science_list)
        print(f"Science array: {sci_array}")
        return [math_array, sci_array]
    
    except IOError:
        print("Error in converting to an array")

# Merging both Science and Math array into one ascending array
def merge_sort(math_list, science_list):
    try:
        # setting variables
        i = 0 
        j = 0
        math_converted = len(math_list)
        science_converted = len(science_list)

        merged = [] # creating a new list to store merged array

        while ((i < math_converted) and (j < science_converted)):
            if (math_list < science_list): # if math grade is less than science grade append the math grade onto the new list
                merged.append(math_list[i])
                i = i + 1
            else:
                merged.append(science_list[j]) # is science grade is less than math grade append the science grade to the new list
                j = j + 1
        
        while(i < math_converted): 
            merged.append(math_list[i])
            i = i + 1
        
        while(j < science_converted): 
            merged.append(science_list[j])
            j = j + 1
        
        print(f"Both Math and Science grades combined: {merged}")
        return merged
    except IOError:
        print("Error merging arrays.")

# Function call
def main():
    math_list = create_MathGrades() # stores the math grades
    science_list = create_ScienceGrades() # stores the science grades
    converted_arrays = convert_array(math_list, science_list) # stores converted arrays to use for merge_sort function
    merge_sort(converted_arrays[0], converted_arrays[1]) # arguements call for the index of the converted_arrays, using math_list/science_list onto the actual function
    return [math_list, science_list, converted_arrays]

# Call for main()
if __name__ == "__main__":
    main()
