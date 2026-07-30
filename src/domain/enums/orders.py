from enum import Enum


class OrderStatus(Enum):
    SEARCHING = 'searching'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
