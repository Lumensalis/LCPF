
# 
(this assumes you have everything installed on your controller / [CIRCUITPY_DRIVE](CIRCUITPY_DRIVE.MD))


## Playing with Demos

There are files for demos In [***CIRCUITPY_DRIVE***](CIRCUITPY_DRIVE.MD)__:\libs\TerrainTronics\Demos_

[***CIRCUITPY_DRIVE***](CIRCUITPY_DRIVE.MD)__:\code.py__ is a file that gets automatically run when the controller boots

There are a number of ways to run a demo. For example, to run  **CaernarfonLavaLights** (at [***CIRCUITPY_DRIVE***](CIRCUITPY_DRIVE.MD)__:\libs\TerrainTronics\Demos\CaernarfonLavaLights.py__ ),  [***CIRCUITPY_DRIVE***](CIRCUITPY_DRIVE.MD)__:\code.py__ could look like
```
from TerrainTronics.Demos import CaernarfonLavaLights
CaernarfonLavaLights.demoMain()
```
or you could copy the contents of [***CIRCUITPY_DRIVE***](CIRCUITPY_DRIVE.MD)__:\libs\TerrainTronics\Demos\CaernarfonLavaLights.py__ into [***CIRCUITPY_DRIVE***](CIRCUITPY_DRIVE.MD)__:\code.py__ and add ```demoMain()```
```
# copied contents from CaernarfonLavaLights.py ...

demoMain()
``` 
at the end

