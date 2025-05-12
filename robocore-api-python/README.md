RoboCore-API

Official Python SDK for controlling RoboCore robots over WebSocket—now fully Jetson-compatible!

Badges:
- PyPI: https://pypi.org/project/robocore-api
- Build Status: https://github.com/your-username/robocore-api/actions/workflows/ci.yml
- License: MIT (see LICENSE file)

---

Features
--------
• Async WebSocket client to connect(), move_forward(speed) & read_sensors()
• Fallback to websocket-client if websockets isn’t available (e.g. on Jetson)
• CLI commands:
    • robocore-cli info <uri>       — show sensor data
    • robocore-cli forward <uri> <speed>  — move at <speed> m/s
• Examples, tests, and CI included

---

Installation
------------
For most Linux & macOS (x86_64):
    pip install robocore-api

On NVIDIA Jetson (ARM64):
Jetson may prefer the native websocket-client library. Install with the jetson extra:
    pip install robocore-api[jetson]

---

Quickstart
----------
from robocore_api.client import RobotClient
import asyncio

async def main():
    client = RobotClient("ws://your-robot.local:8765")
    await client.connect()
    await client.move_forward(0.5)       # 0.5 m/s
    sensors = await client.read_sensors()
    print("Sensors:", sensors)
    await client.disconnect()

asyncio.run(main())

---

Command-Line Interface
----------------------
# Show sensor data
robocore-cli info ws://your-robot.local:8765

# Move forward at 1.2 m/s
robocore-cli forward ws://your-robot.local:8765 1.2

---

Development
-----------
# Clone the repo (or unzip the SDK folder)
git clone https://github.com/RoboCoreERC/robocore-api-complete.git
cd robocore-api

# Create a venv & install dev dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e ".[dev]"

# Run tests & lint
pytest
flake8 robocore_api

---

Compatibility
-------------
• Python 3.7+
• Linux x86_64 and ARM64 (Jetson/TX, Nano, Xavier)
• Tested on Ubuntu & NVIDIA JetPack

---

Repository Structure
--------------------
robocore-api/
├── LICENSE
├── README.md
├── setup.py
├── pyproject.toml
├── requirements-dev.txt
├── .github/
│   └── workflows/ci.yml
├── robocore_api/
│   ├── __init__.py
│   ├── client.py
│   └── cli.py
├── examples/
│   └── example.py
└── tests/
    └── test_client.py

---

Contributing & Support
----------------------
1. Fork & create a feature branch
2. Open a pull request against main
3. CI will run tests & lint automatically
4. We welcome issues, suggestions, and PRs!

---

License
-------
This project is licensed under the MIT License. See LICENSE for details.
