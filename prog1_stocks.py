## Prompt user and get input
user = str(input("Enter name: "))
print("Welcome " + user + "!")
stocks = int(input("How many stocks would you like to purchase? : "))
stockPrice = float(input("At what price are you purchasing each stock at? : "))
## Calculate total base cost
stockCost = stocks * stockPrice
## Put commission in decimal form
commission = float(input("What is the broker's commission? : "))/100
## Calculate purchase commission
buyCommission = commission * stockCost
## Calculate total
stockTotal = stockCost + buyCommission
## Add break for spacing
print()

## Show user purchase order
print("=========] PURCHASE [=========")
print("Name:", user)
print("Stocks:", stocks)
print("Cost: $",format(stockCost, '.2f'))
print("Commission: $",format(buyCommission, '.2f'))
print("Total Paid: $",format(stockTotal, '.2f'))
print()

## Prompt user to sell stocks
stockSale = float(input("What price will you sell at? : "))
## Calculate total sale
totalSale = stockSale * stocks
## Calculate sale commission
saleCommission = totalSale * commission
## Calculate net value
netSale = totalSale - saleCommission
## Break for spacing
print()

## Show user sale order
print("===========] SALE [===========")
print("Name:", user)
print("Stocks:", stocks)
print("Sale Price: $",format(stockSale, '.2f'))
print("Commission: $",format(saleCommission, '.2f'))
print("Net Sale: $",format(netSale, '.2f'))
print()

## Figure out if it was a gain or loss and prompt user
if netSale > stockTotal:
    stockGain = float(netSale - stockTotal)
    print("=====] FINAL VALUATION [=====")
    print("Gain of $", format(stockGain, '.2f'))
elif netSale < stockTotal:
    stockLoss = float(stockTotal - netSale)
    print("=====] FINAL VALUATION [=====")
    print("Loss of $", format(stockLoss, '.2f'))
else:
    print("=====] FINAL VALUATION [=====")
    print("There was no gain or loss.")