import random
def jcus_grade(score):
    if score<50:
        result='N'
    elif score>50 and score<=65:
        result='P'
    elif score>65 and score<=75:
        result='C'
    elif score>75 and score<=85:
        result='D'
    else:
        result='HD'
    return result

def main():
    score=float(input('Score: '))
    if score<0:
        print('Inavlid Score')
    else:
        while(score>=0):
            result=jcus_grade(score)
            print(f'The Score {score} is {result}')
            score=float(input('Score: '))
    number_of_grades=int(input('How many random scores: '))
    for number in range(1,number_of_grades+1):
        scor=random.randint(1,100)
        outcome=jcus_grade(scor)
        print(f'{scor} = {outcome}')

main()

