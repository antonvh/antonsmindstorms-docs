############################################
Welcome to Anton's Mindstorms documentation!
############################################


Software libraries
==================

mpy_robot_tools
---------------

Mpy_robot_tools is the Swiss army knife for programming animated, interactive robots.
It has an installer for LEGO SPIKE Prime and LEGO MINDSTORMS.

The library works on esp32, SPIKE, and mindstorms EV3,  
or any robot microcontroller that has micropython.

:doc:`/Software/mpy_robot_tools`

SerialTalk
__________

Serial Remote Procedure call works over UART, sockets, and BT RFComm. 
In fact, it works over any serial protocol. The protocol is the same as
UartRemote, but it is generalized to work over more channels than just UART.
The protocol is compatible.

:doc:`/Software/SerialTalk/docs/index`

UartRemote
----------

This is a library
for robust, near real-time communication between two UART devices. 
It has been superseded by serialtalk.
We developed it with LEGO EV3, SPIKE Prime, and other MicroPython (ESP)
modules. 

:doc:`/Software/UartRemote/index`

Hardware documentation
======================

Find all pinouts and board layouts for the expansion boards, like LMS-ESP32, from antonsmindstorms.com.

:doc:`/Hardware/index`

Firmware documentation
======================

For our ESP32 boards, we have compiled powerful firmware. 
You can install the firmware via https://firmware.antonsmindstorms.com
You have the choice of:

- :doc:`a MicroPython firmware with ulab and LVGL </Firmware/Micropython/micropython>`

- :doc:`an Arduino version that connects to Bluetooth gamepads. </Firmware/BluePad32/bluepad32>`


.. toctree::
   :hidden:
   :maxdepth: 2
   
   Software/index
   Hardware/index
   Firmware/index

   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
