import random 
import string

pass_len = 10
charValues = string.ascii_letters + string.digits + string.punctuation

# list comprehension is use for generating random password

password= "".join([random.choice(charValues) for i in range(pass_len)])

# using for loop to to generate random password

# password = ""
# for i in range(pass_len):
#     password += (random.choice(charValues))

print("Your Password Is:",password)