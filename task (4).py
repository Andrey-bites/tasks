"""Создайте класс "животное". Наполните его данными и методами на свое усмотрение. Пропишите в методах класса докстринги с описанием метода."""


"""Почитайте про Диаграммы класса. Опишите с помощью классов кухонную технику в виде диаграммы (пример https://www.intuit.ru/EDI/23_04_17_1/1492899714-28128/tutorial/356/objects/2/files/02_05.gif). Продумайте классы, их назначение и взаимосвязи. Реализовать с описанием свойств и методов."""


""" * Описать все то же с помощью питона. """


class Animal:
    
    nickname = 'Spyke'
    age = 'one year'
    breed = 'pit bull'
    color = 'brown'
    food = 'food'
    kind_of_animal = 'some animal'
    
    def __init__(self, init_nickname=None, init_age=None, init_breed=None, init_color=None, init_food=None, init_kind_of_animal=None):
        if self.nickname is not None:
            self.nickname = init_nickname
        if self.age is not None:
            self.age = init_age
        if self.breed is not None:
            self.breed = init_breed
        if self.color is not None:
            self.color = init_color
        if self.food is not None:
            self.food = init_food
        if self.kind_of_animal is not None:
            self.kind_of_animal = init_kind_of_animal

    def feed_the_dog(self):
        return f'{self.nickname} eats {self.food}.'

    def walk_the_dog(self):
        return f'walking with dog {self.nickname}.'

    def play_with_the_dog(self):
        return f'plaing with {self.nickname}'

    def info_about_beast(self):
        return {
            'kind_of_animal': self.kind_of_animal,
            'name': self.nickname,
            'age': self.age,
            'breed': self.breed,
            'color': self.color,
            'food': self.food
            }


puppy = Animal('Spyke', 'half a year', 'pit bull', 'brown', 'chicken', 'dog')

walk = puppy.feed_the_dog()
info = puppy.info_about_beast()

print(info)
