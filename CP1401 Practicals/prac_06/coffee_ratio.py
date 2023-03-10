"""
Algorithm:

get dose,yield
ratio=yield/dose
if ratio<2
display ('ristretto')
else if ratio>=2 to ratio<3
display('normale')
else
display('lungo')

"""

def calculate_brew_ratio(dose,yeld ):
    ratio= yeld/dose
    return ratio

def determine_coffee_style(ratio):
    if ratio<2:
        print(f'1:{ratio} is considered ristretto')
    elif ratio>=2 and ratio<3:
        print(f'1:{ratio} is considered normale')
    else:
        print(f'1:{ratio} is considered lungo')

def main():
    dose=float(input('Dose: '))
    yeld=float(input('Yield: '))
    ratio=calculate_brew_ratio(dose,yeld)
    determine_coffee_style(ratio)

main()



