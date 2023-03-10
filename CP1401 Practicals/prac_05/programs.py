# # 1.Percentage program
original=float(input('Enter the original price: '))
change=float(input('Enter the percentage of change: '))
result=original+(original*change)
print(f'Original= {original}, Change= {change}, Result= {result}')

# 2. Time of Day
time=float(input('Enter the time of the day: '))
status=input('Are you coming or going? ')
if time<12:
    message='It is before noon'
if time>12:
    message='It isn after noon'
if status=='coming':
    message+=' and you are coming.Hi!'
if status=='going':
    message+=' and you are going.Bye!'
print(message)


# 3.Coffee orders
colour=input('Please enter the type of coffee(Black or White): ')
colour=colour.lower()
colour2=colour
if colour!='white' and colour!='black':
     colour='white'
size=input('Please enter your portion size(small,medium,large): ')
size=size.lower()
if size=='small':
    price=3
elif size=='medium':
    price=4
else:
    price=5
if colour=='white':
    price+=1
print(f'Your {colour2} {size} coffee costs $ {price}')


# 4. Coffee order error-checking
colour=input('Please enter the type of coffee(Black or White): ')
colour=colour.lower()
while(colour!='black' and colour!='white'):
    print('Invalid choice')
    colour=input('Please enter the type of the coffee(Black or white): ')
    colour=colour.lower()
size=input('Please enter your portion size(small,medium,large): ')
size=size.lower()
while(size!='small' and size!='medium' and size!='large'):
    print('Invalid choice')
    size = input('Please enter your portion size(small,medium,large): ')
    size=size.lower()
if size=='small':
    price=3
elif size=='medium':
    price=4
else:
    price=5
if colour=='white':
    price+=1
print('Your price is $',price)

# 5. Low-High printing
low=int(input('Enter a low value: '))
high=int(input('Enter a higher value: '))
sum=0
for item in range(low,(high+1)):
    if high<=low:
        print('Invalid input')
        break
    print(item,end="")
    sum+=item
print(sum)

