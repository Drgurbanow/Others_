from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validate(self, v):
        pass

    def __set_name__(self, cls, name):
        self.name = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.name in obj.__dict__:
            return obj.__dict__[self.name]
        raise AttributeError("Атрибут не найден")

    def __set__(self, obj, value):
        self.validate(value)
        obj.__dict__[self.name] = value


class Number(Validator):
    def __init__(self, minvalue=float("-inf"), maxvalue=float("+inf")):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, v):
        if not isinstance(v, (int, float)):
            raise TypeError("Устанавливаемое значение должно быть числом")
        if v < self.minvalue:
            raise ValueError(f"Устанавливаемое число должно быть больше или равно {self.minvalue}")
        if v > self.maxvalue:
            raise ValueError(f"Устанавливаемое число должно быть меньше или равно {self.maxvalue}")


class String(Validator):
    def __init__(self, minsize=float("-inf"), maxsize=float("+inf"), predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, v):
        if not isinstance(v, str):
            raise TypeError("Устанавливаемое значение должно быть строкой")
        if len(v) > self.maxsize:
            raise ValueError(f"Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}")
        if len(v) < self.minsize:
            raise ValueError(f"Длина устанавливаемой строки должна быть больше или равна {self.minsize}")
        if self.predicate is not None and not self.predicate(v):
            raise ValueError("Устанавливаемая строка не удовлетворяет дополнительным условиям")


x = 4
for i in range(-1, -x-1, -1):
    print(i)
