
# LOLIN (Wemos) S2 Mini

https://circuitpython.org/board/lolin_s2_mini/

## Initial setup
Connect a Windows PC to your controller via USB
- If a new drive labeled CIRCUITPY appears, it's already set up for UF2/CircuitPython
- If nothing happens, you need to do the initial install
  - note that "nothing happens" is a very good description for an S2 Mini without a 
UF2 bootloader.  There is no power light, and the board will not appear as a 
USB device.  People sometimes assume the board is dead and return them...

### Install CircuitPython on fresh controller (no UF2 bootloader)
  WARNING : this will erase currently everything on your controller

This should be a simple (although slightly tedious) install, IF you follow the 
directions carefully AND the online Installer hasn't changed.

  - goto https://circuitpython.org/board/lolin_s2_mini/
  - There should be an install section on the right: ![alt text](image.png)
  - click "OPEN INSTALLER" 

    ![alt text](image-1.png)
  - select "Full CircuitPython 9.2.4 Install"
  - click "Next"
  - ![alt text](image-2.png) 
  - Click "Connect"
  - You most likely will NOT see your controller listed at first 
  - ![alt text](image-3.png)
  - While connected via USB, press and hold the BOOT button, double click the RESET button, then release the BOOT button.This should restart the controller in update mode, and your controller should appear in the list 
  - ![alt text](image-4.png)
  - Select your controller ( ESP32-S2 (COM6) for this example) and press "Connect"
  - ![alt text](image-5.png)
  - select "Continue"
  - flash will be erased
  - ![alt text](image-6.png)
  - If you don't see a new drive appear with a label  like S2MINIBOOT or CIRCUITPY, you probably need to reboot your controller. Double press RESET, disconnect/reconnect USB.  You should now see a new drive appear in file explorer
    ![alt text](image-7.png)

  - Click "Select S2MINIBOOTDRIVE" and select the new drive (F: for this example)
  - ![alt text](image-8.png)
  - Click "Edit Files"
  - If you see this, click OK : ![alt text](image-9.png)
  - The drive should now be labeled CIRCUITPY 
  
   ![alt text](image-11.png)

  - ![alt text](image-10.png)
  - Select the CIRCUITPY drive
  - ![alt text](image-12.png)
  - Put in your WiFi info
  - ![alt text](image-13.png)
    
  - more details under the "Install, Repair, or Update UF2 Bootloader" section at https://circuitpython.org/board/lolin_s2_mini/
