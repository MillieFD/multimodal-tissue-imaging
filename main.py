# import asyncio
# import thormotion
import time

from RPi import GPIO

TARGET_SERIAL_NUMBER = "27266788"

if __name__ == '__main__':
    # ocean_devs_manager = OceanDirectAPI()
    # _ = ocean_devs_manager.find_devices()  # Need to find devices before calling get_device_ids()
    # ids = ocean_devs_manager.get_device_ids()
    # print(f"Device IDs: {ids}")
    # if not ids:
    #     print("No Ocean devices found")
    #     exit(0)
    # hdx = ocean_devs_manager.open_device(ids[0])
    # if hdx is None:
    #     print("Failed to open HDX spectrometer")
    #     exit(0)
    # print(f"Connected to device {ids[0]}")
    # hdx.close_device()
    # print(f"Disconnected from device {ids[0]}")

    # -------------------------------------------

    # dev = thormotion.KDC101(TARGET_SERIAL_NUMBER)
    # asyncio.run(dev.home_async(1))
    # dev.move_absolute(1, 0.5)
    # dev.move_absolute(1, 0)

    # -------------------------------------------

    # confocal = MEDAQLib.CreateSensorInstance(SENSOR_TYPE.SENSOR_IFD2421)
    # confocal.SetParameterString("IP_Interface", "TCP/IP")
    # confocal.SetParameterString("IP_RemoteAddr", "169.254.168.150")
    # confocal.SetParameterInt("IP_EnableLogging", 1)
    # confocal.SetParameterInt("IP_AutomaticMode", 3)
    # confocal.OpenSensor()
    # if confocal.GetLastError() == ERR_CODE.NO_ERROR:
    #     print("Successfully opened sensor instance")
    #     data = confocal.Poll(1)
    #     print("raw: {}, scaled: {}".format(data[0], data[1]))
    #     confocal.CloseSensor()
    # else:
    #     print("Failed to open sensor instance")
    # confocal.ReleaseSensorInstance()

    # -------------------------------------------

    GPIO.setmode(GPIO.BCM)

    RELAY_CH1 = 26  # GPIO26 (physical pin 37)
    RELAY_CH2 = 20  # GPIO20 (physical pin 38)
    RELAY_CH3 = 21  # GPIO21 (physical pin 40)

    GPIO.setup(RELAY_CH1, GPIO.OUT)
    GPIO.setup(RELAY_CH2, GPIO.OUT)
    GPIO.setup(RELAY_CH3, GPIO.OUT)

    GPIO.output(RELAY_CH1, GPIO.HIGH)
    print("Relay Channel 1 is ON")
    time.sleep(1)
    GPIO.output(RELAY_CH1, GPIO.LOW)
    print("Relay Channel 1 is OFF")
