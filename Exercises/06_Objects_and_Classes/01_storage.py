class Storage:

    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity

    def add_product(self, name: str):
        if len(self.storage) < self.capacity:
            self.storage.append(name)

    def get_products(self):
        return self.storage
