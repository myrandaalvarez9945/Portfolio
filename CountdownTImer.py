# So, we are going to create a countdown timer
# I have an idea because I watched a youtube video
# I want to do it different
# I know we have to use divmod though
# Lets try to use a while loop
# Maybe to be an addon, we can incorporate minutes and hours
import time

def count_down(timer):
    while timer:
        divmod(timer, 60)
        print(timer)
        print(timer, end="\r")
        time.sleep(1)
        timer -= 1
        
    print("Timer done")

timer = input("Enter the time in seconds: ")

count_down(int(timer))



