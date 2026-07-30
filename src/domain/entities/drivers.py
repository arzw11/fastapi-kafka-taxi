from dataclasses import (
    dataclass,
    field,
)

from src.domain.entities.base import BaseEntity
from src.domain.entities.orders import Order
from src.domain.values.common import (
    Name,
    Phone,
)


@dataclass
class Driver(BaseEntity):
    name: Name
    phone: Phone
    is_online: bool = field(
        default=False,
        kw_only=True,
    )
    active_order: Order | None = field(
        default=None,
        kw_only=True,
    )
    meta: dict = field(
        default_factory=dict,
        kw_only=True,
    )

    @classmethod
    def create_driver(
        cls,
        name: Name,
        phone: Phone,
    ) -> 'Driver':
        return cls(
            name=name,
            phone=phone,
        )

    def online(self) -> None:
        self.is_online = True

    def offline(self) -> None:
        self.is_online = False

    def assign_order(self, order: Order) -> None:
        self.active_order = order

    def complete_order(self) -> None:
        self.active_order = None
