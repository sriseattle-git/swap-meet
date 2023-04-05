import uuid

class Item:
    def __init__(self, id=0):
        if not id:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def get_category(self):
        return type(self).__name__
    

