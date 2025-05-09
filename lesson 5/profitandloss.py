actual_cost=float(input("please enter your actual cost:"))
selling_cost=float(input("please enter your selling cost:"))
cost=selling_cost-actual_cost
if selling_cost>actual_cost:
    print("its a profit",cost)
else:
    print("its a loss")