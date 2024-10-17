# This is a test Python script.
from oceandirect.OceanDirectAPI import OceanDirectAPI

if __name__ == '__main__':
    ocean_devs_manager = OceanDirectAPI()
    ids = ocean_devs_manager.get_device_ids()
    device_1 = ocean_devs_manager.open_device(ids[0])

    print('Hello, World!')
