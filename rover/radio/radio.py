"""Radio communications for the rover."""

from __future__ import annotations

from typing import Any, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - imported for type checking only
    from deck.radio import DeckRadio


class RoverRadio:
    """Simulated rover radio interface."""

    def __init__(self) -> None:
        self.inbox: List[Any] = []
        self.peer: Optional[DeckRadio] = None

    def connect(self, deck_radio: DeckRadio) -> None:
        """Connect this radio to the deck's radio."""
        self.peer = deck_radio
        deck_radio.peer = self

    def transmit(self, message: Any) -> None:
        """Transmit ``message`` to the deck and print it."""
        if self.peer is not None:
            self.peer.inbox.append(message)
        print(f"[RoverRadio] {message}")

    def receive(self) -> Optional[Any]:
        """Retrieve the oldest message from the inbox, if any."""
        return self.inbox.pop(0) if self.inbox else None

    def last_message(self) -> Any | None:
        """Return the most recent received message, if any."""
        return self.inbox[-1] if self.inbox else None
