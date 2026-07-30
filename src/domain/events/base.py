from abc import ABC
from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime
from typing import ClassVar
from uuid import (
    UUID,
    uuid4,
)


@dataclass
class BaseEvent(ABC):
    id: UUID = field( # noqa
        default_factory=uuid4,
        kw_only=True,
    )
    title: ClassVar[str]

    occurred_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )
