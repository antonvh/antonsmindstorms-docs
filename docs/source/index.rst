############################################
Welcome to Anton's Mindstorms documentation!
############################################


Software libraries
==================

Software is here :doc:`/Software/index`



Huskylens
---------

-  HuskyLens() - `Connect to
   Huskylens <https://github.com/antonvh/LEGO-HuskyLenslib>`__ over a
   serial port and get Image AI data.
-  clamp_int(n) - returns an an int between -100 and 100, clamping
   higher or lower numbers.



Remote UART library: uartremote.py
----------------------------------

NOTE: This is temporary. In the future I hope to replace with
`serialtalk <https://github.com/antonvh/SerialTalk>`__. It’s the same
idea but it also works over bluetooth and websockets. This is a library
for robust, near real-time communication between two UART devices. We
developed it with LEGO EV3, SPIKE Prime and other MicroPython (ESP)
modules. The library has the following properties: - It is fast enough
to read sensor data at 30-50Hz. - It is fully symmetrical, so master and
slave can have the same import. - It includes a RAW REPL mode to upload
code to a slave module. This means you can develop code for both modules
in one file. - It is implemented in MicroPython and Arduino/C code. With
arduino code, much higher sensor reading speeds are possible, but
flashing is a bit less user friendly. - The library has a command loop
to wait and listen for calls. That loop is customizable and non-blocking
so you can add your own code to it. - The C-struct-like encoding is
included in the payload, so the other side always knows how to decode
it.

Read more in the `README file of that
library. <Submodules/UartRemote/README.md>`__





Table of Contents
=============================

.. toctree::
   :maxdepth: 2

   Software/index
   Hardware/index
   Firmware/index

   
Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
