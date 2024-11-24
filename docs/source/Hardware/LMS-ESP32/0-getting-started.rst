Getting started with your new LMS-ESP32 board
=============================================

.. image:: ../images/lms-esp32.jpg
  :alt: LMS_esp32 Pinout
  :width: 400


Firmware for the LMS-ESP32
--------------------------

Your board comes flashed with the last Micropython 1.19. 
With our online firmware flasher on https://firmware.antonsmindstorms.com,
you can flash it with other firmware, for instance, if you want to connect gamepads. Only works in Google Chrome or MS Edge.


Connecting to the board
-----------------------

The easiest way to edit files on the board is a program called `Thonny <https://thonny.org/>`__. 
Just connect the board through USB. On Chromebooks you can use a USB serial terminal, 
like `serial terminal <https://googlechromelabs.github.io/serial-terminal/>`__. Connect with 
baudrate 115200. Transferring files will be hard, though.


Configuring a WIFI access point
-------------------------------
You can access the board wirelessly if you configure a WiFi access point and use Micropython.

Upload this `boot.py <https://github.com/antonvh/flash-esp/blob/master/boot.py>`__
to the board. It creates a WiFi Access point called ESP-AP. The password is
``micropythoN``. When you're connected, you can use a
`WebREPL <Connecting-via-webrepl>`__ to program your board. Just press
enter when it asks for a password. There is none.

