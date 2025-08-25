<<<<<<< HEAD
"""Placeholder module for Ui."""
=======
"""User interface for the deck subsystem."""

from typing import List


class DeckUI:
    """Simple UI component that records and displays messages."""

    def __init__(self) -> None:
        self.log: List[str] = []

    def display_message(self, message: str) -> None:
        """Display a message to the operator."""
        self.log.append(message)
        print(f"[UI] {message}")
>>>>>>> codex/create-project-directory-structure-6xgmpq
