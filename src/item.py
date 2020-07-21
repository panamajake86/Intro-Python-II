class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return self.name + ":\t" + self.description

    def on_take(self):
        print("You have picked up " + self.name)
    
    def on_drop(self):
        print("You have dropped " + self.name)