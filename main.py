weight= float(input('enter your weight in Kg= '))
height= float(input('enter your height in meter= '))

BMI = weight/height**2

print(f'your BMI is {BMI}')

if BMI < 18.5:
    print(' you are under weight or malnourished ')

elif BMI <= 25:
    print('you are healthy')

elif BMI > 25.5:
    print('you are overweight')


