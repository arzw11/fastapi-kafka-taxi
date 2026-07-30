from faker import Faker

from src.domain.entities.drivers import Driver
from src.domain.values.common import (
    Name,
    Phone,
)


def test_create_driver(faker: Faker):
    name = Name(faker.name())
    phone = Phone('+79991234567')
    driver = Driver.create_driver(
        name=name,
        phone=phone,
    )

    assert isinstance(driver, Driver)
    assert driver.name == name
    assert driver.phone == phone
    assert driver.is_online is False
    assert driver.active_order is None
    assert driver.meta == {}


def test_driver_online(faker: Faker):
    driver = Driver.create_driver(
        name=Name(faker.name()),
        phone=Phone('+79991234567'),
    )

    driver.online()

    assert driver.is_online is True


def test_driver_offline(faker: Faker):
    driver = Driver.create_driver(
        name=Name(faker.name()),
        phone=Phone('+79991234567'),
    )

    driver.online()
    driver.offline()

    assert driver.is_online is False
