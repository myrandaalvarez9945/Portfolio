# I want to the user to put the number of characters they would like;
# I did use documentation because it is very straight forward
# I could build off of this and make it into a encrpyted password for sites to be
# able to use.

import random
import string

character_count = int(input("Please select the number of characters you would like: "))
include_letters = input("Do you want to include letters? (yes/no): ").lower() == 'yes'
include_digits = input("Do you want to include digits? (yes/no): ").lower() == 'yes'
include_punctuation = input("Do you want to include punctuation? (yes/no): ").lower() == 'yes'

characters = ''
if include_letters:
    characters += string.ascii_letters
if include_digits:
    characters += string.digits
if include_punctuation:
    characters += string.punctuation

password = ''
for i in range(character_count):
    password += random.choice(characters)

print("Random password is:", password)