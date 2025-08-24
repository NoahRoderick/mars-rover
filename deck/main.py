"""Main entry point for the deck subsystem."""

from deck.ui import DeckUI
from deck.alarms import AlarmManager
from deck.telemetry import TelemetryCollector
from deck.radio import DeckRadio
from deck.sims import Simulation


def main() -> None:
    """Demonstrate basic deck functionality."""
    ui = DeckUI()
    alarms = AlarmManager()
    telemetry = TelemetryCollector()
    radio = DeckRadio()
    sim = Simulation()

    sim.start()
    packet = telemetry.collect()
    ui.display_message(f"Telemetry collected: {packet}")
    radio.send("Telemetry packet sent")
    if packet.battery_level < 20.0:
        alarms.raise_alarm("Low battery")
        ui.display_message("Alarm: Low battery")
    sim.stop()


if __name__ == "__main__":
    main()
