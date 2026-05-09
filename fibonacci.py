#Steve Phillips-Ward
# Fibonacci and Dynamic Programming

def fibonacci(n):
    if n <= 1:
        return n
    
    #Create a list to store values up to n
    fib = [0] * (n + 1)

    #Base cases
    fib[0] = 0
    fib[1] = 1

    #Fill the list using the Fibonacci formula
    for i in range (2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]







def fibonnaci_optimized(n):
    #base case
    if n <= 1:
        return n
    
    #keep track of the last two Fibonacci numbers
    a, b = 0, 1

    # Compute from 2 to n
    for i in range(2, n + 1):
        # new number is the sum of the previous two
        c = a + b
        #shift the last two numbers
        a = b
        b = c

    return b
    
#Request for input

n = int(input("Enter the Fibonacci index: "))

#Print the Results

print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
print(f"The {n}th Fibonacci number is: {fibonnaci_optimized(n)}")