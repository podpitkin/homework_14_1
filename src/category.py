
class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        sum_quantity = 0
        for product in self.__products:
            sum_quantity += product.quantity
        return f'{self.name}, количество продуктов: {sum_quantity} шт.'


    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return self.__products

    @property
    def products(self):
        product_list = ''
        for product in self.__products:
            product_list = f'{str(product)}'
        return product_list
