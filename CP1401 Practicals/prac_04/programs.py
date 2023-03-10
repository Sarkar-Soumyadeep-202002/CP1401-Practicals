#1.Error Checking
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

#2.Number Sequences
for odd_number in range(1,100,2):
    print(odd_number)
    print()

for years in range(1896,2021,4):
    print(years,'',end="")

#This sequence is the fibonacci series
a=0;b=1;c=0
limit=int(input('Enter the range: '))
print(a,'',b,'',end='')
for item in range(2,limit+1):
    c=a+b
    print(c,'',end="")
    a=b;b=c
#3.Menus
choice=''
while(choice!='Q'):
    choice = input('Enter your choice(Smiley(S),Frowny(F),Quit(Q)): ')
    choice = choice.upper()
    if choice=='Q':

        print('Thank you')
        break
    elif choice!='S' and choice!='F':
        print('Invalid choice')
        break
    elif choice=='S':
        print(':)')

    elif choice=='F':
        print(':(')

#4. Accumulation
#Average age
total_age=0;count=0
while(total_age<=500):
    age=int(input('Enter the age: '))
    if age<0 or age>130:
        print('Invalid age')
    else:
        count+=1
        total_age+=age
average_age=int(total_age/count)
print('The average age is: ',average_age)

#Smileys count
choice='';count_smiley=0;count_frown=0
while(choice!='Q'):
    choice = input('Enter your choice(Smiley(S),Frowny(F),Quit(Q)): ')
    choice = choice.upper()
    if choice=='Q':
        print('The number of smileys is: ',count_smiley)
        print('The number of frowny faces is: ',count_frown)
        print('Thank you')
        break
    elif choice!='S' and choice!='F':
        print('Invalid choice')
        break
    elif choice=='S':
        print(':)')
        count_smiley+=1
    elif choice=='F':
        print(':(')
        count_frown+=1

#Total Numbers
limit=int(input('Enter the number of iterations: '));sum=0
for number in range(limit):
    num=int(input('Enter a number: '))
    sum+=num
print(sum)
#5.Guessing Game
Secret=2002
choice=int(input('Please enter your guess: '))
while(choice!=Secret):
    print('Please try again')
    choice=int(input('Please enter your guess: '))
print('You got it! ')

# 6.Nested Loops
for number in range(3):
    for numbers in range(7):
        print(numbers,'',end="")
    print()









