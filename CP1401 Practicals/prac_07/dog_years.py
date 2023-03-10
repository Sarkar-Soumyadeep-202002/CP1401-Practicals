def dogyears(age):
    if age<=2:
        Age=age*10.5
    else:
        Age=(2*10.5)+(age-2)*4
    print('Age in human years: ',age)
    return Age


def main():
    age = int(input("Please enter the dog's age: "))
    while age>=0:
        Age=dogyears(age)
        print('Age in Dog years: ', Age)
        age = int(input("Please enter the dog's age: "))
    print('Invalid age')

main()
