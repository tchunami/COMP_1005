# Assignment 5

# Fibonacci sum using recursion
def fib_sum(a,n):
    if n == 0: # base case
        return 0
    else:
        x = ((a**n) * (n/(n+1))) # Fibonacci sequence
        y = fib_sum(a, n-1) # calls for function until base case is met
        return x + y  

def main():
    # while loop for easy user access for invalid inputs
    while True:
        a = input("\nEnter the constant 'a' value you would like to calculate in the Fibonacci Sequence: ") # constant calue of a
        n = input("Enter the Limit 'n' in which you would like the sequence to run: ") # upper limit
    
        try:
            # turns string input into floats
            a, n = float(a), float(n)
            
            # parameters to catch negative integers and zeros
            if a <= 0 or n <= 0: 
                print("\nInvalid number, try a positive number greater than zero(0).")
            # prints the result of user input
            else:
                result = fib_sum(a,n) # calls for function storing into result variable for result print
                print(f"\nFor the constant value of: {a}, and the limit value of: {n}. \nThe final result is: {result}\n")
                quit()

        except ValueError: # catches all invalid characters
            print("\nError: your input contains an invalid character(s).")

if __name__ == "__main__":
    main()