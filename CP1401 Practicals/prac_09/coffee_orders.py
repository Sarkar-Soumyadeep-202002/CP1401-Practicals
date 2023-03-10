import random
def orders(coffee_types):
    print('Please choose from: ')
    choice=input('Flat White - Espresso - Long Black - Babyccino - ?')
    choice=choice.title()
    while (choice in coffee_types)==False:
        print('Invalid order')
        choice = input('?')
        choice=choice.title()
    if choice=='Long Black':
        print("Here's how to make a/n Long Black:")
        print('- Insert portafilter into grinder')
        print('- Press grind button to grind beans into portafilter')
        print('- Distribute grounds')
        print('- Tamp grounds')
        print('- Insert full portafilter into group head')
        print('- Press shot button to pour espresso into cup')
        print('- Add hot water to cup')
    elif choice== 'Espresso':
        print("Here's how to make a/n Espresso:")
        print('- Insert portafilter into grinder')
        print('- Press grind button to grind beans into portafilter')
        print('- Distribute grounds')
        print('- Tamp grounds')
        print('- Insert full portafilter into group head')
        print('- Press shot button to pour espresso into cup')
    elif choice== 'Flat White':
        print("Here's how to make a/n Flat White:")
        print('- Insert portafilter into grinder')
        print('- Press grind button to grind beans into portafilter')
        print('- Distribute grounds')
        print('- Tamp grounds')
        print('- Insert full portafilter into group head')
        print('- Press shot button to pour espresso into cup')
        print('- Fill jug with milk')
        print('-Steam milk until nice microfoam formed and milk up to temperature')
        print('- Swirl milk gently in jug')
        print('Pour milk into cup... carefully, artistically :)')
    elif choice=='Babyccino':
        print('Sorry, not available')
    return choice

def drink(list_of_orders):
    if len(list_of_orders)==0:
        print("Oh... where's my coffee?")
    else:
        if list_of_orders[-1]=='Babyccino':
            print('Sorry not available')
        else:
            print(f'Mmmm, nice {list_of_orders[-1]}')


def random_selection(coffee_types):
    choice=random.randint(0,(len(coffee_types)-1))
    coffee=coffee_types[choice]
    if coffee=='Long Black':
        print("Here's how to make a/n Long Black:")
        print('- Insert portafilter into grinder')
        print('- Press grind button to grind beans into portafilter')
        print('- Distribute grounds')
        print('- Tamp grounds')
        print('- Insert full portafilter into group head')
        print('- Press shot button to pour espresso into cup')
        print('- Add hot water to cup')
    elif coffee== 'Espresso':
        print("Here's how to make a/n Espresso:")
        print('- Insert portafilter into grinder')
        print('- Press grind button to grind beans into portafilter')
        print('- Distribute grounds')
        print('- Tamp grounds')
        print('- Insert full portafilter into group head')
        print('- Press shot button to pour espresso into cup')
    elif coffee== 'Flat White':
        print("Here's how to make a/n Flat White:")
        print('- Insert portafilter into grinder')
        print('- Press grind button to grind beans into portafilter')
        print('- Distribute grounds')
        print('- Tamp grounds')
        print('- Insert full portafilter into group head')
        print('- Press shot button to pour espresso into cup')
        print('- Fill jug with milk')
        print('-Steam milk until nice microfoam formed and milk up to temperature')
        print('- Swirl milk gently in jug')
        print('Pour milk into cup... carefully, artistically :)')
    elif coffee=='Babyccino':
        print('Sorry, not available')


def main():
    coffee_types=['Flat White','Espresso','Long Black','Babyccino']
    list_of_orders=[]
    print('Welcome to the IT@JCU Coffee Shop')
    print('(O)rder - (D)rink - (R)andom choice - (Q)uit')
    choice=input('>>>')
    choice=choice.upper()
    while choice!='O' and choice!='D' and choice!='R' and choice!='Q':
        print('Invalid option')
        print('(O)rder - (D)rink - (R)andom choice - (Q)uit')
        choice = input('>>>')
        choice = choice.upper()
    while True:
        if choice!='O' and choice!='D' and choice!='R' and choice!='Q':
            print('Invalid option')
            print('(O)rder - (D)rink - (R)andom choice - (Q)uit')
            choice = input('>>>')
            choice = choice.upper()
        elif choice=='O':
            list_of_orders.append(orders(coffee_types))
            print('(O)rder - (D)rink - (R)andom choice - (Q)uit')
            choice = input('>>>')
            choice = choice.upper()
        elif choice=='D':
            drink(list_of_orders)
            print('(O)rder - (D)rink - (R)andom choice - (Q)uit')
            choice = input('>>>')
            choice = choice.upper()
        elif choice=='R':
            random_selection(coffee_types)
            print('(O)rder - (D)rink - (R)andom choice - (Q)uit')
            choice = input('>>>')
            choice = choice.upper()
        elif choice=='Q':
             print('Thanks for drinking coffee')
             break


main()









