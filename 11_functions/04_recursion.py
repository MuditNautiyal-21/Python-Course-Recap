# Recursion: Occurs when a function calls itself.

# Lets say we want to print out a fibonacci series...0,1,1,2,3,5,8...i.e., first number is 0 and second is 1 then the rest comes from adding the previous 2 values.

'''
Mathematical pattern:

fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1)
fib(3) = fib(2) + fib (1)
fib(n) = fib(n-1) + fib(n-2)
'''

def fib(n):
    # Base case of recursion:
    if (n == 0 or n == 1):
        return n
    
    return fib(n-2) + fib(n-1)

print(fib(6))

# If you want to print each value till the index you want the fibonacci series...
def fibo(n):
    if (n == 0 or n == 1):
        return n
    else:
        f1 = 0
        f2 = 1
        print(f1,f2,sep=", ", end = ", ")
        for i in range(0, n-1):
            f3 = f1 + f2
            print(f3, end = ", ")
            f1 = f2
            f2 = f3
    print("\n")

fibo(6)
fibo(8)