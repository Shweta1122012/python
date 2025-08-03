class computer:
    def __init__(self):
        self.__maxprice =500
    def sell(self):
        print("selling price is",self.__maxprice)
    def maxsellprice(self,price):
        self.__maxprice = price
        
c=computer()
c.sell()
c.__maxprice=1000
c.sell()
c.maxsellprice(300)
c.sell()
       
        
