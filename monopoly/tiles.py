class Tile:
    def __init__(self,type:str, money: int):
        self.type=type
        self.money=money
        self.availble=None
        self.payment=None

class PropertyTile(Tile):
    def __init__(self,type,money, name ,city,price,rent):
        super().__init__(type,money)
        self.name=name
        self.city=city
        self.price=price
        self.rent=rent
        self.owner=None

class RailTile(Tile):
    pass
class BonusTile(Tile):
    def update_money(self):
        self.money+=200
class TaxTile(Tile):
    def update_money(self):
        self.money-=200