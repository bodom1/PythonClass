Number = 0

while True:
    Number = input('\nWhich assignment would you like to see? (type N to stop viewing problems)\n')
    if Number == '1':
        #1.Personal Information
        print('\nBlakeley Odom\n')
        print('171 moultrie street, \nCharleton, \nSouth Carolina, \n29365\n')
        print('(864)909-0755\n')
        print('Mechanical Engineering')

#--------------------------------------------------------------------------------
        
    elif Number == '2':
        #2.Sales Prediction
        Profit = 0.0
        PercentProfit = .23
        Sales = 0
        Sales = float(input('\nWhat is the total sales of the company?\n'))
        Profit = Sales*PercentProfit
        print('Your total Profit should be $' + str(format(Profit,'.2f')) + 'for the fiscal year. ')

#---------------------------------------------------------------------------------

    elif Number == '3':
        #3.Land Calculation
        Acrage = 0.0
        ConversionFactor = 43560
        SquareFootage = 0
        SquareFootage = float(input('\nWhat is the area of the land in square feet?\n'))
        Acrage = SquareFootage/ConversionFactor
        print('Your acreage is ' + str(format(Acrage,'.2f')) + ' Acres of land')

#----------------------------------------------------------------------------------

    elif Number == '4':
        #4.Total Purchase
        SalesTax = .07
        Price1 = 0
        Price2 = 0
        Price3 = 0
        Price4 = 0
        Price5 = 0
        Price1 = float(input('\nWhat is the price of the first Item?\n'))
        Price2 = float(input('What is the price of the second Item?\n'))
        Price3 = float(input('What is the price of the third Item?\n'))
        Price4 = float(input('What is the price of the fourth Item?\n'))
        Price5 = float(input('What is the price of the fifth Item?\n'))
        Subtotal  = float(format(Price1 + Price2 + Price3 + Price4 + Price5,'.2f'))
        Total = (1 + SalesTax)*Subtotal
        print('Your subtotal is $' + str(format(Subtotal,'.2f')))
        print('Sales tax is ' + str(format(100*(SalesTax),'.1f')) + '%')
        print('The total tax will be $' + str(format(SalesTax*Subtotal,'.2f')))
        print('Your total is $' + str(format(Total,'.2f')))

#---------------------------------------------------------------------------------

    elif Number == '5':
        #5.Distance Traveled
        Speed = 70.0
        Time1 = 6.0
        Time2 = 10.0
        Time3 = 15.0
        Distance1 = Time1*Speed
        Distance2 = Time2*Speed
        Distance3 = Time3*Speed
        print('\nThe distance traveled in ' + str(int(Time1)) + ' hours, while traveleing at ' + str(int(Speed)) + ' MPH, is ' + str(int(Distance1)) + ' miles.')                 
        print('The distance traveled in ' + str(int(Time2)) + ' hours, while traveleing at ' + str(int(Speed)) + ' MPH, is ' + str(int(Distance2)) + ' miles.')
        print('The distance traveled in ' + str(int(Time3)) + ' hours, while traveleing at ' + str(int(Speed)) + ' MPH, is ' + str(int(Distance3)) + ' miles.')

#---------------------------------------------------------------------------------

    elif Number == '6':
        #6.Sales Tax
        StateTaxRate = .05
        CountyTaxRate = .025
        Price = 0
        Price = float(input('\nWhat is the subtotal of the Purchase?\n'))
        CountyTaxes = Price*CountyTaxRate
        StateTaxes = Price*StateTaxRate
        TotalTaxes = CountyTaxes + StateTaxes
        FinalPrice = Price + StateTaxes + CountyTaxes
        print('The subtotal of the Purchase is $' + format(Price,'.2f'))
        print('The State Taxes are $' + format(StateTaxes,'.2f'))
        print('The County Taxes are $' + format(CountyTaxes,'.2f'))
        print('The Total Taxes are $' + format(TotalTaxes,'.2f'))
        print('The Final Price is $' + format(FinalPrice,'.2f'))

#--------------------------------------------------------------------------------------

    elif Number == '7':
        #7.Miles-per-Gallon
        Distance = 0
        Fuel = 0
        Distance = float(input('\nWhat is the Distance Traveled in this trip?\n'))
        Fuel = float(input('How Much fuel was used along the Trip?\n'))
        MPG = Distance/Fuel
        print('The avereage fuel consumption is ' + str(format(MPG,'.2f')) + ' MPG')

