# Tutorial 4

def generate_array():
    arr = []

    for i in range(1, 11):
        arr.append(i)
    return arr

def sum_div_by_three(arr):
    totalVal = 0 

    for x in arr:
        if x % 3 == 0:
            totalVal += x
    return totalVal
 
def find_min_max(arr):
    min = arr[0]
    max = arr[0]


    for y in range(len(arr)):

        if arr[y] > max:
            max = arr[y]

        if min > arr[y]:
            min = arr[y]

    return min, max    



def swap(arr, min, max):
    minPos = arr.index(min) 
    maxPos = arr.index(max)

    # print("maxpos: ", maxPos)

    arr.remove(min)
    arr.remove(max)

    arr.insert(minPos, max)
    arr.insert(maxPos, min)

    return arr


def main():

    print("The array is:")
    arr = generate_array()
    print(arr)

    print("The sum is:")
    sum = sum_div_by_three(arr)
    print(sum)

    print("The min, max, respectively:")
    min, max = find_min_max(arr)
    print(min, max)

    print("The swap of min and max:")
    swap_val = swap(arr, min, max)
    print(swap_val)


main()