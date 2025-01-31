# Maya-Flask Integration

This project integrates Maya with a Flask server for managing object transforms and an inventory system.

## Features:
- **Maya Plugin**: Select objects, get transformations, and send them to the server.
- **Flask Server**: Handles transformation and inventory management.
- **SQLite Database**: Stores inventory data.
- **PyQt UI**: Allows inventory viewing and management.

## Installation
1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `python server.py`
3. Run the UI: `python ui.py`
4. Use Maya to send transformations.

## API Endpoints
- **/transform**: Receives full transformation data.
- **/add-item**: Adds inventory item.
- **/remove-item**: Removes inventory item.

## License
MIT
