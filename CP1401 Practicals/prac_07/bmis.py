def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number

def calculate_bmi(height, weight):
    return weight / (height ** 2)


def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


def main():
    choice=input('(C)onstant height of 1.75m or (V)ariable height: ')
    choice=choice.upper()
    if choice == 'C':
        height=1.75
        for weight in range(50,101,2):
            bmi = calculate_bmi(height, weight)
            category = determine_weight_category(bmi)
            print(f'Height {height}, weight {weight},the BMI is', f' {bmi:.1f}', f'which is considered {category}')
    elif choice=='V':
         height=1.5
         while height<=2.0:
            for weight in range(50, 101, 10):
                 bmi = calculate_bmi(height, weight)
                 category = determine_weight_category(bmi)
                 print(f'Height {height}, weight {weight},the BMI is', f' {bmi:.1f}', f'which is considered {category}')
            height+=0.1

    else:
        print('Invalid choice')


main()
