'''
Demonstrates the ability to randomly insert characters into a string that meets specific password requirements.

Input: Command Line Argument Optional Length
Generate a password ( of a given length if provided) that meets the password requirements from Project 1

Output: A Valid Password

Example:
U:\private\generator> python PasswordGenerator.py -h
usage: PasswordGenerator.py [-h] [-length <Length of requested password in whole number>]

optional arguments:
    -h --help               show this message and exit
    -length <Length of requested password in whole numbers>

U:\private\generator> python PasswordGenerator.py -length 30
Creating new password, please wait:
n7rHUY<2<15x\n9lFDz@"6I+7FvcC"
'''
import random
import string
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', metavar="", type=int, default=14,
                    help="If you want to input a password greater than 14 characters, please specify the number of integers you want it to be.")

p = parser.parse_args()

print('''\n\n\nThis is your standard password generator. It will create a password for you that a minimum will meet the following requirements:

1. Password must be at least 14 characters in length
2. Password must contain at least one character from each of the following character sets:
    * Uppercase characters
    * Lowercase characters
    * Numerical digits
    * Special characters ==> !"#$%&\'()*+,-./:;<=>?@[\\]^_'{|}~
3. Password cannot contain more than three consecutive characters from the same character set.

If you want to generate a password that is greater than 14 characters long, please utilize the '-l' or '--length' option of this program.

Thank you and have a wonderful day!\n\n''')

pw_length = 14
charcount = 0
goodpasswd = 50
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special = string.punctuation
p_list = (uppercase + lowercase + digits + special)
mypw = ""

# This is only generating a 14 character password at random from my list of upper, lower, digits, and special characters
# The for loop will only loop through 14 times
for i in range(pw_length):
    # This next_index variable is defining a random index number from the list of characters in my p_list variable
    next_index = random.randrange(len(p_list))
    # this is what is actually creating my password. It will add onto the mypw variable 14 times, each time grabbing a random index number from my p_list string and concatenating that with what was there previously. It will loop 14 times as defined in my outer for loop.
    mypw = mypw + p_list[next_index]

# Can I just have my password checker check to see if the randomly generated password matches the requirements, and if it doesn't generate a new one until it does?
    # This part is checking to see that I have at least one of each character set in the generated password
    if any(i.isupper() for i in mypw):
        if any(j.islower() for j in mypw):
            if any(k.isdigit() for k in mypw):
                if any(char in special for char in mypw):
                    pass
                else:
                    goodpasswd -= 1
            else:
                goodpasswd -= 1
        else:
            goodpasswd -= 1
    else:
        goodpasswd -= 1
    # This part is checking for more than 3 instances of a character.
    for char in mypw:
        if char in uppercase:
            # The charcount variable is there to count the amount of times uppercase is found and iterates it by one each tie. The intial value is set at the top of the script.
            charcount += 1
            # The good passwd variable is there as an 'and' condition because I want the loop to stop when I encounter this nested 'if' condition. So basically, if in the user-inputted password, I find the uppercase character more than 3 times in a row AND my goodpaswd variable is still set to what I initially set it at the top, then I want to print out my False statment and exit the program
            if charcount >= 4 and goodpasswd == 50:
                goodpasswd -= 1
            else:
                pass
        else:
            charcount = 0
    charcount = 0
    for char in mypw:
        if char in lowercase:
            charcount += 1
            if charcount >= 4 and goodpasswd == 50:
                goodpasswd -= 1
            else:
                pass
        else:
            charcount = 0
    charcount = 0
    for char in mypw:
        if char in digits:
            charcount += 1
            if charcount >= 4 and goodpasswd == 50:
                goodpasswd -= 1
            else:
                pass
        else:
            charcount = 0
    charcount = 0
    for char in mypw:
        if char in special:
            charcount += 1
            if charcount >= 4 and goodpasswd == 50:
                goodpasswd -= 1
            else:
                pass
        else:
            charcount = 0

if goodpasswd == 50:
    print(mypw)
else:
