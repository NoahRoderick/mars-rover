# Mars Rover

## Features
- 3D‑printable chassis designed for rapid prototyping.
- Raspberry Pi 5 controller running Python‑based mission software.
- Modular sensor bays and expandable motor drivers.

## Quick Start
```bash
git clone https://github.com/your-org/mars-rover.git
cd mars-rover
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python rover.py --config config/rover.yaml
```
Adjust parameters inside [`config/rover.yaml`](config/rover.yaml) to match your hardware setup.

## Hardware Reference
See [docs/](docs/) for wiring diagrams and additional hardware notes.
Mechanical models suitable for fabrication are located in the [cad/](cad/) directory.

