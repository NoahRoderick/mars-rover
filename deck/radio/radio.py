"""Radio communications for the deck subsystem."""

from __future__ import annotations

from typing import Any, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - imported for type checking only
    from rover.radio import RoverRadio


class DeckRadio:
    """In-memory radio link for the deck.

    Messages sent through :meth:`send` are delivered to the connected
    :class:`~rover.radio.RoverRadio` instance's inbox. Incoming messages from
    the rover are stored in :attr:`inbox` and retrieved via :meth:`receive`.
    """

    def __init__(self) -> None:
        self.inbox: List[Any] = []
        self.peer: Optional[RoverRadio] = None

    def connect(self, rover_radio: RoverRadio) -> None:
        """Connect this radio to the rover's radio."""
        self.peer = rover_radio
        rover_radio.peer = self

    def send(self, message: Any) -> None:
        """Transmit ``message`` to the rover if connected."""
        if self.peer is not None:
            self.peer.inbox.append(message)

    def receive(self) -> Optional[Any]:
        """Retrieve the oldest message from the inbox, if any."""
        return self.inbox.pop(0) if self.inbox else None
