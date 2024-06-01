# So, I want to create a simulation of paper, rock, or scissors
# The idea is the user will input what they want
# After it will go through a bunch of conditional statements to see if they pick
# Can defeat the other user

user = input("User select one: Rock, Paper, Scissors? ")
user_2 = input("User_2 select one: Rock, Paper, Scissors? ")

if(user == 'Scissors'):
    print("User selected Scissors")
    if (user_2 == 'Scissors'):
        print("User_2 Selected Scissors")
        print("Tie, Try Again")
    elif (user_2 == 'Rock'):
        print("User_2 Selected Rock")
        print("User_2 wins!")
    elif (user_2 == 'Paper'):
        print("User_2 Selected Paper")
        print("User wins")
    else:
        print("What are you doing?!")

if(user == 'Paper'):
    print("User selected Paper")
    if (user_2 == 'Paper'):
        print("User_2 Selected Paper")
        print("Tie, Try Again")
    elif (user_2 == 'Rock'):
        print("User_2 Selected Rock")
        print("User wins!")
    elif (user_2 == 'Scissors'):
        print("User_2 Selected Scissors")
        print("User_2 wins")
    else:
        print("What are you doing?!")

if(user == 'Rock'):
    print("User selected Rock")
    if (user_2 == 'Rock'):
        print("User_2 Selected Rock")
        print("Tie, Try Again")
    elif (user_2 == 'Scissors'):
        print("User_2 Selected Scissors")
        print("User wins!")
    elif (user_2 == 'Paper'):
        print("User_2 Selected Paper")
        print("User_2 wins")
    else:
        print("What are you doing?!")

# In the end it was a success, definately an easier way to do this, 
# I like challenging myself and letting myself think 
# I could've used random.choice from a forum, but I want two users to play
# Is there an advantage, of course because you can see what the first User
# chooses, but I will find a way to fix that
