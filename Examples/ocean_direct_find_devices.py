# -*- coding: utf-8 -*-
"""
Created 9/18/2024
This program reads information about any connected spectrometers, such as serial number and device ID.
@author: Adam B
"""
from OceanDirect import OceanDirectAPI, OceanDirectError


def main():
    # Initialize the OceanDirectAPI.
    od = OceanDirectAPI()

    # Find all connected USB devices.
    device_count = od.find_usb_devices()
    device_ids = od.get_device_ids()

    if device_count == 0:
        print("No device found.")
        return

    device = od.open_device(device_ids[0])
    serial_number = device.get_serial_number()

    # Print API and device information
    api_version = od.get_api_version_numbers()
    print(f"OceanDirect Version: {api_version[0]}.{api_version[1]}.{api_version[2]}")
    print(f"Device ID: {device_ids[0]}")
    print(f"Serial Number: {serial_number}")

    # Try to get firmware and FPGA versions
    try:
        firmware_version = device.Advanced.get_revision_firmware()
        print(f"Firmware Version: {firmware_version}")
    except OceanDirectAPI.OceanDirectError as err:
        print(f"Firmware Version Error: {err.get_error_details()}")

    try:
        fpga_version = device.Advanced.get_revision_fpga()
        print(f"FPGA Version: {fpga_version}")
    except OceanDirectError as err:
        print(f"FPGA Version Error: {err.get_error_details()}")
    # Prompt the user to press Enter before closing
    input("Press Enter to close...")

    # Close the device and then shutdown the API
    try:
        del od
        print(f"Device {serial_number} closed and OceanDirect was shutdown.")
    except Exception as e:
        print(f"Error during shutdown: {e}")


if __name__ == '__main__':
    main()
