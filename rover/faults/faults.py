"""Fault detection for the rover."""

from typing import List


class FaultDetector:
    """Track reported faults in the rover."""

    def __init__(self) -> None:
        self.faults: List[str] = []

    def report_fault(self, fault: str) -> None:
        """Record a fault condition."""
        self.faults.append(fault)

    def has_faults(self) -> bool:
        """Return True if any faults have been reported."""
        return bool(self.faults)
