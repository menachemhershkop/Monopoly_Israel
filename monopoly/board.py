from monopoly.data import tiles_data
from monopoly.tiles import BonusTile


class Board:
    board=tiles_data
    def __init__(self,location:int, step:int):
        self.location=location
        self.step=step
    def movement(self):
        self.location+=self.step
        if self.location>40:
            self.location-=40
