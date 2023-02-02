#1.Sales Tax
StateTaxRate = .05
CountyTaxRate = .025
Price = 0
Price = float(input('What is the subtotal of the Purchase?\n'))
CountyTaxes = Price*CountyTaxRate
StateTaxes = Price*StateTaxRate
TotalTaxes = CountyTaxes + StateTaxes
FinalPrice = Price + StateTaxes + CountyTaxes
print('The subtotal of the Purchase is $' + format(Price,'.2f'))
print('The State Taxes are $' + format(StateTaxes,'.2f'))
print('The County Taxes are $' + format(CountyTaxes,'.2f'))
print('The Total Taxes are $' + format(TotalTaxes,'.2f'))
print('The Final Price is $' + format(FinalPrice,'.2f'))
