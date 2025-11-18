import update_devices

def test_update_workflow():
    devices = [
        {"name": "TestDevice1", "updated": False},
        {"name": "TestDevice2", "updated": True}
    ]

    # Simulate update
    for device in devices:
        if not update_devices.check_update_status(device):
            update_devices.push_update(device)

    # Ensure all devices are updated after running workflow
    assert devices[0]["updated"] == True
    assert devices[1]["updated"] == True

