import json
import time
devices = [
    {"name": "Router1", "updated": False},
    {"name": "Switch1", "updated": True},
    {"name": "Firewall1", "updated": False}
]


def check_update_status(device):
    return device["updated"]


def push_update(device):

    print(f"Pushing update to {device['name']}...")
    time.sleep(1)
    device["updated"] = True
    print(f"Update completed for {device['name']}.")


def update_all_devices():

    for device in devices:
        if not check_update_status(device):
            print(f"{device['name']} is NOT updated. Applying update...")
            push_update(device)
        else:
            print(f"{device['name']} is already updated.")

    return devices


if __name__ == "__main__":
    updated_devices = update_all_devices()
    with open("device_status.json", "w") as f:
        json.dump(updated_devices, f, indent=4)
    print("\nAll device statuses have been saved to device_status.json")

