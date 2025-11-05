from monopoly.data import tiles_data
from monopoly.tiles import BonusTile


class Board:
    board=tiles_data
    def __init__(self,location:int = 0):
        self.location=location
    def movement(self, step):
        self.location+=step
        if self.location>40:
            self.location-=40
        print(self.location)