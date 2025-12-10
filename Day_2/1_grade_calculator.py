print('---GRADE CALCULETOR---')
grade = False
massage = False
num = float(input('Enter your number: '))
if 0 <= num <= 100:
    if num >= 90:
        grade = 'A'
        massage = 'excellent!'
    elif num >= 80:
        grade = 'B'
        massage = 'good!'
    elif num >= 70:
        grade = 'C'
        massage = 'average!'
    elif num >= 60:
        grade = 'D'
        massage = 'pass!'
    else:
        grade = 'F'
        massage = 'sorry!'
else:
    print('Enter number correctly.')
if grade:
    print(f'your grade is {grade}.')
    print(massage)