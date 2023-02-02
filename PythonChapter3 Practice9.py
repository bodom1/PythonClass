# Chapter 3 Practice9
Num = int(input('What is your number'))

if Num == 0:
    print('green')
elif Num >= 1 and Num <= 10 or Num >= 19 and Num <= 28:
    if Num % 2 ==0:
        print('black')
    else:
        print('red')
elif Num >= 11 and Num <= 18 or Num >= 29 and Num <= 36:
    if Num % 2 ==0:
        print('red')
    else:
        print('black')
else:
    print('Please enter a valid Number')
        




