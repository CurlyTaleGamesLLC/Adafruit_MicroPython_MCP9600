# MCP9600 Micropython Library

I ported this library from CircuitPython to Micropython for use with PyKiln. An open source web based kiln controller that runs on an ESP32. 

If I made a mistake anywhere let me know and I'll update it.

You can check out the original library here:

https://github.com/adafruit/Adafruit_CircuitPython_MCP9600

## Getting Started

Make sure to install Micropython on your microcontroller. I've only tested this with the ESP32 but I imagine it should work on other microcontrollers with Micropython, you'll likely need to change the pins that are used for the i2c connection.

Copy the following files/folder:
* mcp9600_simpletest.py
* adafruit_mcp9600.py
* adafruit_register/
    * i2c_bit.py
    * i2c_bits.py
    * i2c_struct.py

In REPL run:
```
import mcp9600_simpletest
```

The mcp9600_simpletest example file will print out the interal chip temperature, the thermocouple temperature, and the difference between the two in degrees Celsius. It defaults to using a K type thermocouple, but other thermocouples are supported.

```
MicroPython v1.13 on 2020-09-02; ESP32 module with ESP32
Type "help()" for more information.
>>> import mcp9600_simpletest
(26.3125, 25.9375, -0.4375)
(26.25, 25.875, -0.4375)
(26.25, 25.875, -0.4375)
(26.25, 25.875, -0.4375)
(26.25, 25.875, -0.4375)
(26.25, 25.875, -0.4375)
(26.25, 25.875, -0.4375)
(26.25, 25.875, -0.4375)
(26.3125, 25.9375, -0.4375)
(26.25, 25.875, -0.4375)
(26.3125, 28.625, 2.25)
(26.25, 30.4375, 4.125)
(26.25, 30.8125, 4.5625)
(26.25, 31.0625, 4.875)
(26.25, 31.1875, 4.9375)
(26.25, 31.25, 5.0625)
(26.25, 31.4375, 5.1875)
```

