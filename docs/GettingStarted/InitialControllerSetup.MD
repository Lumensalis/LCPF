If you have a controller which supports UF2 (like an ESP32-S2 or ESP32-S3),  the common setup steps are

 
  - install Circuit Python
  - install to [CIRCUITPY_DRIVE](../CIRCUITPY_DRIVE.MD)
    - dependencies from bundles
    - copy the TT code to [CIRCUITPY_DRIVE](../CIRCUITPY_DRIVE.MD):\lib
    


Initial Configuration


# settings.toml
This is a file on the [CIRCUITPY drive](../CIRCUITPY_DRIVE.MD) drive ( [***CIRCUITPY***](../CIRCUITPY_DRIVE.MD):\settings.toml ) 
which is used to set the configuration for the local controller.  For example :
 
```
# make available under "http://MyControllerHostname.local"
TTCP_HOSTNAME = "MyControllerHostname"

CIRCUITPY_WIFI_SSID = "MyWifiSSID"
CIRCUITPY_WIFI_PASSWORD = "MyWifiPassword"
```
