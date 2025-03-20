# NeoPixel Connections
NeoPixel cables require three wires - power (typically 5V), ground, and data.  NeoPixel LED devices will typically actually have four wires (or places to attach them)  - power, ground, data In, and data out.  This allows you to "daisy chain" them together into strings of dozens of LEDs.


## Connectors
You can directly solder wires between NeoPixel devices, but that's not recommended[^1].  It's much more convenient to use add a pair of 3 Pin connectors to each device, allowing you to simply plug them together.

I prefer the 3 pin JST 1.25MM connectors, but there are a many options for connectors.  However, if you're considering choosing something else you should take into account the following considerations:
  - Needs to have at least 3 pins / wires (VDD/GND/DATA)
  - small enough to be reasonably easy to hide / work into terrain
  - chained female / male plugs & sockets
    - prevents connecting Data Out from one link to Data Out of the next
    - female tied to Data In, male pins tied to Data Out recommended, as PCB sockets for the start of the chain (which needs to be Data Out) are more often male pins
  - polarized / keyed sockets / plugs so you can't plug them in backwards
  - not in common use for anything other connections (i.e. JST servo connections)
  - avoids making it easy to plug in to the wrong place
  - simple to connect / disconnect
  - durable enough for more than a few reconnect cycles
  - big enough wire to handle a decent chain of LEDS
     - WS2812Bs can draw up to 60ma at full brightness - 16 LEDs can pull up an amp
     - OTOH splicing a 5v "boost" in the middle of  chain works well

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


[^1]: There are rare cases where this makes sense, usually in very tight space constrained projects.