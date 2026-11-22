#Singleton
class Fridge:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.food = []
        return cls._instance

    def put(self, item):
        self.food.append(item)

    def take(self, item):
        self.food.remove(item)

mom = Fridge()
mom.put("молоко")

son = Fridge()
son.put("колбаса")

print(mom is son)
print(son.food)
print(mom.food)

#Factory method
class Burger:
    filling = ""

    def wrap(self):
        print(f"Упаковка бургера с {self.filling}")

class ChickenBurger(Burger):
    filling = "курицей"

class BeefBurger(Burger):
    filling = "говядиной"

class BurgerMachine:
    def make_burger(self):
        pass

    def serve(self):
        burger = self.make_burger()
        burger.wrap()

class ChickenBurgerMachine(BurgerMachine):
    def make_burger(self):
        return ChickenBurger()

class BeefBurgerMachine(BurgerMachine):
    def make_burger(self):
        return BeefBurger()

ChickenBurgerMachine().serve()
BeefBurgerMachine().serve()

#Abstract factory
class Button:
    def paint(self):
        pass

class DarkButton(Button):
    def paint(self):
        print("Тёмная кнопка")

class LightButton(Button):
    def paint(self):
        print("Светлая кнопка")

class Input:
    def paint(self):
        pass

class DarkInput(Input):
    def paint(self):
        print("Тёмное поле ввода")

class LightInput(Input):
    def paint(self):
        print("Светлое поле ввода")

class ThemeFactory:
    def create_button(self):
        pass

    def create_input(self):
        pass

class DarkFactory(ThemeFactory):
    def create_button(self):
        return DarkButton()

    def create_input(self):
        return DarkInput()

class LightFactory(ThemeFactory):
    def create_button(self):
        return LightButton()

    def create_input(self):
        return LightInput()

def render(factory):
    factory.create_button().paint()
    factory.create_input().paint()

render(DarkFactory())
render(LightFactory())

#Builder
class Coffee:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def __str__(self):
        return "Кофе: " + ", ".join(self.parts)

class CoffeeBuilder:
    def __init__(self):
        self.coffee = Coffee()

    def add_espresso(self):
        self.coffee.add("эспрессо")

    def add_milk(self):
        self.coffee.add("молоко")

    def add_syrup(self):
        self.coffee.add("сироп")

    def add_topping(self):
        self.coffee.add("корица")

    def get_result(self):
        return self.coffee

class Barista:
    def __init__(self, builder):
        self.builder = builder

    def make_coffee(self):
        self.builder.add_espresso()
        self.builder.add_milk()
        self.builder.add_syrup()
        self.builder.add_topping()

builder = CoffeeBuilder()
barista = Barista(builder)

barista.make_coffee()
coffee = builder.get_result()

print(coffee)