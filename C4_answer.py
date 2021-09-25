# please install first> pip install pillow
# insert image file in same directory as image.png
from PIL import Image
class Layer:
    def __init__(self, name):
        self.name = name

    def __call__(self, image):
        width, height = image.size
        print('The width is:', width)
        print('The height is:', height)


image = Image.open('image.png')
layer = Layer("custom layer name")
y = layer(image)
