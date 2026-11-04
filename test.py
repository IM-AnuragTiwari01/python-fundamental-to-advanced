import requests
import psutil
import pprint

# 1. Get Battery Information
def get_battery_info():
    battery = psutil.sensors_battery()
    if battery:
        print(f"Battery Percentage: {battery.percent}%")
        print(f"Power Plugged In: {battery.power_plugged}")
        # Convert seconds to hours/minutes if not plugged in
        if battery.secsleft != psutil.POWER_TIME_UNLIMITED and battery.secsleft != psutil.POWER_TIME_UNKNOWN:
            hours, remainder = divmod(battery.secsleft, 3600)
            minutes, _ = divmod(remainder, 60)
            print(f"Time Left: {hours}h {minutes}m")
        else:
            print("Time Left: N/A or Unlimited")
    else:
        print("Battery information is not available on this device.")

# 2. Get Approximate Location via IP Address
def get_ip_location():
    try:
        response = requests.get('https://ipinfo.io', timeout=5)
        data = response.json()
        print(data)
        # print(f"IP Address: {data.get('ip')}")
        # print(f"City: {data.get('city')}")
        # print(f"Region/State: {data.get('region')}")
        # print(f"Country: {data.get('country')}")
        # print(f"Coordinates (Lat, Long): {data.get('loc')}")
        # print(f"ISP / Organization: {data.get('org')}")
    except Exception as e:
        print(f"Could not retrieve location: {e}")

# 3. Get System/Device Info (CPU & Memory)
def get_system_info():
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    memory = psutil.virtual_memory()
    print(f"Total Memory: {round(memory.total / (1024**3), 2)} GB")
    print(f"Used Memory: {round(memory.used / (1024**3), 2)} GB ({memory.percent}%)")

if __name__ == "__main__":
    print("=== BATTERY STATUS ===")
    get_battery_info()
    
    print("\n=== LOCATION INFO (IP-based) ===")
    get_ip_location()
    
    print("\n=== SYSTEM RESOURCES ===")
    get_system_info()
