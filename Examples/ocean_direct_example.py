from OceanDirect import OceanDirectAPI

if __name__ == "__main__":
    ocean_devices_manager = OceanDirectAPI()
    ids = ocean_devices_manager.get_device_ids()
    print(ids)
    spectrometer_instance = ocean_devices_manager.open_device(ids[0])
    print("Successfully opened device")
    spectrometer_instance.close_device()
    print("Successfully closed device")
