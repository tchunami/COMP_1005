# Assignment 4 - Merge Sort (no recursion)

import array

# 1-Read the math.txt file and store the grades into a list called math list
def create_MathGrades():
    try: 
        math = open("math.txt", "w")
        math.write("66,69,70,73,80,85,90,92,95,99 ")
        math = open("math.txt", "r")
        for i in math:
            math_integer = []
            for j in i [0:-1].split(","):
                math_integer.append(int(j))
            print(f"Math list: {math_integer}")
        math.close()

        return math_integer

    except IOError:
        print("Error: creating math grades text file unsuccessful.")

# 2-Read the science.txt file and store the grades into list called science list
def create_ScienceGrades():
    try:
        science = open("science.txt", "w")
        science.write("60,67,68,72,77,82,89,91,97,98 ")
        science = open("science.txt", "r")
        for i in science:
            sci_integer =[]
            for j in i [0:-1].split(","):
                sci_integer.append(int(j))
            print(f"Science List: {sci_integer}")
        science.close()

        return sci_integer
        
    except IOError:
        print("Error: creating science grades text file unsuccessful.")


# 3-Convert each list into an array.The data in each array must be of an Integer type
def convert_array(math_list, science_list):
    try:

        math_array = array.array("i", math_list)
        print(f"Math array: {math_array}")

        sci_array = array.array("i", science_list)
        print(f"Science array: {sci_array}")
        return [math_array, sci_array]
    
    except IOError:
        print("Error in converting to an array")

# 4-Use the merge sort algorithm to combine the two arrays into a new third array such that the elements in the new array are sorted in an ascending order
def merge_sort(math_list, science_list):
    try:
        i = 0 
        j = 0
        math_converted = len(math_list)
        science_converted = len(science_list)

        merged = []

        while ((i < math_converted) and (j < science_converted)):
            if (math_list < science_list):
                merged.append(math_list[i])
                i = i + 1
            else:
                merged.append(science_list[j])
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
    math_list = create_MathGrades()
    science_list = create_ScienceGrades()
    converted_arrays = convert_array(math_list, science_list) 
    merge_sort(converted_arrays[0], converted_arrays[1])
    return [math_list, science_list, converted_arrays]

# Call for main()
if __name__ == "__main__":
    main()
