# My try:

# print("Let's genarate your new password together. ")
# NumberOfDigits = input("How many digits do you want your password to be? (between 6 and 10) ")
# Numbers = input("Do you want numbers? ")
# Letters = input("Do you want letters in it? ")
# CapitalLetters = input("Do you want a capital letter? ")
# Symbols = input("Do you want symbols? ")

# import random

# if Numbers == "yes" :
#     random_number = random.randint(1, 10)
#     random_number2 = random.randint(1, 10)
#     random_number3 = random.randint(1, 10)
#     random_number4 = random.randint(1, 10)

# if Letters == "yes" :
#     Letters = ("abcdefghijklmnopqrstuvwxyz")
#     random_letters = random.choice(Letters)

# if Letters == "no" :
#     Letters = ""

# if CapitalLetters == "yes" :
#     CapitalLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# if CapitalLetters == "no" :
#     CapitalLetters = ""

# if Symbols == "yes" :
#     Symbols = "!@#$%^&*()_+-=[]{}<>,./"

# if Symbols == "no" :
#     Symbols = ""

# print(random_number+random_number2+random_number3+random_number4)
# print(random_letters)
#________________________________________________________________________________
# BlackBox:

import random

def password_generator():
  user_input = input("For a strong password, type 'strong'. For a weak one, type 'weak': ")
  if user_input.lower() == 'weak': 
    return random.choice(['password', 'myname', 'iloveyou', 'goodchoice', 'cocacola', 'oneball', "Letusgo"])

  else:
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJLMNOPQRSTUVWXYZ!@#$%^&*()?1234567890'
    password = ''.join(random.choices(letters, k=(random.randrange(8, 24))))
    return password
print(password_generator())

# names = ['John', 'Jane', 'Alice']
# joined_names = ', '.join(names)

# print(joined_names)
# Output: John, jane, Alice