# 1. Напишите функцию, которая запрашивает у пользователя номер карты, CVC-код и PIN-код.
# После этого выводит на экран номер карты с первыми четырьмя цифрами,
# остальные заменены на звездочки, CVC-код в виде ###, и PIN-код в виде &&&0 (вместо 0 последняя цифра).

def platezh(number_cart,cvc,pin):
    return print(number_cart[:3] + '*' * len(number_cart[:-4]), '#' * len(cvc), '&' * len(pin[:-1]) + pin[-1])
platezh((input('Введите номер платежной карты: ')),(input('Введите CVC-код: ')),(input('Введите PIN-код: ')))

# 2. Напишите функцию, которая возвращает True, если введенный текст читается одинаково слева-направо и справа-налево.
# Иначе – False. Допишите к функции декоратор, который выведет имя функции, ее аргумент.


def decorator(slovo):
    def wrapper(arg):
        return slovo(arg), f'Имя функции: {str(slovo.__name__)}, Аргумент: {str(arg)}'
    return wrapper
@decorator
def slovo(arg):
    if arg[::1] == arg[::-1]:
        return True
    else: return False
print(slovo('ОСЛО'))
print(slovo('ОлСлО'))

# 3 (не полностью)

class Company:
    levels = {1: "junior", 2: "middle", 3: "senior", 4: "lead"}

    def __init__(self, _index, _levels):
        self._index = _index
        _index = Company.levels
        self._levels = Company.levels.keys()

    def _level_up(self, _index):
        self._index = 1
        _level_up = self._index + 1
        return _level_up

    def is_lead(self):
        while self._index < 4:
            print('Квалификация: ', Company.levels())

class Programmer(Company):
    def __init__(self, name, _level_1):
        self.name = 'Alex'
        self.age = 31
        self._level_1 = Company.levels
    def work(Company):
        Company._index = 1
        _level_up = Company._index + 1
        return Company._level_up


@staticmethod
def knowledge_base():
    print(Company.default_name,Company.levels)

# 4 (НЕ полностью). Создайте класс на тему животных.
# Используйте статические и динамические переменные, дочерний (1 или более) классов на конкретное животное.
# Публичные и приватные методы. Полиморфизм (одинаковые названия методов info в обоих классах,
# которые выводят информацию о животных, либо о конкретном животном данного класса).
# Создайте объекты каждого класса и обратитесь к каждому методу.
# Напишите один staticmethod, один classmethod, к которым также обратитесь.

class Animals:
    default_1 = 'Дышать'
    default_2 = 'Питаться'
    default_col = 1000000000000

    def __init__(self, color, vid, col):
        self.color = color
        self.vid = vid
        self.col = col

    @staticmethod
    def model_hash(self):
        if Animals.col < 5000 :
            return 'Мало'
        else:
            return 'Много'

Zebra = Animals('Полосатая','Лошади', 2500)
Lev = Animals('Желтый','Кошачьи', 39000)

print(Zebra.col)