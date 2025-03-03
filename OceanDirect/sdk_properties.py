# -*- coding: utf-8 -*-
"""
Created on 9th January 2019

@author: Ocean Insight Inc.
"""

import os.path
import platform

## Dynamically assign the path to `liboceandirect`
if platform.system() == 'Darwin':
    #For OSX, make sure that OCEANDIRECT_HOME points to the ./bin folder.
    lib_name=("liboceandirect.dylib")
elif os.name == 'nt':
    #For windows, make sure that OCEANDIRECT_HOME points to the ./bin folder.
    lib_name=("OceanDirect.dll")
else:
    #For linux, make sure that LD_LIBRARY_PATH and OCEANDIRECT_HOME points to the ./bin folder.
    lib_name=("liboceandirect.so")

module_path=os.path.dirname(__file__)
lib_path = module_path + os.path.normpath("/bin/" + lib_name)
