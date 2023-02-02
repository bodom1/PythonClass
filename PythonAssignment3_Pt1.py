# Assignment 3: Color Mixer
Color_One = '0'
Color_Two = '0'
NewCol = '0'
valid = '0'

while True:
    
    Color_One = input('What is the first color?')
    Color_Two = input('What is the second color?')

    Color_One = Color_One.upper()
    Color_Two = Color_Two.upper()

    if Color_One == 'RED' and Color_Two == 'RED' :
        NewCol = 'Red'
        valid = True
    elif Color_One == 'BLUE' and Color_Two == 'BLUE' :
        NewCol = 'Blue'
        valid = True
    elif Color_One == 'YELLOW' and Color_Two == 'YELLOW' :
        NewCol = 'Yellow'
        valid = True
    elif Color_One == 'RED' and Color_Two == 'BLUE' or Color_One == 'BLUE' and Color_Two == 'RED' :
        NewCol = 'Purple'
        valid = True
    elif Color_One == 'RED' and Color_Two == 'YELLOW' or Color_One == 'YELLOW' and Color_Two == 'RED' :
        NewCol = 'Orange'
        valid = True
    elif Color_One == 'BLUE' and Color_Two == 'YELLOW' or Color_One == 'YELLOW' and Color_Two == 'BLUE' :
        NewCol = 'Green'
        valid = True

    else:
        valid = False

    if valid == True:
        print('The Secondary color is ' + NewCol)
        break
    else :
        print('Error: Please enter a valid value')
    
