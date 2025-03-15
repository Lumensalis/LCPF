If you have a controller which supports UF2 (like an ESP32-S2 or ESP32-S3),  the common setup steps are

 
  - install Circuit Python
  - install to to <CIRCUIT_PY>
    - (where CIRCUIT_PY is the drive letter for the USB file system that appears when you plug in the controller)
    - dependencies from bundles
    - copy the TT code to <CIRCUIT_PY>:\lib
    


Initial Configuration


# settings.toml
This is a file on the CIRCUITPY drive ( <CIRCUIT_PY>:\settings.toml ) 
which is used to set the configuration for the local controller.  For example :
 
```
# set controller type
TTCP_CONTROLLER = "WemosS2Mini"

# make available under "http://MyControllerHostname.local"
TTCP_HOSTNAME = "MyControllerHostname"

CIRCUITPY_WIFI_SSID = "MyWifiSSID"
CIRCUITPY_WIFI_PASSWORD = "MyWifiPassword"
```
