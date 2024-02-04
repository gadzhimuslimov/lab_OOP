class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def autor(self) -> str:
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._name!r}, {self._pages!r})'


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность аудиокниги должно быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность аудиокниги должно быть положительным числом")
        self._duration = new_duration

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._name!r}, {self._duration!r})'
