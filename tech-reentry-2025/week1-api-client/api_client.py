import argparse, json, sys, urllib.request
# Simple API client demo without external packages.
# Default demo uses a public, no-key Open-Meteo endpoint for weather by latitude/longitude.
# Example:
#   python api_client.py --lat 28.5383 --lon -81.3792  # Orlando, FL

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m&forecast_days=1"

def fetch_weather(lat: float, lon: float) -> dict:
    url = OPEN_METEO_URL.format(lat=lat, lon=lon)
    with urllib.request.urlopen(url, timeout=10) as resp:
        data = resp.read()
    return json.loads(data.decode("utf-8"))

def main():
    ap = argparse.ArgumentParser(description="Simple API client demo")
    ap.add_argument("--lat", type=float, required=True, help="Latitude")
    ap.add_argument("--lon", type=float, required=True, help="Longitude")
    args = ap.parse_args()

    try:
        data = fetch_weather(args.lat, args.lon)
        hourly = data.get("hourly", {})
        times = hourly.get("time", [])
        temps = hourly.get("temperature_2m", [])
        print("=== Weather (Open-Meteo) ===")
        for t, temp in list(zip(times, temps))[:8]:
            print(f"{t}: {temp}°C")
        print("\nTip: Swap in any API you like and format the output.")
    except Exception as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
