# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Ported to Micropython by Ben Jones for Curly Tale Games LLC

import time
from machine import Pin, I2C
import adafruit_mcp9600

# frequency must be set for the MCP9600 to function.
# If you experience I/O errors, try changing the frequency.

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
mcp = adafruit_mcp9600.MCP9600(i2c, 96, "K", 0)

while True:
    print((mcp.ambient_temperature, mcp.temperature, mcp.delta_temperature))
    time.sleep(1)
