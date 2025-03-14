import time

from MicroEpsilon import MEDAQLib, ERR_CODE, SENSOR_TYPE

# Tell MEDAQLib what type of sensor you want to use
sensor_instance = MEDAQLib.CreateSensorInstance(SENSOR_TYPE.SENSOR_IFC2421)

# Specify the interface that MEDAQLib should use to communicate with the sensor
sensor_instance.SetParameterString("IP_Interface", "TCP/IP")
sensor_instance.SetParameterString("IP_RemoteAddr", "169.254.168.150")

# OPTIONAL: Enable Logfile writing
# sensor_instance.SetParameterInt("IP_EnableLogging", 1)

# OPTIONAL: Enable automatic MEDAQLib and sensor setup
sensor_instance.SetParameterInt("IP_AutomaticMode", 3)
time.sleep(1)

# Try to open communication to sensor using the specified interface
sensor_instance.OpenSensor()
if sensor_instance.GetLastError() != ERR_CODE.NO_ERROR:
    print("Failed to open sensor instance")
    # Print the OpenSensor Error message
    print(sensor_instance.GetError())
else:
    while True:
        print("Successfully opened sensor instance")
        # Check whether there is data to read from the sensor
        currently_available = sensor_instance.DataAvail()
        # Check whether DataAvail returned an error
        if sensor_instance.GetLastError() != ERR_CODE.NO_ERROR:
            # Print the DataAvail Error message
            print(sensor_instance.GetError())
        elif currently_available > 0:
            # Get the most recent measurement from the sensor
            poll_data = sensor_instance.Poll(1)
            print("Most recent measurement: ", poll_data[1])
            # Bulk transfer all currently available data from the MEDAQLib internal buffer
            transfer_data = sensor_instance.TransferData(currently_available)
            print("Transferred data: ", transfer_data)
            break
        else:
            print("No data available")
            time.sleep(0.1)

# Close the communication interface and release the sensor instance
sensor_instance.CloseSensor()
sensor_instance.ReleaseSensorInstance()
