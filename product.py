class Product:
    counter = 0

    def __init__(self, name, price, category):
        self.code = Product.counter
        self.name = name
        self.price = price
        self.category = category
        Product.counter += 1

    def __repr__(self):
        return str(self.__dict__)

    def update_price(self, percent_change, is_increased):
        percent_change = percent_change / 100
        if is_increased:
            self.price = round(self.price + (self.price * percent_change))
        else:
            self.price = round(self.price - (self.price * percent_change))

    def print_info(self):
        print("Code:\t"+str(self.code)+"\nNombre:\t"+self.name+"\nCateg:\t"+self.category+"\nPrecio:\t"+str(self.price))
        print()
