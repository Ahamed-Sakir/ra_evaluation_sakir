class LaptopBrand:
    def __init__(self, name):
        self.name = name

# we can do this
#laptopBrand = LaptopBrand("Lenovo")
# but how can i do this > Answer:

laptopBrand = [LaptopBrand('DELL'), LaptopBrand('Hp'), LaptopBrand('Lenovo')]
print(laptopBrand[0].name)
