class Parallelogram:
    """Описание класса "Параллелограм" """

    def __init__(self, length: (int, float), width: (int, float)):
        """
            Создание и подготовка к работе объекта
            Длина и ширина должны пройти проверки на корректность и поэтому являются защищенными атрибутами.
            :param length: Длина параллелограмма
            :param width: Ширина параллелограмма
            :raised TypeError: Когда аргументы - нечисловые типы данных
            :raised ValueError: Когда значение соответствующих аргументов меньше или равно нулю
        """

        if not isinstance(length, (int, float)):
            raise TypeError("Аргумент должен быть числовым типом данных")
        if length <= 0:
            raise ValueError("Некорректное значение длины")
        if not isinstance(width, (int, float)):
            raise TypeError("Аргумент должен быть числовым типом данных")
        if width <= 0:
            raise ValueError("Некорректное значение ширины")

        self._length = length
        self._width = width

    def __str__(self) -> str:
        """
            Реализует представление объекта в удобном виде для пользователя
       """

        return f'Прямоугольник(длина={self._length}, ширина={self._width})'

    def __repr__(self) -> str:
        """
            Реализует представление объекта в машинно-ориентированного виде
        """

        return f'{self.__class__.__name__}(length={self._length}, width={self._width})'

    @property
    def square(self) -> (int, float):
        """Возвращает площадь объекта"""
        return self._length * self._width


class Parallelepiped(Parallelogram):
    """
    Описание класса "Параллелепипед"
    Класс "Параллелепипед" является дочерним от класса "Параллелограмм"
    """

    def __init__(self, length: (int, float), width: (int, float), height: (int, float)):
        """
        Создание и подготовка к работе объекта
        :param length: Длина параллелипипеда
        :param width: Ширина параллелипипеда
        :param height: Высота параллелипипеда также является защищенным атрибутом, в согласовании с базовым классом
        :raised TypeError: Когда аргументы - нечисловые типы данных
        :raised ValueError: Когда значение соответствующих аргументов меньше или равно нулю
        """
        super().__init__(length, width)
        if not isinstance(height, (int, float)):
            raise TypeError("Аргумент должен быть числовым типом данных")
        if height <= 0:
            raise ValueError("Некорректное значение аргумента")

        self._height = height

    def __str__(self) -> str:
        """
            Реализует представление объекта в удобном виде для пользователя
            Метод перезагружен т.к. добавлен параметр высоты
        """
        return f'Прямоугольник(длина={self._length}, ширина={self._width}, высота={self._height})'

    def __repr__(self) -> str:
        """
            Реализует представление объекта в машинно-ориентированного виде
            Метод перезагружен т.к. добавлен параметр высоты
        """
        return f'{self.__class__.__name__}(length={self._length}, width={self._width}, height={self._height})'

    @property
    def square(self) -> (int, float):
        """
            Возвращает площадь объекта
            Свойство перегружено, т.к. необходимо вычислить площадь полной поверхности
        """

        # 2(ab + bc + ac)
        return 2 * ((self._length * self._width) + (self._width * self._height) + (self._length * self._height))

    @property
    def volume(self) -> (int, float):
        """
            Свойство возвращает объем объекта
            Внимание: В данном свойстве square - площадь основания, вызываемый из базового класса!
        """
        return super().square * self._height


if __name__ == "__main__":
    # Write your solution here
    quadro = Parallelogram(3, 3)
    stereo = Parallelepiped(4, 5, 3)

    print(quadro)
    print(stereo)
    print(repr(quadro))
    print(repr(stereo))
    print(quadro.square)
    print(stereo.square)
    print(stereo.volume)
    print(help(quadro))
    print(help(stereo))
