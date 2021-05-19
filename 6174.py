# Sorted Number
def SN(str):
    return int(''.join(sorted(list(num))))


# Reverse Sorted Number
def RSN(str):
    return int(''.join(sorted(list(num), reverse=True)))


while True:
    number = input('Enter 4 digits number:')
    num = number
    # Number that entered must be 4 digit and not begin with 0 and not contain a letter.
    if len(num) == 4 and num[0] != '0' and num.isdigit():
        counter = 1
        while num != '6174':
            subtract = RSN(num) - SN(num)
            print(f'{counter}.{RSN(num)} - {SN(num)} = {subtract}')
            if subtract == 0:
                print('''This number can't reach 6174''')
                break
            # Adding 0 to numbers with 3 digits.
            if subtract < 1000:
                subtract = subtract * 10
            counter += 1
            num = str(subtract)
    else:
        print('This number is not acceptable!')
