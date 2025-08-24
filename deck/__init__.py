"""Deck subsystem package."""

from .main import main
from .ui import DeckUI
from .alarms import AlarmManager
from .radio import DeckRadio
from .sims import Simulation
from .telemetry import TelemetryCollector

__all__ = [
    "main",
    "DeckUI",
    "AlarmManager",
    "DeckRadio",
    "Simulation",
    "TelemetryCollector",
]
