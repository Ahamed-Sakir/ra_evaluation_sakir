# super class
class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height


# child class
class FlowerImage(Image):
    def __init__(self, width, height, flower_name):
        super().__init__(width, height)
        pass


# For Example, Accessing the information
info = FlowerImage(5, 6, 'Rose')
print(info.width)
