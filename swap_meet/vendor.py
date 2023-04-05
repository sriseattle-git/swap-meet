from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = []
        if inventory:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if self.inventory and (item in self.inventory):
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_id(self, id)    :
        if not self.inventory:
            return None
        
        for item in self.inventory:
            if id == item.id:
                return item
        
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
    # Check for null objects and return False
        if not other_vendor or not my_item or not their_item:
            return False
        
        # Check that both items are present - if either item isn't present abort and return False
        if self.get_by_id(my_item.id) and other_vendor.get_by_id(their_item.id):
            # Remove my item and add to other vendor's inventory
            other_vendor.add(my_item)
            self.remove(my_item)

            # Remove vendor item and add to my vendor's inventory
            self.add(their_item)
            other_vendor.remove(their_item)
            return True
        else:
            return False

    def swap_first_item(self, other_vendor):
        if not other_vendor or not self.inventory or not other_vendor.inventory:
            return False
        
        # Remove 1st Item from my inventory and add 1st item from other vendor's inventory
        temp_item = self.remove(self.inventory[0])
        self.add(other_vendor.inventory[0])

        # Remove 1st Item from other vendor's inventory and add 1st item from my inventory        
        other_vendor.remove(other_vendor.inventory[0])
        other_vendor.add(temp_item)

        return True
    

