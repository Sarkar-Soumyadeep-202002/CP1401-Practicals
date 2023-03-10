def worker_level():
    worker_level=int(input('Enter the worker level: '))
    c=0
    for check in range(1,11):
        if worker_level==check:
            c+=1
            break
    if c==0:
        print('Invalid Worker level')
    else:
        salary=worker_level*5000
        print(f'With worker level {worker_level},your salary is {salary}$')

def nested_loop():
    for number in range(3):
        for numbers in range(7):
            print(numbers,'',end="")
        print()

def main():
    choice=input('Please enter your choice(Worker level,Rows and columns): ')
    choice=choice.lower()
    if choice=='worker level':
        worker_level()
    elif choice=='rows and columns':
        nested_loop()
    else:
        print('Invalid input')
main()
