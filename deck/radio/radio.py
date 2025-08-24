"""Radio communications for the deck subsystem."""

from typing import List, Optional


class DeckRadio:
    """Simulated radio interface for the deck."""

    def __init__(self) -> None:
        self.outbox: List[str] = []

    def send(self, message: str) -> None:
        """Queue a message for transmission."""
        self.outbox.append(message)

    def receive(self) -> Optional[str]:
        """Retrieve the oldest message from the outbox, if any."""
        if self.outbox:
            return self.outbox.pop(0)
        return None
