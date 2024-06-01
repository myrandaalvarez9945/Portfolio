# We are going to create a Conversion Tool
# From inches to centimeters
# STEPS -
## 1. Enter a number
## 2. See if it is inches or centimeters
## 3. if centimeters, can convert it to inches
## 4. if inches, can convert it back to centimeters
## 5. print the value of what the final conversion is
# FORMULAS -
## inches to centimeters = multiply the given inch value by 2.54 cm
## centimeters to inches = multiply the given centimeter value by 0.393701 inches

x = input("Enter a number please? ")
select = input("Is the number that you entered in inches or centimeters? ")
if select == "inches":
    inch_cent = float(x) * 2.54
    print("The conversion from inches to centimeters is: ", inch_cent, "in centimeters")
elif select == "centimeters":
    cent_inch = float(x) * 0.393701
    print("The conversion of centmeters to inches is: ", cent_inch,"inches")
else:
    print("Error!")

# I can make this more better by adding more
# Conversion tools, but for now I want 
# to keep it the way that it is.
        

