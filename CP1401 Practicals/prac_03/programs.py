# 1.TAX
"""Pseudocode
if income< 100
       tax=0
   else if income>=100 & income<1000
       tax=0.05*income
   else
       tax=0.10*income
take_home_pay=income-tax"""
TAX_RATE_LOW = 0.05
TAX_RATE_HIGH = 0.1
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_HIGH = 1000
print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))
if income<TAX_THRESHOLD_LOW:
    total_tax=0
elif income>=TAX_THRESHOLD_LOW and income<TAX_THRESHOLD_HIGH:
    total_tax=income*TAX_RATE_LOW
else:
    total_tax=income*TAX_RATE_HIGH
take_home_pay=income-total_tax
print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")

# 2. CAR INSURANCE
age=int(input('Please enter your age: '))
if age<18:
    print('Hire refused')
elif age>=18 and age<25:
    print('Insurance required')
else:
    print('Insurance not required')

# 3. Simple Password Checker
password='Venom'
enter=input('Please enter the password: ')
if enter==password:
    print('Access granted')
else:
    print('Access denied')

# 4. Dog Years
age=int(input("Please enter the dog's age: "))
if age<=2:
    Age=age*10.5
else:
    Age=(2*10.5)+(age-2)*4
print('Age in human years: ',age)
print('Age in Dog years: ',Age)

#5. Rock of Ages
age=int(input('Enter your age: '))
if age<=0 or age>=120:
    print('Invalid Age')
elif age>=0 and age<7:
    print('You join school')
elif age>=7 and age<20:
    print('You work hard to successfully graduate from school')
elif age>=20 and age<=60:
    print('You have to choose what you want to accomplish in your life and start working accordingly')
elif age>60:
    print('You reap the rewards of your hardwork you put in throughout your life')

# 6. Speeding Fines
speed_limit=float(input('Enter your speed limit in km/hr: '))
speed=float(input('Enter your speed in km/hr: '))
if speed<(speed_limit+13):
    print('No fine needed')
elif speed>(speed_limit+13) and speed<(speed_limit+20):
    print('Fine payable is:$ ',266)
elif speed>=(speed_limit+20) and speed<(speed_limit+30):
    print('Fine payable is:$ ',444)
elif speed>=(speed_limit+30) and speed<(speed_limit+40):
    print('Fine payable is:$ ', 622)
elif speed>=(speed_limit+40):
    print(f'Fine payable is:$ {1245} along with a 6-month suspension')


