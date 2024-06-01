# Let's just make a basic calculator

# First, lets do the addition
def Addition(x, y):
    return x + y

# Next, we will do the subtraction
def Subtract(x, y):
    return x - y

# After, we will add the divide function
def divide(x, y):
    return x / y

# Lastly, we will add the multiply function
def multiply(x, y):
    return x * y

# Now I got the basic calculator functions, 
# now I need to see how to input numbers that way it will work
# using def(main) will work
# This works where we are inputting numbers
def main():
# Now we need to call the functions from above
# But how?
# Using the if statement, elif, and else statements
# But what do I put in them to make this work
    if  (result == "+"):
        final = Addition(x, y)
        print("The sum of the numbers are: ", final)
    elif (result == "-"):
        final_2 = Subtract(x, y)
        print("The difference of the numbers are: ", final_2)
    elif (result == "/"):
        final_3 = divide(x, y)
        print("The quotient of the numbers are: ", final_3)
    elif (result == "*"):
        final_4 = multiply(x, y)
        print("The product of the numbers are: ", final_4)
    else:
        print("Error")

# There was a lot that I had to change, but I was successful in the end
# I ended up looking for similar problems on Stack Exchange and I asked chatgpt for an explaination
# Once I sae what I was doing wrong it was easy to fix

if __name__ == "__main__":
    x = int(input("Enter a value for X: "))
    y = int(input("Enter a value for y: "))
    result = input("Please select a function: +, -, /, or *: ")
    main()
    Addition(x, y)
    Subtract(x, y)
    divide(x, y)
    multiply(x, y)

# I think there is an easier way to do this,
# but I think once I start doing my own applications/projects
# I can modify it, but I like the feeling of being challenged
# I might make it to an advanced calulator adding sqrt and powers

