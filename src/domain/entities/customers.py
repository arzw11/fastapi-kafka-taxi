from dataclasses import dataclass

from src.domain.entities.base import BaseEntity
from src.domain.values.common import (
    Name,
    Phone,
)


@dataclass
class Customer(BaseEntity):
    name: Name
    phone: Phone

    @classmethod
    def create_customer(
        cls,
        name: Name,
        phone: Phone,
    ) -> 'Customer':
        return cls(
            name=name,
            phone=phone,
        )
