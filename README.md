# Geocode U.S. Weather Stations

This Python utility enriches a JSON dataset of U.S. weather stations with latitude and longitude using the [OpenStreetMap Nominatim](https://nominatim.org/) geocoding service via the `geopy` library.

Originally developed for [TodaysRecordHigh.com](https://todaysrecordhigh.com), where station-level weather data is visualized and compared to historical records, this tool is general-purpose and can be used in any project where location coordinates are needed for named city/state entries.

---

## Features

- Accepts a JSON file of weather stations or place records with `city` and `state` fields
- Geocodes each entry using `city, state, USA` format
- Appends `latitude` and `longitude` to each record
- Saves a new enriched JSON file with coordinates

---

## Example Input

```json
[
  {
    "name": "Minneapolis / St Paul",
    "city": "Minneapolis",
    "state": "MN",
    "stateName": "Minnesota",
    "id": 12345
  }
]
```

---

## Example Output

```json
[
  {
    "name": "Minneapolis / St Paul",
    "city": "Minneapolis",
    "state": "MN",
    "stateName": "Minnesota",
    "id": 12345,
    "latitude": 44.9778,
    "longitude": -93.2650
  }
]
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/clintmmcahon/geocode-stations.git
cd geocode-stations
```

2. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Place your cleaned input file as `filtered_stationData_cleaned.json` in the root directory.

Then run:

```bash
python geocode_stations.py
```

Output will be saved to:

```bash
filtered_stationData_with_coords.json
```

---

## Notes

- This script uses OpenStreetMap Nominatim, which is **rate limited to 1 request per second**.
- Results may be `null` if a location can't be resolved (e.g., ambiguous city names).
- This tool can be adapted to use coordinates from other APIs (Google Maps, HERE, Mapbox).

---

## License

MIT — free to use, modify, and share.

---

## Author

Developed by [@clintmcmahon](https://github.com/clintmcmahon) for TodaysRecordHigh.com, but built for use in any city/state geolocation project.
