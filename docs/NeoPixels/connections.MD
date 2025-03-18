# NeoPixel Connections
NeoPixel cables require three wires - power (typically 5V), ground, and data.  NeoPixel LED devices will typically actually have four wires (or places to attach them)  - power, ground, data In, and data out.  This allows you to "daisy chain" them together into strings of dozens of LEDs.


## Connectors
You can directly solder wires between NeoPixel devices, but that's not recommended[^1].  It's much more convenient to use add a pair of 3 Pin connectors to each device, allowing you to simply plug them together.

There are a few options for connectors.

### 3 pin JST-SM connectors {#JST-SM}

These are often used and some NeoPixel devices come with them already attached. 
  - Pros
    - You can get a variety of NeoPixel devices with them already attached - less soldering
  - Cons
    - they're a bit big and clunky - harder to hide in terrain


### 3 pin JST 1.25MM connectors {#JST 1.25MM}

I highly recommend these [JST 1.25MM 3 Pin Connectors](https://www.amazon.com/dp/B07DL4FNTF).  

  - Pros
    - They are pretty small and flexible - much easier to hide in terrain but not so small that the wires will have issues with a few dozen LEDs
  - Cons 
    -  They'll need to be soldered on, which can be moderately challenging for a beginner


[^1]: There are rare cases where this makes sense, usually in vary tight spaced constrained projects.