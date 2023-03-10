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
    out_file=open('bmis.txt','w')
    number_of_people=int(input('Enter number of people: '))
    count=1
    while(count<=number_of_people):
        height=get_valid_number('Enter the height: ',0,2.5)
        weight=get_valid_number('Enter the weight: ',0,120)
        bmi=calculate_bmi(height,weight)
        print(bmi,file=out_file)
        count+=1
    out_file.close()
