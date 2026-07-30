from faker import Faker

from src.domain.entities.customers import Customer
from src.domain.values.common import (
    Name,
    Phone,
)


def test_create_customer(faker: Faker):
    name = Name(faker.name())
    phone = Phone('+79991234567')

    customer = Customer.create_customer(
        name=name,
        phone=phone,
    )

    assert isinstance(customer, Customer)
    assert customer.name == name
    assert customer.phone == phone


def test_create_customer_values(faker: Faker):
    name = Name(faker.name())
    phone = Phone('+79001234567')
    customer = Customer.create_customer(
        name=name,
        phone=phone,
    )

    assert customer.name.as_generic_type() == name.as_generic_type()
    assert customer.phone.as_generic_type() == phone.as_generic_type()
