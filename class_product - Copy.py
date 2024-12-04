class Product:
    def __init__(self, product_id, marked_price, discount):
        self.id = product_id
        self.marked_price = marked_price
        self.disc = discount
        self.discount = discount
    def display(self):
        print(self.id, self.marked_price, self.dis)
    @property
    def discount(self):
        pass
    @discount.setter
    def discount(self, dis):
        if dis == self.disc:
            self.dis = dis
        else:
            self.dis = self.disc + dis
    @property
    def selling_price(self):
        return self.marked_price - self.marked_price*self.dis/100
