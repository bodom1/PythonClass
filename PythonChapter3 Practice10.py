# Chapter 3 Practice10
penny = 1
nickel = 5
dime = 10
quarter = 25
currentSum = 0

##while currentSum < 100:
##
##    print('You are currently less than a dollar')
##    
##    Coin = input ('what kind of coin would you like to use?\n')
##    
##    Coin = Coin.upper()
##    if Coin == 'PENNY':
##        currentSum = currentSum + penny
##    elif Coin == 'NICKEL':
##        currentSum = currentSum + nickel
##    elif Coin == 'DIME':
##        currentSum = currentSum + dime
##    elif Coin == 'QUARTER':
##        currentSum = currentSum + quarter
##    else:
##        print('please enter a valid coin name')
##if currentSum == 100:
##    print('congratulations, you have hit a dollar')
##else:
##    print('sorry you have gone bust')

numP = int(input('how many penneis\n'))
numN = int(input('how many nickels\n'))
numD = int(input('how many dime\n'))
numQ = int(input('how many quarter\n'))

currentSum = numP*penny + numN*nickel + numD*dime + numQ*quarter
    
if currentSum == 100:
    print('congratulations, you have hit a dollar')
elif currentSum < 100:
    print("sorry, you're short")
else:
    print('sorry you have gone bust')
    


        




