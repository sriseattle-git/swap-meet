from swap_meet.item import Item

UNKNOWN_TYPE = "Unknown"

class Electronics(Item):
    def __init__(self, id=0, type=UNKNOWN_TYPE, condition=0):
        super().__init__(id, condition)
        self.type = type

    def __str__(self):
        return super().__str__() + f" This is a {self.type} device."

