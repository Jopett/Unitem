class Item:
    def __init__(self):
        self.title = None
        self.itemUrl = None
        self.imgUrl = None
        self.price = None
        self.location = None
    def toString(self):
        print(self.title)
        print(self.itemUrl)
        print(self.imgUrl)
        print(self.price)
        print(self.location + "\n")