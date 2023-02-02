# Calculator V1

FirstNumber = input('What is the Number\n')

Operator = input('What command would you like to do?\n')

SecondNumber = input('What is the Number\n')

if Operator == '+' :
    Final = int(FirstNumber) + int(SecondNumber)
    print(Final)
elif Operator == '-' :
    Final = int(FirstNumber) - int(SecondNumber)
    print(Final)
elif Operator == '*' :
    Final = int(FirstNumber) * int(SecondNumber)
    print(Final)
elif Operator == '/' :
    Final = int(FirstNumber) / int(SecondNumber)
    print(Final)
else :
    print('Please enter a valid operator\n')

Final = int(FirstNumber) 


randN = random.choice()
print(randN)
