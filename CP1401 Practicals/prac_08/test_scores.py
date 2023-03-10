"""
Pseudocode for main function:
 function main()
    number of scores=4
    scores=[]
    get score
    while()
        if <loop runs more than 4 times>
            quit the loop
        else
            get score
            scores= score
            display score
    for score in scores
        grade= function jcus_grade(score)
        display grade
    average=sum of list elements/length of list
    if average>highest score
        display 'not positive'
    else
        display positive

"""

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
    num_of_scores=4
    scores=[]
    count=1
    while (count<=num_of_scores):
        score = int(input(f'Score{count}: '))
        scores.append(score)
        count+=1
    count=1
    for score in scores:
        grade=jcus_grade(score)
        print(f'Score{count} was {score}, which is {grade}.')
        count+=1
    average_score=sum(scores)/len(scores)
    print('Average score: ', average_score)
    if average_score>scores[3]:
        print('Trend is not positive')
    else:
        print('Trend is positive')


main()
