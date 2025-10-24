class SomeClass():
    def __init__(self, x: int):
        """
            SomeClass has many functionalities etc.

            Args:
                x (int): an integer.
        """

        self.x = x

    def some_method(self, y: int):
        """
           This method does something very important.

           Args:
               y (int): an integer.
        """

        return self.x + y
