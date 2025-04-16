class Menu:
    def __init__(self):
        self.items=[]
    def add_menu_item(self,item):
        self.items.append(item)
    def find_item(self,item_name):
        for item in self.items:
            return item
        return None
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f"{item_name} removed from menu.")
        else:
            print(f"{item_name} not found in menu.")
    def show_menu(self):
        print("****Menu****")
        print("Item Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t\t{item.price}\t{item.quantity}")
