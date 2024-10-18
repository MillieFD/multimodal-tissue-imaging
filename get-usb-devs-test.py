import usb.core
import usb.util

def list_usb_devices():
    devices = usb.core.find(find_all=True)
    device_list = [dev for dev in devices if dev.idVendor and dev.idProduct]

    if not device_list:
        print("No USB devices")
    else:
        print("Found {} device(s)".format(len(device_list)))
        for device in device_list:
            try:
                manufacturer = usb.util.get_string(device, device.iManufacturer)
                product = usb.util.get_string(device, device.iProduct)
                print(f"Device: {manufacturer} {product}")
            except ValueError as e:
                print(f"Device: Unable to retrieve string descriptors ({e})")
            except usb.core.USBError as e:
                print(f"Device: USB error ({e})")
            print(f"Vendor ID: {device.idVendor}, Product ID: {device.idProduct}")

if __name__ == '__main__':
    list_usb_devices()