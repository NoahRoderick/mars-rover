"""Shared data schemas."""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class TelemetryPacket:
    """Telemetry information sent from the rover."""

    timestamp: str
    temperature: float
    battery_level: float


@dataclass
class Command:
    """Command sent to the rover or deck."""

    command_type: str
    payload: Dict[str, Any]
