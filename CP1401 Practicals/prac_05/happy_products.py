print('Menu: ')
print('(I)nstructions')
print('(C)alculate')
print('(Q)uit')
choice=input('Choice: ')
choice=choice.upper()
while(True):
    if(choice!='I' and choice!='C' and choice!='Q'):
        print('Invalid choice')
        print('Menu: ')
        print('(I)nstructions')
        print('(C)alculate')
        print('(Q)uit')
        choice = input('Choice: ')
        choice = choice.upper()
    if choice=='I':
       print("Enter the number of products you want to buy and your chosen price.")
       print("If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")
       print('Menu: ')
       print('(I)nstructions')
       print('(C)alculate')
       print('(Q)uit')
       choice = input('Choice: ')
       choice = choice.upper()
    if choice=='C':
        num=int(input('Number of products: '))
        while(num<0):
            print('Invalid input')
            num = int(input('Number of products: '))
        price=float(input('Price: '))
        while(price<=0):
            print('Invalid input')
            price = int(input('Price: $'))
        if(num<6):
            total=num*price
        else:
            price2=price-(price*0.05)
            total=num*price2
        print(f'{num} x ${price} products = {total}')
        print('Menu: ')
        print('(I)nstructions')
        print('(C)alculate')
        print('(Q)uit')
        choice = input('Choice: ')
        choice = choice.upper()
    if choice=='Q':
        print('Farewell')
        break



