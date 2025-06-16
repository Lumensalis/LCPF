
# INTERNAL

This is collection of notes / reminders for attempting to get JTAG debug working under WSL


https://developer.espressif.com/blog/espressif-devkits-with-wsl2/


https://learn.microsoft.com/en-us/windows/wsl/connect-usb

## setup permissions in WSL 
  - https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/api-guides/jtag-debugging/configure-builtin-jtag.html
  - ```sudo mv 60-openocd.rules /etc/udev/rules.d```
  - sudo service udev restart
  - sudo service udev restart
  - sudo udevadm control --reload
  - sudo udevadm trigger

- stty -F /dev/ttyACM0


C:\Users\jbrel>wsl --shutdown

C:\Users\jbrel>wsl --update