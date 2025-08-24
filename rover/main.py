"""Main entry point for the rover subsystem."""

from rover.drive import DriveSystem
from rover.claw import ClawController
from rover.sensors import SensorSuite
from rover.radio import RoverRadio
from rover.faults import FaultDetector


def main() -> None:
    """Demonstrate basic rover functionality."""
    drive = DriveSystem()
    claw = ClawController()
    sensors = SensorSuite()
    radio = RoverRadio()
    faults = FaultDetector()

    drive.set_speed(1.0)
    radio.transmit(f"Speed set to {drive.get_speed()}")

    temp = sensors.read_temperature()
    radio.transmit(f"Temperature reading: {temp:.2f}C")
    if temp < -50.0:
        faults.report_fault("Extreme cold")

    claw.close_claw()
    radio.transmit(f"Claw open? {claw.is_open()}")

    drive.stop()
    radio.transmit("Rover stopped")


if __name__ == "__main__":
    main()
