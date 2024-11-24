Getting started with your new LMS-ESP32v2 board
===============================================

.. image:: ../images/LMS-ESP32v2_with_cable.jpg
  :alt: LMS_esp32v2 Photo
  :width: 400


Firmware for the LMS-ESP32v2
----------------------------

Your board comes flashed with the last Micropython 1.24. 
With our online firmware flasher on https://firmware.antonsmindstorms.com,
you can flash it with other firmware, for instance, if you want to connect gamepads. Only works in Google Chrome or MS Edge.


Connecting to the board
-----------------------

The easiest way to edit files on the board is a program called `Thonny <https://thonny.org/>`__. 
Just connect the board through USB. On Chromebooks you can use the online IDE `Viper IDE <https://viper-ide.org/>`__. Connect with 
USB/Serial and look for a port indctaing CH340. 
If you want basic access to the serial port of the board, you can use this `online Serial Terminal <https://googlechromelabs.github.io/serial-terminal/>`__.

Configuring a WIFI access point
-------------------------------
You can access the board wirelessly if you configure a WiFi access point and use Micropython.

Upload this `boot.py <https://github.com/antonvh/flash-esp/blob/master/boot.py>`__
to the board. It creates a WiFi Access point called ESP-AP. The password is
``micropythoN``. When you're connected, you can use a
`WebREPL <Connecting-via-webrepl>`__ to program your board. Just press
enter when it asks for a password. There is none.

