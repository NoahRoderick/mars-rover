"""Shared data schemas."""

<<<<<<< HEAD
# Placeholder for schema definitions.

=======
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
>>>>>>> codex/create-project-directory-structure-6xgmpq
