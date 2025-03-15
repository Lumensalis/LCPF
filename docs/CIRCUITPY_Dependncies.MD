

After a fresh CircuitPython install on a new controller, you'll still need to 
add the support framework for TerrainTronics boards.  The "lib" directory on your CIRCUITPY drive should be empty.

# Install external CircuitPython content
- download https://gitlab.com/lumensalis/demodata/-/raw/main/CircuitPyDependencies.zip
- unzip contents into your CIRCUITPY drive
- you should now have a bunch of adafruit files and directories in <CIRCUITPY>:\lib, and 
  a font5x8.bin file in the root directory

# Install TerrainTronics modules
- download https://gitlab.com/lumensalis/terraintronicscp/-/archive/main/terraintronicscp-main.zip?path=CircuitPyPartialImage
- open terraintronicscp-main-CircuitPyPartialImage.zip and go to **terraintronicscp-main-CircuitPyPartialImage**/**CircuitPyPartialImage**/**lib**.   You should see a directory called TerrainTronics.  Copy (drag & drop) this directory into <CIRCUITPY>:\li