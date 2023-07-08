class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        output = [x for x in self.products if x[0] == first_letter]
        return output

    def __repr__(self):
        output = f"Items in the {self.name} catalogue:\n"
        self.products.sort()
        for product in self.products:
            output += f"{product}\n"

        return output[:-1]
