import os
import pickle
import tempfile


class Soda:
    def __init__(self, supple):
        self.supple = supple

    def show_my_drink(self):
        if self.supple:
            print("🥤 Газировка {}".format(self.supple))
        else:
            print("🥤 Обычная газировка")


class TriangleChecker:
    def __init__(self, a, b, c):
        if a > 0 and b > 0 and c > 0:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("С отрицательными числами ничего не выйдет!")

    def is_triangle(self):
        if (
            isinstance(self.a, (int, float))
            and isinstance(self.b, (int, float))
            and isinstance(self.c, (int, float))
        ):
            if (
                self.a + self.b > self.c
                and self.a + self.c > self.b
                and self.b + self.c > self.a
            ):
                return "🔺 Ура, можно построить треугольник!"
            else:
                return "🔺 Жаль, но из этого треугольник не сделать."
        else:
            return "🔺 Нужно вводить только числа!"


class KgToPounds:
    def __init__(self, kg):
        if kg >= 0:
            self._kg = kg
        else:
            raise ValueError("Килограммы не могут быть отрицательными")

    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, new_kg):
        if new_kg >= 0:
            self._kg = new_kg
        else:
            raise ValueError("Килограммы не могут быть отрицательными")

    def to_pounds(self):
        return self._kg * 2.205


class Nikola:
    def __init__(self, name, age):
        if name == "Николай":
            self.name = name
        else:
            self.name = "Я не {}, а Николай,".format(name)
        self.age = age


class RealString:
    def __init__(self, value):
        self.value = str(value)

    def __len__(self):
        return len(self.value)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)


def run_soda():
    additive = input("Введите добавку к газировке: ")
    soda = Soda(additive)
    soda.show_my_drink()


def run_triangle_checker():
    a = float(input("Введите длину первой стороны треугольника: "))
    b = float(input("Введите длину второй стороны треугольника: "))
    c = float(input("Введите длину третьей стороны треугольника: "))
    triangle = TriangleChecker(a, b, c)
    print(triangle.is_triangle())


def run_kg_to_pounds():
    kg_weight = float(input("Введите вес в килограммах: "))
    kg_to_pounds = KgToPounds(kg_weight)
    print("{} кг = {} фунтов".format(kg_to_pounds.kg, kg_to_pounds.to_pounds()))


def run_nikola():
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    nikola = Nikola(name, age)
    print(nikola.name + " мне " + str(nikola.age) + " лет")


def run_real_string():
    string_value = input("Введите строку: ")
    string_object = RealString(string_value)

    other_string = input("Введите другую строку для сравнения: ")
    if string_object > other_string:
        print("Первая строка длиннее второй.")
    elif string_object < other_string:
        print("Первая строка короче второй.")
    else:
        print("Строки равной длины.")


def choose_task():
    print("Выберите задание:")
    print("1. Газировка")
    print("2. Проверка треугольника")
    print("3. Конвертация веса")
    print("4. Николай")
    print("5. Сравнение длин строк")

    task_number = input("Введите номер задания: ")

    if task_number == "1":
        run_soda()
    elif task_number == "2":
        run_triangle_checker()
    elif task_number == "3":
        run_kg_to_pounds()
    elif task_number == "4":
        run_nikola()
    elif task_number == "5":
        run_real_string()
    else:
        print("Неверный номер задания.")


# Основной код
choose_task()
