If you have a controller which supports UF2 (like an ESP32-S2 or ESP32-S3),  the common setup steps are

 
  - install Circuit Python
  - copy the TT code to <CIRCUIT_PY>:\lib
    - (where CIRCUIT_PY is the drive letter for the USB file system that appears when you plug in the controller)


Initial Configuration

 - Create/edit <CIRCUIT_PY>:\settings.toml
 
```
TTCP_CONTROLLER = "WemosS2Mini"

CIRCUITPY_WIFI_SSID = "MyWifiSSID"
CIRCUITPY_WIFI_PASSWORD = "MyWifiPassword"
```
