class Tile:
    def __init__(self,type:str, name:str):
        self.type=type
        self.name=name
        self.availble=None
        self.payment=None

class PropertyTile(Tile):
    def __init__(self,type,money, name ,city,price,rent):
        super().__init__(type,money,name)
        self.city=city
        self.price=price
        self.rent=rent
        self.owner=None

class RailTile(PropertyTile):
    pass
class BonusTile(Tile):
    def update_money(self,money):
        money+=200
class TaxTile(Tile):
    def update_money(self,money):
        money-=200