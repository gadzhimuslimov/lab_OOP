class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def autor(self):
        return self._author

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super.__init__()
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

    def __repr__(self):
        super.__repr__()


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__()
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def pages(self, new_duration) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность аудиокниги должно быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность аудиокниги должно быть положительным числом")
        self._duration = new_duration

    def __repr__(self):
        super.__repr__()
