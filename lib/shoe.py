class Shoe:
    def __init__(self, brand, size):
        self._brand = None
        self._size = None
        self._condition = 'New'
        self.set_brand(brand)
        self.set_size(size)

    def set_brand(self, value):
        if type(value) == str:
            self._brand = value
        else:
            print("Brand must be a string")

    def get_brand(self):
        return self._brand

    def set_size(self, value):
        if type(value) == int:
            self._size = value
        else:
            print("Size must be an integer")

    def get_size(self):
        return self._size

    def repair_shoe(self):
        print("The shoe has been repaired.")
        self._condition = 'New'

    def get_condition(self):
        return self._condition

# Example usage:
shoe_instance = Shoe("Adidas", 9)
print(shoe_instance.get_brand())          # Output: Adidas
print(shoe_instance.get_size())           # Output: 9
print(shoe_instance.get_condition())      # Output: New

shoe_instance.repair_shoe()
print(shoe_instance.get_condition())      # Output: New
