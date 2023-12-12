import doctest


# TODO Написать 3 класса с документацией и аннотацией типов

class Table:
    def __init__(self, height: (int, float), surface_area: float):
        """
        Создание и подготовка к работе объекта "Стол"

        :param height: Высота стола
        :param surface_area: Площадь поверхности стола
        :raised TypeError: Когда аргументы - нечисловые типы данных
        :raised ValueError: Когда значение площади/высоты меньше или равно нулю

        Пример:
        >>> table = Table(800, 1.5) # инициализация экземпляра класса
        """

        if not isinstance(height, (int, float)):
            raise TypeError("Аргумент должен быть числовым типом данных")
        if height <= 0:
            raise ValueError("Некорректное значение высоты")
        self.height = height

        if not isinstance(surface_area, (int, float)):
            raise TypeError("Аргумент должен быть числовым типом данных")
        if surface_area <= 0:
            raise ValueError("Некорректное значение площади")
        self.surface_area = surface_area

    def increase_height(self, add: int) -> None:
        """
        Метод увеличивает высоту стола

        :param add: Значение добавляемой высоты
        :raised TypeError: Только целочисленный тип
        :raised ValueError: Данный параметр увеличивает высоту, поэтому не может быть отрицательным

        Пример:
        >>> table = Table(800, 1.5)
        >>> table.increase_height(300)
        """
        if not isinstance(add, (int, float)):
            raise TypeError("Недопустимый тип данных")

        if add < 0:
            raise ValueError("Недопустимое значение")
        ...

    def change_slope(self) -> None:
        """
        Метод изменяет угол наклона поверхности

        :raised TypeError: Если аргумент нечисловой тип данных

        Пример:
        >>> table = Table(800, 1.5)
        >>> table.change_slope()
        """
        ...


class Rectangle:
    def __init__(self, length: (int, float), width: (int, float)):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param length: Длина
        :param width: Ширина
        :raised TypeError: Когда аргументы - нечисловые типы данных
        :raised ValueError: Когда значение меньше или равно нулю

        Пример:
        >>> rect = Rectangle(3, 1.5) # инициализация экземпляра класса "Прямоугольник"
        """

        if not isinstance(length, (int, float)):
            raise TypeError("Аргумент должен быть числовым типом данных")
        if length <= 0:
            raise ValueError("Некорректное значение длины")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Аргумент должен быть числовым типом данных")
        if width <= 0:
            raise ValueError("Некорректное значение ширины")
        self.width = width

    def square(self) -> None:
        """
        Метод для вычисления площади.

        :return: Возвращает площадь

        Пример:
        >>> rect = Rectangle(4, 2)
        >>> rect.square()
        """

    def perimeter(self) -> None:
        """
        Метод для вычисления периметра

        :return: Возвращает периметр

        Пример:
        >>> rect = Rectangle(4, 2)
        >>> rect.perimeter()
        """


class Circle:
    def __init__(self, radius: (int, float)):
        """
        Инициализация объекта "Круг"

        :param radius: Радиус
        :raised TypeError: Когда радиус - нечисловой типы данных
        :raised ValueError: Когда значение радиуса меньше или равно нулю

        Пример:
        >>> circle = Circle(5)
        """

        if not isinstance(radius, (int, float)):
            raise TypeError("Аргумент должен быть числовым типом данных")
        if radius <= 0:
            raise ValueError("Некорректное значение радиуса")
        self.radius = radius

    def square(self):
        """
        Метод для вычисления
        площади круга
        Для реализации понадобиться импортировать модуль math(в частности math.pi)

        :return: Возвращает площадь круга

        Пример:
        >>> circle = Circle(5)
        >>> circle.square()
        """

    def length(self):
        """Метод для вычисления
        длины окружности.
        Для реализации понадобиться импортировать модуль math(в частности math.pi)

        :return: Возвращает длину окружности

        Пример:
        >>> circle = Circle(5)
        >>> circle.length()
        """


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
