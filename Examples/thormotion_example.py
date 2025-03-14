import thormotion


def main():
    device = thormotion.KDC101("27xxxxxx") # Replace "27xxxxxx" with the serial number of your device
    device.identify()
    device.home()
    device.move_absolute(4)
    device.move_absolute(0)


if __name__ == "__main__":
    main()
