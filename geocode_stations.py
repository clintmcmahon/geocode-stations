import json
import time
from geopy.geocoders import Nominatim

# Load cleaned data
with open("filtered_stationData_cleaned.json", "r") as f:
    stations = json.load(f)

# Initialize geocoder (use your own user agent string)
geolocator = Nominatim(user_agent="todaysrecordhigh-locator")

# Enrich with coordinates
for station in stations:
    query = f"{station['city']}, {station['state']}, USA"
    print(query)
    try:
        location = geolocator.geocode(query, timeout=10)
        if location:
            station["latitude"] = location.latitude
            station["longitude"] = location.longitude
        else:
            station["latitude"] = None
            station["longitude"] = None
    except Exception as e:
        station["latitude"] = None
        station["longitude"] = None
        print(f"Failed to geocode: {query} – {e}")
    time.sleep(1)  # Comply with Nominatim rate limit

# Save enriched file
with open("filtered_stationData_with_coords.json", "w") as f:
    json.dump(stations, f, indent=2)

print("Geocoding complete. Saved to filtered_stationData_with_coords.json")
