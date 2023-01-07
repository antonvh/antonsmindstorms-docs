`ulab`-library
===============

`ulab` is a numpy-like array manipulation library for MicroPython and CircuitPython. The module is written in native C, 
defines compact containers (ndarrays) for numerical data of one to four dimensions, and is fast. `ulab`` uses the extra 4MByte pf PSRAM of the ESP32-wrover very effienctly and can thus
be used for handling larger arrays. 8-, and 16-bit signed and unsigned integer dtypes, as well as float, and, optionally,  
complex are supported. The float implementation of micropython (32-bit float, or 64-bit double) is automatically detected and handled.
Furthermore, some `scipy` library functions are also incorportaed in the `ulab` library.
See `micropython-ulab Github page <https://github.com/v923z/micropython-ulab>`__ for more information.

Audio application of ulab
-------------------------

The ESP32 support with the I2S a direct way for handling audio streams. 

LVGL library
============

A micrpython port of the LVGL library is incorporated in the firmware. This allows to program GUI's on TFT screens very easily from within the MicroPython environment.
