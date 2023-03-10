def print_parity(number,check,parity):
    if check==False:
        print(f'Parity of {number} should be 0: {parity} ')
    else:
        print(f'Parity of {number} should be 1: {parity} ')

def calculate_parity(number):
    parity=number%2
    return parity

def check_odd(number):
    if (number%2==0):
        return False
    else:
        return True

def main():
    number=int(input('Enter the number: '))
    parity=calculate_parity(number)
    check=check_odd(number)
    print_parity(number,check,parity)

main()

