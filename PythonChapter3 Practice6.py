# Chapter 3 Practice6

Date = input('What is the date in MM/DD/YY format')

day1 = Date[-5:]
day = day1[:2]

month = Date[:2]

year = Date[-2:]

DateMult = int(month)*int(day)

if DateMult == int(year):
    print('magic Number')
else:
    print('nah bruv, no luck')

