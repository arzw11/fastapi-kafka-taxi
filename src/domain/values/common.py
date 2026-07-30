import re
from dataclasses import dataclass

from src.domain.exceptions.common import (
    EmptyTextExcepetion,
    InvalidPhoneException,
    NameTooLongException,
)
from src.domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Name(BaseValueObject[str]):
    def validate(self) -> None:
        if not self.value:
            raise EmptyTextExcepetion()

        if len(self.value) > 255:
            raise NameTooLongException(self.value)

    def as_generic_type(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class Phone(BaseValueObject[str]):
    PHONE_PATTERN = re.compile(r"^\+7\d{10}$")

    def validate(self) -> None:
        if not self.PHONE_PATTERN.fullmatch(self.value):
            raise InvalidPhoneException(self.value)

    def as_generic_type(self) -> str:
        return str(self.value)
