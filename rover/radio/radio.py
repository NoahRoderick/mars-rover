<<<<<<< HEAD
"""Placeholder module for Radio."""
=======
"""Radio communications for the rover."""

from typing import List


class RoverRadio:
    """Simulated rover radio interface."""

    def __init__(self) -> None:
        self.inbox: List[str] = []

    def transmit(self, message: str) -> None:
        """Transmit a message (printed to stdout)."""
        print(f"[RoverRadio] {message}")

    def receive(self, message: str) -> None:
        """Store a message in the inbox."""
        self.inbox.append(message)

    def last_message(self) -> str | None:
        """Return the most recent received message, if any."""
        return self.inbox[-1] if self.inbox else None
>>>>>>> codex/create-project-directory-structure-6xgmpq
