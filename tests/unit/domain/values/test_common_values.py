import pytest
from faker import Faker

from src.domain.exceptions.common import (
    EmptyTextExcepetion,
    InvalidPhoneException,
    NameTooLongException,
)
from src.domain.values.common import (
    Name,
    Phone,
)


def test_create_name_vo(faker: Faker):
    name = Name(faker.name())

    assert isinstance(name, Name), f'{name=}'
    assert isinstance(name.as_generic_type(), str), f'{name=}'


def test_create_name_vo_too_long(faker: Faker):
    with pytest.raises(NameTooLongException):
        Name(faker.text(max_nb_chars=1000))


def test_create_name_vo_empty_text():
    with pytest.raises(EmptyTextExcepetion):
        Name('')


def test_create_phone_invalid_country_code():
    with pytest.raises(InvalidPhoneException):
        Phone('+89991234567')


def test_create_phone_invalid_length():
    with pytest.raises(InvalidPhoneException):
        Phone('+7999123456')


def test_create_phone_empty():
    with pytest.raises(InvalidPhoneException):
        Phone('')
