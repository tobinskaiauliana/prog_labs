#Strategy
class TeaStrategy:
    def brew(self):
        pass

class GreenTea(TeaStrategy):
    def brew(self):
        return "Зелёный чай: 10 минут"

class BlackTea(TeaStrategy):
    def brew(self):
        return "Чёрный чай: 3 минуты"

class Teapot:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_tea(self):
        print(self.strategy.brew())

teapot = Teapot(GreenTea())
teapot.make_tea()

teapot.strategy = BlackTea()
teapot.make_tea()

#Chain of Responsibility
class Handler:
    def __init__(self, kind, name, next_=None):
        self.kind = kind
        self.name = name
        self.next = next_

    def handle(self, request):
        if request == self.kind:
            return self.name
        if self.next is not None:
            return self.next.handle(request)
        return "Не найдено"

cardiologist = Handler("heart", "Кардиолог")
therapist = Handler("general", "Терапевт", cardiologist)
reception = Handler("registr", "Регистратура", therapist)

print(reception.handle("registr"))
print(reception.handle("general"))
print(reception.handle("heart"))

#Iterator
class BookIterator:
    def __init__(self, books):
        self.books = tuple(books)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.books):
            raise StopIteration
        book = self.books[self.index]
        self.index += 1
        return book

class Shelf:
    def __init__(self, books):
        self.books = tuple(books)

    def __iter__(self):
        return BookIterator(self.books)


shelf = Shelf(["Мастер и Маргарита", "Мёртвые души", "Отцы и дети"])

for book in shelf:
    print(book)

print(list(shelf))
print(list(shelf))