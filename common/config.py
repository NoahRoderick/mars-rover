"""Configuration helpers."""

<<<<<<< HEAD
# Placeholder for configuration management.

=======
from dataclasses import dataclass
import os


@dataclass
class Config:
    """Simple configuration object loaded from environment variables."""

    rover_name: str = "MarsRover"
    deck_port: int = 8000

    @classmethod
    def from_env(cls) -> "Config":
        """Create a :class:`Config` from environment variables."""
        return cls(
            rover_name=os.getenv("ROVER_NAME", cls.rover_name),
            deck_port=int(os.getenv("DECK_PORT", cls.deck_port)),
        )
>>>>>>> codex/create-project-directory-structure-6xgmpq
