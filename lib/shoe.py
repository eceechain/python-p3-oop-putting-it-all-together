class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def get_size(self):
        return self._size
    
    @get_size.setter
    def set_size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")
     
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"