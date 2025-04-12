# A program takes a positive floating-point number as input 
# Outputs an approximation of its square root.

# Author: Joanna Mnich

# I had diificulty to find the way to have answer with one position after comma-(3.8)
# In print, I used round function

# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# https://docs.python.org/3/library/exceptions.html#ValueError
# https://docs.python.org/3/library/functions.html#abs
# https://docs.python.org/3/library/functions.html#round

# Calculate the square root of S using Newton's method
# S(float) The square root of the given number
# tolerance (float): The merging tolerance (default is 1e-6)
# max_iterations (int): Maximum iterations (1000 by default)

def SquareRoot(S, tolerance = 1e-6,max_iterations=1000):

 if S < 0:
    raise ValueError(" Cannot number be a negative value")
 
 if S > 1:
    x = S/2.0

 else :
     x = S/1.0

 for _ in range(max_iterations):
        new_x = 0.5 * (x + (S / x))  # Newton`s` formula


        if abs(new_x - x) < tolerance:
            return new_x
        
        x = new_x 

 return x

number = float(input("Enter number: "))
result = SquareRoot(number)

print(f" The Square Root of {number} is approximately {round(result,1)}")