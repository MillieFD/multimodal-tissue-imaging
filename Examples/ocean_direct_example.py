from OceanDirect import OceanDirectAPI

if __name__ == '__main__':
    ocean_devices_manager = OceanDirectAPI()
    ids = ocean_devices_manager.get_device_ids()
    print(ids)
    device_1 = ocean_devices_manager.open_device(ids[0])
    print("Successfully opened device")
    device_1.close_device()
    print("Successfully closed device")