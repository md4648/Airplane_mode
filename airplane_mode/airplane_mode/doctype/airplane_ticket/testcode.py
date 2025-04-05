
import random

uppercase_letters = "ABCDE"

seat=""

ranome_letter=random.choice(uppercase_letters)
random_digit = str(random.randint(0, 100))

seat=str(random_digit+ranome_letter)

print("random digit is" , random_digit)

print("random letter is ",ranome_letter)
print(seat)



#   67156