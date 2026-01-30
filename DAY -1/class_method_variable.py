class car:
    base_price=300000
    def __init__(self,windows,doors,power):
        self.windows=windows
        self.doors=doors
        self.power=power
    def what_base_price(self):
        print("The base price is {}".format(self.base_price))
    @classmethod
    def revise_base_price(cls,inflation):
            cls.base_price=cls.base_price+cls.base_price*inflation
        
car.revise_base_price(0.10)
car.base_price