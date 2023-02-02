# Chapter 3 Practice5

Mass = 0
weight = 0
G = 9.8
MaxW = 500
MinW = 100



Mass = float(input('give me a mass\n'))

weight = Mass * G

if weight < MinW:
    print('too light')
elif weight > MaxW:
    print('Too Heavy')
else:
    print('The weight is ' + str(format(weight,'.2f')) + ' Newtons')

