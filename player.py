from audioop import add #what's audioop?


class Player:
    #constructor -  default values
    def __init__(self, name, health, mana, style):
        self.name = name
        self.health = 20
        self.mana = 15
        self.style = style

    #updates health when player receives damage or restores health
    def add_heal(self, added_pts):
        if added_pts < 0:
            self.health = self.health - added_pts
        else:
            self.health = self.health + added_pts
    
    #updates mana when player spend mana or restores mana
    def add_mana(self, added_pts):
        if added_pts < 0:
            self.mana = self.mana - added_pts
        else:
            self.mana = self.mana + added_pts

