from abc import ABC, abstractmethod
from enum import Enum
from inspect import getmembers, isclass, isabstract
from sys import modules


class Dish(ABC):
    """Блюда которые есть"""
    DISH = True
    @abstractmethod
    def consume(self):
        pass

class Paste(Dish):
    """Реализация пасты"""
    def consume(self):
        print('Паста готова.')

class Onigiri(Dish):
    """Реализация онигири"""
    def consume(self):
        print('Онигири готовы.')

class Steak(Dish):
    """Реализация стека"""
    def consume(self):
        print('Стейк готов.')


class DishFactory(ABC):
    """Абстрактный для реализации метода prepare()"""
    @abstractmethod
    def prepare(self, amount: int):
        pass

class PasteFactory(DishFactory):
    def prepare(self, amount: int):
        """Метод подготавливает данные и создаёт объект."""
        print('Паста будет готовится примерно 10 минут.')
        print(f'К нему вы получите {amount} мл вина.')
        return Paste()

class OnigiriFactory(DishFactory):
    def prepare(self, amount: int):
        """Метод подготавливает данные и создаёт объект."""
        print('Паста будет готовится примерно 30 минут.')
        print(f'К нему вы получите {amount} мл саке.')
        return Onigiri()

class SteakFactory(DishFactory):
    def prepare(self, amount: int):
        """Метод подготавливает данные и создаёт объект."""
        print('Стейк будет готовится примерно 30 минут.')
        print(f'К нему вы получите {amount} мл красного вина.')
        return Steak()


class RestaurantAlgorithm:
    """Модель алгоритмов ресторана. 
    Осуществляет сбор данных для последующего создания объекта."""
    # динамически формируемое перечисление напитков с номерами
    # существующие напитки берёт из соответствующих классов
    AvailableDish = \
        Enum('AvailableDish', 
             [pair[0] 
              for pair in getmembers(modules[__name__], 
                                     lambda obj: isclass(obj)
                                                 and getattr(obj, 'DISH', False)
                                                 and not isabstract(obj))])
    # словарь хранит экземпляры фабрик по ключам из перечисления RestaurantAlgorithm
    factories = {}
    __initialized = False
    
    def __init__(self):
        if not self.__class__.__initialized:
            self.__class__.__initialized = True
            for dish in self.AvailableDish:
                self.__class__.factories[dish] = eval(f"{dish.name}Factory")()
    
    def show_dish(self) -> None:
        """Показать все доступные блюда."""
        print('Блюда:')
        for dish in self.AvailableDish:
            print(f'\t{dish.value}. {dish.name}')
    
    def choose_type(self) -> int:
        """Запрос пользователю: вид блюда."""
        lf = len(self.AvailableDish)
        return int(input(f'Выберите блюдо (1-{lf}): '))
    
    def choose_amount(self) -> int:
        """Запрос пользователю: объём напитка."""
        return int(input('Укажите количество напитка (мл): '))
    
    def make_drink(self) -> Dish:
        """Собирает все данные и вызывает метод для генерации объекта напитка от нужного экземпляра фабрики."""
        self.show_dish()
        id = self.choose_type()
        amount = self.choose_amount()
        return self.factories[self.AvailableDish(id)].prepare(amount)


hdm = RestaurantAlgorithm()
hdm.make_drink().consume()
