from monopoly.board import Board


class Player:
    def __init__(self,name, location,money):
        self.name=name
        self.location=location
        self.money=money
        self.assets=[]
    def payment(self,price,name):
        self.money-=price
        self.assets.append(name)
    def get_money(self,amount):
        self.money+=amount
    def movement(self,step):
        # step=Dice
        self.location=Board().movement(step)
    def buy(self, name,price):
        buy=input("Are you want to buy this property? ")
        if buy == "yes":
            self.payment(name,price)

