from dataclasses import (
    dataclass,
    field,
)

from src.domain.entities.base import BaseEntity
from src.domain.enums.orders import OrderStatus


@dataclass
class Location(BaseEntity):
    address: str
    latitude: str | None = field(
        default=None,
        kw_only=True,
    )
    longitude: str | None = field(
        default=None,
        kw_only=True,
    )


@dataclass
class Order(BaseEntity):
    customer_id: str
    executor_id: str | None = field(
        default=None,
        kw_only=True,
    )
    order_status: OrderStatus = field(
        default=OrderStatus.SEARCHING,
        kw_only=True,
    )
    pickup: Location
    destination: Location

    @classmethod
    def create_order(
        cls,
        customer_id: str,
        pickup: Location,
        destination: Location,
    ) -> 'Order':
        return cls(
            customer_id=customer_id,
            pickup=pickup,
            destination=destination,
        )

    def in_progress(self) -> None:
        self.order_status = OrderStatus.IN_PROGRESS

    def cancel_order(self) -> None:
        self.order_status = OrderStatus.CANCELLED

    def complete_order(self) -> None:
        self.order_status = OrderStatus.COMPLETED
