import math as maths #because i'm british

def fibonacci(n): #returns the nth fibonacci number
    a, b = 0, 1
    for i in range(n+1):
        a, b = b, a+b
    return a

fibonacci_length = 1 #keeps track of the length of the number we're on
current_number = 1 #current fibonacci number
num_iterations = 0

while fibonacci_length < 1000:
    fibonacci_length = len(str(current_number))
    current_number = fibonacci(num_iterations+1)
    num_iterations += 1

print(num_iterations)