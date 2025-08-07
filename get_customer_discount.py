class Customer:
    def __init__(self, name: str, __discount: int = 10):
        self.name = name
        self.__discount = __discount

    # Метод set_discount() принимает на вход
    # новое значение для приватного атрибута "скидка".
    # Если new_value превышает 80 -
    # новое значение скидки должно стать 80.
    # Метод не должен ничего возвращать.
    def set_discount(self, new_value: int):
        self.new_value = new_value
        if self.new_value > 80:
            self.__discount = 80
        else:
            self.__discount = new_value

    # Метод get_price() получает на вход исходную стоимость товара
    # и должен вернуть новую цену товара с учётом
    # скидки покупателя.
    # Возвращаемое значение округлите до двух знаков после запятой.
    def get_price(self, price: int) -> float:
        self.price = price
        discount_value = (100 - self.__discount)/100
        return round(self.price * discount_value, 2)


# Проверим работу программы.
# Создаём объект покупателя:
customer = Customer('Иван Иванович')

original_price = 85

print(
    f'С исходной скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)
# Изменим скидку до неприемлемого уровня.
# Метод set_discount() должен установить размер скидки равным 80.
customer.set_discount(90)
print(
    f'С новой скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)