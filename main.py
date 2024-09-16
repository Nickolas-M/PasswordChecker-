
def main():

    password = input('\nPlease enter a password to check its strength: ')

    # Checking password length
    if len(password) < 14:
        print('Password must contain atleast 14 characters')
        exit(1)
    
    # Checking for atleast one Uppercase letter
    # Checking for atleast one lowercase letter
    # Checking for atleast one number
    # Checking for atleast one special character
    upper = 0
    lower = 0
    number = 0
    special_char = 0
    special_characters = "!@#$%^&*()_-+=/\:;}{]["
    
    for x in password:
        if x.isupper():
            upper = 1
        elif x.islower():
            lower = 1
        if x.isnumeric():
            number = 1
        for y in special_characters:
            if x == y:
                special_char = 1

    if lower == 0 or upper == 0:
        print('Password must contain at least one UPPERCASE and one LOWERCASE letter')
    elif number == 0:
        print('Password must contain at least one NUMBER')
    elif special_char == 0:
        print('Password must contain at least one SPECIAL character (!@#$%^&*()_-+=/\;}{:][)')
    else:
        word_check = wordlist(password)
        if word_check == 1:
            print('\nPassword is very strong!\n')
        elif word_check == 0:
            print('\nPassword was found on the wordlist please choose another password\n')

def wordlist(check):

    # Checks if the password is on the wordlist
    file = open("commonpasswords.txt","r")
    data = file.read()
    lines = data.splitlines()

    count = 0
    while count < len(lines):
        if lines[count] == check:
            return 0
        count = count + 1
    return 1

if __name__ == '__main__': 
    main()


