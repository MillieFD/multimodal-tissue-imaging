from OceanDirect import OceanDirectAPI, OceanDirectError

if __name__ == "__main__":
    od = OceanDirectAPI()
    od.find_usb_devices()
    device_ids = od.get_device_ids()

    if not device_ids:
        print("No devices found.")
        exit(1)

    device_id = device_ids[0]  # Get the first device ID from the list
    try:
        device = od.open_device(device_id)  # Open the device with the given ID
        sn = device.get_serial_number()  # Retrieve the serial number of the device
        print(f"Opened Device, ID = {device_id}, Serial Number: {sn}\n")  # Print info about the device

        try:
            wavelengths = device.get_wavelengths()
            intensities = device.get_formatted_spectrum()
            for wavelength, intensity in zip(wavelengths, intensities):
                print(f"Wavelength: {round(wavelength, 5)} nm, Intensity:  {round(intensity, 8)}")
            print(f"\nRecorded {len(wavelengths)} wavelengths")

        except OceanDirectError as e:
            # Print any errors encountered during the device operation
            print(f"Error during device operation: {e.get_error_details()}")

        device.close_device()
        print("Closed device")

    except OceanDirectError as e:
        # Print any errors encountered during device opening
        print(f"Error opening device: {e.get_error_details()}")
