from product import Product


class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, name, price, category):
        new_product = Product(name, price, category)
        self.products.append(new_product)
        print(self.name)
        new_product.print_info()
        return self

    def sell_product(self, code):
        for i in range(len(self.products)):
            if self.products[i].code == code:
                self.products[i].print_info()
                self.products.pop(i)
                print(self.products)
                return
        else:
            print("Artículo no disponible en tienda")

    def inflation(self, percent_increase):
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase, True)
            self.products[i].print_info()

    def set_clearance(self, category, percent_discount):
        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i].update_price(percent_discount, False)
                self.products[i].print_info()
