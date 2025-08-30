"""Drive system for the rover."""


class DriveSystem:
    """Simple rover drive control."""

    def __init__(self) -> None:
        self.speed = 0.0

    def set_speed(self, speed: float) -> None:
        """Set the rover's speed."""
        self.speed = speed

    def stop(self) -> None:
        """Stop the rover."""
        self.speed = 0.0

    def get_speed(self) -> float:
        """Return the current speed."""
        return self.speed
