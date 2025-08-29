"""Sensor suite for the rover."""

import random


class SensorSuite:
    """Provide access to rover sensors."""

    def read_temperature(self) -> float:
        """Return a simulated temperature reading."""
        return random.uniform(-80.0, 0.0)
