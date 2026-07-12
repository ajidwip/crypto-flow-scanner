"""
Base domain model.
"""

from __future__ import annotations

from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


def utc_now() -> datetime:
    """
    Return current UTC datetime.
    """
    return datetime.now(timezone.utc)


@dataclass(slots=True)
class BaseModel:
    """
    Base model for all domain objects.
    """

    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    def touch(self) -> None:
        """
        Update modified timestamp.
        """
        self.updated_at = utc_now()

    def to_dict(self) -> dict[str, Any]:
        """
        Convert dataclass to dictionary.
        """
        return asdict(self)