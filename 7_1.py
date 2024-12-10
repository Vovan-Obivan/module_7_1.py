from pprint import pprint


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'Название:{self.name}, Вес:{self.weight}, Категория:{self.category}')


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return 'Ошибка «Файл не найден».'

    def add(self, *products):
        existing_products = self.get_products().split('\n')
        existing_product_names = {line.split(', ')[0] for line in existing_products if line}
        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name in existing_product_names:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(str(product) + '\n')
                    existing_product_names.add(product.name)


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegitables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
s1.add(p1, p2, p3)

print(p2)  # __str__

s1.get_products()

s1.add(p1, p2, p3)

print(s1.get_products())

