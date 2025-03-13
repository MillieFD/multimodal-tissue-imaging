# Ocean Direct API Overview

OceanDirect is a multi-platform device driver for Ocean Optics spectrometers, designed specifically for embedded
applications needing to run in resource-constrained hardware environments.

The OceanDirect library is written in C/C++ to provide a lightweight and high-speed solution suitable for real-time 
operation on resource-constrained hardware such as embedded devices. Ocean Insight do not share this `.cpp` source 
code, but instead provide the library as a pre-compiled binary.
Different versions of this precompiled library are available, each targeting a specific hardware architecture (`x86` 
or `arm64`) and operating system (`Linux` or `macOS` or `Windows`). Thus, the library may appear as:

| Filename               | Purpose                                                                                                                                    |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `liboceandirect.so`    | Shared-object for Linux                                                                                                                    |
| `liboceandirect.dylib` | Dynamic library for macOS                                                                                                                  |
| `OceanDirect.dll`      | Dynamically-linked library for Windows                                                                                                     |
| `NETOceanDirect.dll`   | Dynamically-linked library for the dotnet framework 4.7.2 on Windows, which then references `OceanDirect.dll` (both files must be present) | 

> [!ERROR] Not all platforms are maintained
> OceanInsight are currently only actively developing the **Windows x86** version of the Ocean Direct API.
> All other versions may not incorporate the latest features.

The OceanDirect API for your target framework can be accessed from the [Ocean Insight Downloads Page][1]. Each 
downloaded package contains the following directories:

[1]: (https://www.oceanoptics.com/software/oceandirect/)

| Directory  | Contents                                                            |
|------------|---------------------------------------------------------------------|
| `/doc`     | Supporting documentation such as the README.md                      |
| `/driver`  | Driver (written in C/C++) to handle communication with the device   |
| `/EULA`    | End-User Licensing Agreement (summary below)                        |
| `/include` | Headers  used to build the OceanDirect library.                     |
| `/lib`     | Precompiled library which can be referenced in client applications. |
| `/test`    | Example projects and demos                                          |

In addition to the precompiled binary, OceanInsight also provides header files (.h and .hpp) for all public-facing 
C/C++ methods in the library.
These files show the function signatures, thus enabling users to build their own wrappers if necessary.

### Adding OceanDirectAPI to Python

1. Create a new `OceanDirect` directory in the project's root directory
2. Copy the following files into the `oceandirect` directory:
	- `OceanDirectAPI.py`
	- `od_logger.py`
	- `sdk_properties.py`
	- `__init__.py` is not essential for functionality, but adds convenience.
3. Create a `bin` directory inside the first `oceandirect` directory. You can use a different directory name if required (e.g. `lib`), but make sure to update the `lib_path` variable in `sdk_properties.py`.
4. Copy the library binary (`liboceandirect.so` and/or `liboceandirect.dylib` and/or `OceanDirect.dll`) into the `bin` directory

After following these instructions, the file structure of the project should follow this arrangement.

```
project_root/
├── main.py
└── OceanDirect/
	├── __init__.py
    ├── OceanDirectAPI.py
    ├── od_logger.py
    ├── sdk_properties.py
    └── lib/
        └── liboceandirect.so
        └── liboceandirect.dylib
        └── OceanDirect.dll
```

### ⚙️ Libusb

OceanDirect dynamically binds to `libusb` in order to communicate with USB devices.
You may already have `libusb` installed. If not, follow the instructions below.

**MacOS**

Install libusb using [homebrew](https://brew.sh):

```bash
brew install libusb
```

**Linux**

Install libusb using your package manager:

```bash  
sudo apt updatesudo apt install libusb-1.0-0-dev
```  

**Windows**  

Install libusb using [vcpkg](https://vcpkg.io/en/):

```bash 
vcpkg install libusb
```

### Using OceanDirectAPI

1. Add `from OceanDirect import OceanDirectAPI` to the top of your python file
2. Create an instance of the OceanDirectAPI class: `ocean_devices_manager = OceanDirectAPI()`
3. For setup troubleshooting, see [[Ocean Direct API Python Troubleshooting]]

> [!TIP] OceanDirectAPI python class
> The [[OceanDirectAPI Python Class]] manages the connection to the `OceanDirectAPI` C/C++ class in the OceanDirect 
> library (`.so` or `.dylib` or `.dll`) and manages a list of connected devices.

Member functions from the `OceanDirectAPI` class can now be called through the `ocean_devices_manager` object. A 
full list of available functions can be found on the [[OceanDirectAPI Python Class]] page.
These functions are used to find, open, and close connected devices. A new instance of the `spectrometer` python 
class is created for each connected device (irrespective of whether the device is open or closed).

```python
# This is a test Python script.  
from OceanDirect import OceanDirectAPI

if __name__ == '__main__':
	ocean_devs_manager = OceanDirectAPI()
	ids = ocean_devs_manager.get_device_ids()
	device_1 = ocean_devs_manager.open_device(ids[0])
```

> [!INFO] Spectrometer python class
> The OceanDirect Python API also includes a class for an individual spectrometer. The [[Spectrometer Python Class]]
> manages the connection to the `spectrometer` C/C++ class in the precompiled OceanDirect library, and each instance 
> of the `spectrometer` class contains all the information concerning the spectrometer it represents.

In the code example above, `device_1` is an instance of the `spectrometer` class.
A full list of available functions can be found on the [[Spectrometer Python Class]] page.
These functions are used to get and set device parameters, fetch device information, and take measurements.

### 📝 License
OceanDirect is covered by the Ocean Optics end-user licensing agreement (Ocean Insight Incorporated, all rights 
reserved). All source-code and accompanying information remains the property of Ocean Insight Incorporated and its 
suppliers. The intellectual and technical concepts contained are proprietary to Ocean Insight Incorporated and its 
suppliers and may be covered by U.S. and Foreign Patents, patents in process, and are protected by trade secret or 
copyright law. Dissemination of this information or reproduction of this material is strictly forbidden unless prior 
written permission is obtained from Ocean Insight Incorporated.