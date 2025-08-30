"""Claw control for the rover subsystem."""


class ClawController:
    """Operate a simple open/close claw."""

    def __init__(self) -> None:
        self.open = True

    def open_claw(self) -> None:
        """Open the claw."""
        self.open = True

    def close_claw(self) -> None:
        """Close the claw."""
        self.open = False

    def is_open(self) -> bool:
        """Return whether the claw is open."""
        return self.open
