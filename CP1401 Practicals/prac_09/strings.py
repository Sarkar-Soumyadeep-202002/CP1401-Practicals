# 6. Processing strings
def question_6(data_strings):
    result=data_strings[0]
    print(result[9:])
    score=data_strings[1]
    print(score[14])
    value=data_strings[2]
    print(value[17:])
    variable=data_strings[3]
    print(variable[39:])
    x=data_strings[4]
    print(x[4:])


def main():
    data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
                    "Something else that's very important = 9.2%", "x = 42%"]
    question_6(data_strings)


main()

#7. Date strings
def date():
    date_of_birth=input('DOB: ')
    print(f'You were born in {date_of_birth[6:]}')
    date1=int(date_of_birth[6:])
    difference=2020-date1
    print(f'You turned {difference} in 2020.')


def main():
    date()


main()


# 8. Subject code strings
def subject_code():
    code=input('Enter subject code: ')
    code=code.upper()
    while code!='':
        if code[2]=='1':
            if code[0:2]=='CP':
                print('That is a first year IT subject.')
            else:
                print('That is a first year subject')
        elif code[2]=='2':
            if code[0:2]=='CP':
                print('That is a second year IT subject.')
            else:
                print('That is a second year subject')
        elif code[2]=='3':
            if code[0:2]=='CP':
                print('That is a third year IT subject.')
            else:
                print('That is a third year subject')
        elif code[3]>='4':
            print('This is a masters or other IT subject')
        code = input('Enter subject code: ')
        code = code.upper()


def main():
    subject_code()


main()


