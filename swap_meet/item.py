import uuid

CONDITION_DESCRIPTORS = ["Dump it", "Passable", "Nice", "Good", "Great", "Excellent"]

class Item:
    def __init__(self, id=0, condition=0):
        if not id:
            self.id = uuid.uuid4().int
        else:
            self.id = id

        self.condition = condition

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def get_category(self):
        return type(self).__name__
    
    def condition_description(self):
        return CONDITION_DESCRIPTORS[self.condition]
