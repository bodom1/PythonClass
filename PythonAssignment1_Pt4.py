#4.Celcius to Fahrenheit converter
Temp = 0
while True:
    ConversionType = input('What unit is your temputature in? [C/F]?\n')
    if ConversionType == 'C':
        Temp = int(input('What is the tempurature in degrees ' +ConversionType +'?\n'))
        NewTemp = 9/5*Temp + 32
        OppositeUnit = 'Fahrenheit'
        break
    elif ConversionType == 'F':
        Temp = int(input('What is the tempurature in degrees ' +ConversionType +'?\n'))   
        NewTemp = 5/9*(Temp - 32)
        OppositeUnit = 'Celcius'
        break
    else :
        print('That is not a Valid Unit')
print('The Temperature in ' + OppositeUnit  + ' is ' + str(format(NewTemp,'.1f')) + ' degrees ' + OppositeUnit)
