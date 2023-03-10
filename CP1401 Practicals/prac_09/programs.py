# 1. Print a line
def print_hyphen():
    print('-'*40)


def question_1():
    print_hyphen()


question_1()

# 2. Is it even
def is_even(number):
    if number%2==0:
        print(f'{number} is even.')
    else:
        print(f'{number} is odd.')


def question_2():
    number=int(input('Enter a number: '))
    is_even(number)


question_2()

# 3. Non-empty String
def nonempty_string():
    name=input('Enter your name: ')
    while(name==''):
        print('Invalid input')
        name = input('Enter your name: ')
    birth_place=input('Enter your birth place: ')
    while (birth_place == ''):
        print('Invalid input')
        birth_place = input('Enter your birth place: ')
    print(f'Hi {name} from {birth_place}')


def question_3():
    nonempty_string()


question_3()

# 4. List
def list_of_numbers(min,max):
    numbers=[]
    for number in range(min,(max+1)):
        numbers.append(number)
    print(numbers)


def question_4():
    min=int(input('Minimum number: '))
    max=int(input('Maximum number: '))
    while(max<=min):
        print(f'Your Maximum should be greater than {min}.')
        max=int(input('Maximum number: '))
    list_of_numbers(min,max)


question_4()

# 5. Subject code
def subject_code():
    codes = []
    code=input('Enter subject code: ')
    while code!='':
        while(len(code)!=6):
            print('Invalid code')
            code = input('Enter subject code: ')
        codes.append(code)
        code = input('Enter subject code: ')
    print(f'You take these {len(codes)} subjects')


    for item in codes:
        print(item)
    if 'CP1401' in codes:
        print('You are cool!')


def question_5():
    subject_code()


question_5()

