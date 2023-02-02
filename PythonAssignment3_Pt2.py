#Assignment3 Pt2
numDawgs = 0
weenieNum = 0
bunNum = 0
weeniePacks = 0
bunPacks = 0
totBun = 0
totWeenie = 0
leftoverWeenie = 0
leftoverBun = 0

numDawgs = int(input('How many Hotdogs do you plan on making?\n'))
weenieNum = 10
bunNum = 8
weeniePacks = int(numDawgs/weenieNum)
bunPacks = int(numDawgs/bunNum)
totWeenie = weeniePacks*weenieNum
totBun = bunPacks*bunNum

if totWeenie < numDawgs:
    weeniePacks = weeniePacks + 1
else:
    print('') #meant to do nothing, but required an else ststement it seemed
if totBun < numDawgs:
    bunPacks = bunPacks + 1
else:
    print('') #meant to do nothing, but required an else ststement it seemed

totWeenie = weeniePacks*weenieNum
totBun = bunPacks*bunNum
leftoverBun = totBun % numDawgs
leftoverWeenie = totWeenie % numDawgs
print('You will need ' + str(weeniePacks) + ' packs of weenies')
print('You will need ' + str(bunPacks) + ' packs of buns')
print('You will have ' + str(leftoverWeenie) + ' weenies leftover')
print('You will have ' + str(leftoverBun) + ' buns leftover')
