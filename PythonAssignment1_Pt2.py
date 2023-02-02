#2.Miles-per-Gallon
Distance = 0
Fuel = 0
Distance = float(input('What is the Distance Traveled in this trip?\n'))
Fuel = float(input('How Much fuel was used along the Trip?\n'))
MPG = Distance/Fuel
print('The avereage fuel consumption is ' + str(format(MPG,'.1f')) + ' MPG')
