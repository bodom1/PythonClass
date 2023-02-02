# Chapter 3 Practice2

Rectangle1Width = float(input('What is the width of the first rectangle'))
Rectangle1Length = float(input('What is the length of the first rectangle'))
Rectangle2Width = float(input('What is the width of the second rectangle'))
Rectangle2Length = float(input('What is the length of the second rectangle'))

Area1 = Rectangle1Width*Rectangle1Length
Area2 = Rectangle2Width*Rectangle2Length

if Area1 > Area2:
    print('The First Rectangle has the greater area')
elif Area1 < Area2:
    print('The Second Rectangle has the greater area')
else:
    print('The areas are equal')
                        
