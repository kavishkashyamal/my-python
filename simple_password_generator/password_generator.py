import random
import string

character_pool = []
length = int(input("Enter password length : "))


if input("Include lowercase letters? (y/n) : ").lower() == 'y':
    character_pool.extend(list(string.ascii_lowercase))
if input("Include uppercase letters? (y/n) : ").lower() == 'y':
    character_pool.extend(list(string.ascii_uppercase))
if input("Include numbers? (y/n) :").lower() == 'y':
    character_pool.extend(list(string.digits))
if input("Include punctuations? (y/n) :").lower() == 'y':
    character_pool.extend(list(string.punctuation))
if not character_pool:
        print("You must choose at least one type of character!")

else:
     password = ""
     for _ in range(length):
          password += random.choice(character_pool)
          
print(f"Your password is : {password}")