import array

def main():
    my_array = array.array("i", [9,3,8,2,1,5,4,0,6,7]) # random value array
    print(f"\nUnsorted array: {my_array}")

    sorted = selection_sort(my_array) # call for sorted
    print(f"Sorted array: {sorted}\n")

# sort algorithm 
def selection_sort(my_array):
    for i in range(len(my_array)):
        minPos = i
        for j in range(i+1, len(my_array)):
            if my_array[minPos] > my_array[j]:
                minPos = j
        
        my_array[i], my_array[minPos] = my_array[minPos], my_array[i]
    return my_array

# call for main()
if __name__ == "__main__":
    main()