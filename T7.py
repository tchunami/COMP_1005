# 1. Dictionary key=1-12, values=Jan-Dec
months = {
    "1" : "January",
    "2" : "February",
    "3" : "March", 
    "4" : "April",
    "5" : "May", 
    "6" : "June",
    "7" : "July",
    "8" : "August",
    "9" : "September",
    "10" : "October",
    "11" : "November", 
    "12" : "December"
}

# 2. Months with odd keys function
def odd_keys():
    for i in months:
        if int(i) % 2 != 0:
            print(months.get(i))

# 3. All months function
def mon_vals():
    for i in months:
        if int(i) != 0:
            print(months.get(i))

#  Calling functions
def main():
    print("The odd months are: ")
    odd_keys()
    print("\nAll the months are:")
    mon_vals()

if __name__ == "__main__":
    main()