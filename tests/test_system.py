import math
import sys
from pathlib import Path

# Ensure project root is on sys.path when tests are executed from the tests directory
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common.schema import TelemetryPacket
from deck.alarms.alarms import AlarmManager
from deck.radio.radio import DeckRadio
from deck.telemetry.telemetry import TelemetryCollector
from deck.ui.ui import DeckUI
from rover.claw.claw import ClawController
from rover.drive.drive import DriveSystem
from rover.faults.faults import FaultDetector
from rover.radio.radio import RoverRadio
from rover.sensors.sensors import SensorSuite


def test_alarm_manager():
    mgr = AlarmManager()
    mgr.raise_alarm("low_battery")
    assert mgr.is_active("low_battery")
    mgr.clear_alarm("low_battery")
    assert not mgr.is_active("low_battery")


def test_drive_and_claw():
    drive = DriveSystem()
    drive.set_speed(2.5)
    assert math.isclose(drive.get_speed(), 2.5)
    drive.stop()
    assert drive.get_speed() == 0.0

    claw = ClawController()
    claw.close_claw()
    assert not claw.is_open()
    claw.open_claw()
    assert claw.is_open()


def test_fault_detector():
    faults = FaultDetector()
    faults.report_fault("motor")
    assert faults.has_faults()


def test_sensor_and_telemetry_range():
    sensors = SensorSuite()
    temp = sensors.read_temperature()
    assert -80.0 <= temp <= 0.0

    collector = TelemetryCollector()
    packet = collector.collect()
    assert isinstance(packet, TelemetryPacket)
    assert -80.0 <= packet.temperature <= 0.0
    assert 0.0 <= packet.battery_level <= 100.0


def test_ui_and_radio_link():
    deck_radio = DeckRadio()
    rover_radio = RoverRadio()
    deck_radio.connect(rover_radio)

    # Rover sends telemetry
    packet = TelemetryCollector().collect()
    rover_radio.transmit(packet)

    received = deck_radio.receive()
    assert isinstance(received, TelemetryPacket)

    ui = DeckUI()
    ui.display_message("hello")
    assert ui.log == ["hello"]

    # Deck sends command to rover
    deck_radio.send("move")
    assert rover_radio.receive() == "move"
