# randomly generate a password containing:
#     upper letter
#     lower letter
#     number 0-9
#     special characters: ~`!@#$%^&*()_<>?/

from random import randint, choice

password = ""

char = "~`!@#$%^&*()_<>?/"

for i in range(20):
    A = [chr(randint(65, 90)), chr(randint(97, 122)), randint(0, 9), choice(char)]
    password = password + str(choice(A))

print(password)