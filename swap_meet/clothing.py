from swap_meet.item import Item

UNKNOWN_FABRIC = "Unknown"

class Clothing(Item):
    def __init__(self, id=0, fabric="", condition=0):
        super().__init__(id, condition)
        if fabric:
            self.fabric = fabric
        else:
            self.fabric = UNKNOWN_FABRIC

    def __str__(self):
        return super().__str__() + f" It is made from {self.fabric} fabric."
