class Car:
    def __init__(self, model,__vin,__numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers

    def __is_valid_vin(self, vin_number):
        #self.__vin = vin_number
        if isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number is range(1000000, 9999999):
            raise IncorrectVinNumber(f'Неверный диапазон для номера')
        return vin_number

    def __is_valid_numbers(self, numbers):
        #self.__numbers = numbers
        if isinstance(numbers, str):
            raise IncorrectCarNumber('Некорректный тип данных для номера')
        if numbers is len(6):
            raise IncorrectCarNumber('Неверная длина номера')
        return numbers

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')


