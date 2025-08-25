<<<<<<< HEAD
"""Placeholder module for Alarms."""
=======
"""Alarm management for the deck subsystem."""

from typing import List


class AlarmManager:
    """Manage active alarms for the deck system."""

    def __init__(self) -> None:
        self.active_alarms: List[str] = []

    def raise_alarm(self, alarm: str) -> None:
        """Add an alarm to the active list."""
        if alarm not in self.active_alarms:
            self.active_alarms.append(alarm)

    def clear_alarm(self, alarm: str) -> None:
        """Remove an alarm from the active list."""
        if alarm in self.active_alarms:
            self.active_alarms.remove(alarm)

    def is_active(self, alarm: str) -> bool:
        """Check if an alarm is currently active."""
        return alarm in self.active_alarms
>>>>>>> codex/create-project-directory-structure-6xgmpq
