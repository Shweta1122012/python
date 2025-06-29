def hotelcost (days):
    return 140 *days
def planecost (city):
    if city == "lucknow":
        return 400
    elif city == "mumbai":
        return 500
    elif city == "amritsar":
        return 600
    elif city == "delhi":
        return 700
def rentalcarcost (days):
    if days >= 7:
        return 40*days -50
    elif days >= 3:
        return 40*days -20
    else:
        return 40*days
def tripcost (city,days,spendingmoney):
    return rentalcarcost(days)+hotelcost(days)+planecost(city)+spendingmoney
print ("carrentalcost=",rentalcarcost(6))
print ("cost of plane=",planecost("amritsar"))
print ("cost of hotel=",hotelcost(7))
print ("total cost of the trip=",tripcost("amritsar",7,1400))