#!/usr/bin/env python3

#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count
    
    @property
    def get_page_count(self):
        return self._page_count
    
    @get_page_count.setter
    def page_count(self, page_count):
        if type(page_count) == int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


    # turn_page(7)
    
    # _page_count = property(get_page_count, set_page_count)

