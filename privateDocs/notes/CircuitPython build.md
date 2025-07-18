# using wsl

## file system
USE WSL FILE SYSTEM, i.e. **~/git/...**
Using the "mapped" windows 11 file system, i.e. **/mnt/c/Users/jbrel/git/circuitpython**, dramatically increases build time

## wsl install

  - ```sudo apt update```
  - install brew
    - ```bash
sudo apt-get install build-essential procps curl file git```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
  - follow instruction at https://learn.adafruit.com/building-circuitpython/build-circuitpython and https://learn.adafruit.com/building-circuitpython/espressif-build
    - ```bash
cd circuitpython
pip3 install --upgrade -r requirements-dev.txt
pip3 install --upgrade -r requirements-doc.txt

cd ports/espressif/
make fetch-port-submodules
pre-commit install
cd ../..
make fetch-tags
```

```
    - in fresh shell
      ```bash
# ok for deactivate to fail - only needed if you're in a python venv
deactivate

cd circuitpython
cd ports/espressif/

esp-idf/install.sh
. esp-idf/export.sh 
cd ../..
pip3 install --upgrade -r requirements-dev.txt
pip3 install --upgrade -r requirements-doc.txt



```
  - old...
    - pip install huffman
    - make -j16 -C mpy-cross
    - sudo apt install python3.10-venv
    - cd ports/espressif/
    - esp-idf/install.sh 
    - ```. esp-idf/export.sh```
    - pip install minify_html jsmin

after install
  - always set environment before any build commands
    - ```bash
cd circuitpython
cd ports/espressif/
. esp-idf/export.sh
```
  - build mpy_cross ( in **./circuitpython** )
    ```bash

make -j16 -C mpy-cross
```

- build mpy_cross ( in **./circuitpython** )
make -j30 BOARD=lolin_s2_mini
```