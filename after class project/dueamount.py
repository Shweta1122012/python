bill = int(input("enter the bill amount"))
payed = int(input("enter the amount you have paid"))
def dueamount(bill, payed):
    return bill - payed
print("You still have to pay ", due(bill, payed))
