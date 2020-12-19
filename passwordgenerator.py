#for random numbers,symbols,etc
import random

#password in lowercase
lowercase = 'abcdefghijklmnopqrstuvwxyz'

#password in uppercase
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#password in numbers
numbers = '0123456789'

#password in symbols
symbols = ',./;(){}[]""!@#$%^&*'

#adds all of them
generate_all = lowercase + uppercase + numbers + symbols

#the length of the password to be generated
length = int(input("Enter the length of the password you want: "))

#join all characters and processes the entered length
password = "".join(random.sample(generate_all,length))

#prints generated password
print(password)
