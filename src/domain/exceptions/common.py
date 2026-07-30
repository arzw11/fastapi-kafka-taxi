from dataclasses import dataclass

from src.domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class EmptyTextExcepetion(ApplicationException):
    @property
    def message(self) -> str:
        return 'Текст не может быть слишком длинным.'


@dataclass(eq=False)
class NameTooLongException(ApplicationException):
    name: str

    @property
    def message(self) -> str:
        return f'Слишком длинное имя "{self.name[:255]}..."'


@dataclass(eq=False)
class InvalidPhoneException(ApplicationException):
    phone: str

    @property
    def message(self) -> str:
        return f'Неверный формат номера телефона "{self.phone}".'
