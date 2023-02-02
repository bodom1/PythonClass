#3.Tip, Tax, Total
Tip = .18
Taxes = .07
Cost = 0
Cost = float(input('What is the cost of the food?\n'))
TipTotal = Cost*Tip
TaxTotal = Cost*Taxes
FinalPrice = Cost + TipTotal + TaxTotal
print('The subtotal of the Food is $' + format(Cost,'.2f'))
print('The Tip is $' + format(TipTotal,'.2f'))
print('The Taxes are $' + format(TaxTotal,'.2f'))
print('The Final Price is $' + format(FinalPrice,'.2f'))