#--------------------------------------------------------------------------------------------

    elif Number == '8':
        #8.Tip, Tax, Total
        Tip = .18
        Taxes = .07
        Cost = 0
        Cost = float(input('\nWhat is the cost of the food?\n'))
        TipTotal = Cost*Tip
        TaxTotal = Cost*Taxes
        FinalPrice = Cost + TipTotal + TaxTotal
        print('The subtotal of the Food is $' + format(Cost,'.2f'))
        print('The Tip is $' + format(TipTotal,'.2f'))
        print('The Taxes are $' + format(TaxTotal,'.2f'))
        print('The Final Price is $' + format(FinalPrice,'.2f'))

#--------------------------------------------------------------------------------------------

    elif Number == '9':
        #9.Celcius to Fahrenheit converter
        Temp = 0
        while True:
            ConversionType = input('\nWhat unit is your temputature in? [C/F]?\n')
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

#--------------------------------------------------------------------------------------------

    elif Number == '10':
        #10.Ingredient Adjuster
        Cookies = 0
        SugarPerCookie = 1.5/48
        ButterPerCookie = 1/48
        FlourPerCookie = 2.75/48
        Cookies = float(input('\nHow many cookies would you like to make?\n'))
        Sugar = SugarPerCookie*Cookies
        Butter = Cookies*ButterPerCookie
        Flour = Cookies*FlourPerCookie
        print('For this recipe you will need\n' + str(format(Sugar,'.2f')) + ' cups of sugar\n' + str(format(Butter,'.2f')) + ' cups of butter\n' + str(format(Flour,'.2f')) + ' cups of flour')

#-------------------------------------------------------------------------------------------

    elif Number == '11':
        #11.Male and Female Percentages
        Male = 0
        Female = 0
        Male = int(input('\nHow many Males are in the class?\n'))
        Female = int(input('How many Females are in the class?\n'))
        TotalPupils = Male + Female
        PercentMen = Male/TotalPupils*100
        PercentWomen = Female/TotalPupils*100
        print('The Percentage of men in the class is ' + str(format(PercentMen,'.2f')) + '%.\nThe Percentage of women in the class is ' + str(format(PercentWomen,'.2f')) + '%.')

#-------------------------------------------------------------------------------------------

    elif Number == '12':
        #12.Stock Transaction Program
        PurchaseNum = 2000.0
        InitialCost = 40.00
        FinalCost = 42.75
        BrokerPay = .03
        PurchaseCost = PurchaseNum*InitialCost
        BrokerInitial = PurchaseCost*BrokerPay
        SellCost = PurchaseNum*FinalCost
        BrokerFinal = SellCost*BrokerPay
        JoeFinal = SellCost - PurchaseCost - BrokerInitial - BrokerFinal
        print('\nJoe bought the stocks for $' + str(format(PurchaseCost,'.2f')))
        print('Joe paid the Broker $' + str(format(BrokerInitial,'.2f')) + ' for the Purchase of the stocks')
        print('Joe sold the Stocks for $' + str(format(SellCost,'.2f')))
        print('Joe paid the Broker $' + str(format(BrokerFinal,'.2f')) + ' when he sold his stocks')
        print('Joe ultimately made $'+ str(format(JoeFinal,'.2f')) + ' after all of these transations')

#---------------------------------------------------------------------------------------------------------------
        
    elif Number == '13':
        #13.Planting Grapevines
        V = 0.0
        R = 0.0
        E = 0.0
        S = 0.0
        R = float(input('\nHow long is the row of GrapeVines?(feet)'))
        E = float(input('How much space is needed by the end-post assembly?(feet)'))
        S = float(input('How much space is between each vine?(feet)'))
        V = int(R - 2*E*S)
        print('This row will fit ' + str(V) + ' Vines')

#------------------------------------------------------------------------------------------------------------

    elif Number =='14':
        #14. Compund Interest
        Principle = 0
        InterestRate = 0
        N = 0
        Time = 0
        Principle = float(input('\nHow much money is the initial deposit?\n'))
        InterestRate = (float(input('What is the intrest rate of your savings account?\n')))/100
        N = float(input('How often is the money compunded in the account?\n'))
        Time = float(input('How many years would you allow the money to accrue?\n'))
        A = Principle*(1+InterestRate/N)**(N*Time)
        print('In ' + str(Time) + ' years, You will have $' + str(format(A,'.2f')) + ' in your savings account')
#--------------------------------------------------------------------------------------------------------------
#This is just here to end the while loop
    elif Number == 'N':
        break
    elif Number == 'n':
        break
    else :
        print('please select a valid problem')

