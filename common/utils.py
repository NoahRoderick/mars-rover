"""Utility functions."""

from datetime import datetime
from typing import Any


def current_time_iso() -> str:
    """Return the current UTC time in ISO-8601 format."""
    return datetime.utcnow().isoformat() + "Z"


def clamp(value: float, minimum: float, maximum: float) -> float:
    """Clamp ``value`` between ``minimum`` and ``maximum``."""
    return max(minimum, min(value, maximum))


def ensure(condition: bool, message: str) -> None:
    """Raise a :class:`ValueError` if ``condition`` is False."""
    if not condition:
        raise ValueError(message)
