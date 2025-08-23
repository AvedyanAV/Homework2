from abc import ABC, abstractmethod


class InitLoggerMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__

        params = []

        for arg in args:
            params.append(repr(arg))

        for key, value in kwargs.items():
            params.append(f"{key}={repr(value)}")

        params_str = ', '.join(params)

        print(f"{class_name}({params_str})")

        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    """Базовый абстрактный класс"""
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def price(self):
        pass


class Product(InitLoggerMixin, BaseProduct):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict):
        """Создает новый продукт из словаря данных"""
        return cls(
            name=product_data.get('name'),
            description=product_data.get('description'),
            price=product_data.get('price'),
            quantity=product_data.get('quantity')
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение продуктов: возвращает общую стоимость только для объектов одного класса"""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")

        if type(self) is not type(other):
            raise TypeError("Нельзя складывать объекты разных классов продуктов")

        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
