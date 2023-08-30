#############################
mpy_robot_tools documentation
#############################

About mpy_robot_tools: a set MicroPython robotics libraries
===========================================================

When programming robots with sensors, you want to focus on the behaviors, not the interfaces.
This set of libraries contains abstractions for interfaces like Bluetooth Low Energy (BLE), Huskylens, UART communication, synchronized motor arrays, and LED lights.

With this set, you can easily create a Bluetooth-controlled robot with multiple robotic hubs, communicating and synchronizing their motors. They can run lights, read camera data, and read Arduino sensors.

Libraries will work MicroPython devices like OpenMV, ESP32, LEGO Robot Inventor, and LEGO SPIKE Prime. 

Installation
============

SPIKE Prime / Mindstorms Robot Inventor Installation
----------------------------------------------------

1. Copy the code from the `install
   script <https://github.com/antonvh/mpy-robot-tools/blob/master/Installer/install_mpy_robot_tools.py>`__ (`click the Copy raw
   contents
   button <https://github.blog/changelog/2021-09-20-quickly-copy-the-contents-of-a-file-to-the-clipboard/>`__)
   to an empty Python project in the LEGO MINDSTORMS or LEGO SPIKE
   program.
2. Then run it once. It will take additional time to transfer to the Hub
   please use patience.
3. Start using the modules.

EV3 Installation
----------------

Create a new VS Code EV3 project with the MINDSTORMS extension. Then git clone this repository
in the new project directory.

OpenMV / ESP32 Installation
---------------------------

Copy the files to your device using Thonny or the USB drive feature. Then import them like any other Python file.

FAQ
----

... The Spike/Mindstorm app asks for a firmware update after installing
   The LEGO software has a bug with a memory leak. The drive becomes filled up,
   and you lose disk space. To fix it, connect your hub via USB and go here:
   https://dfu.pybricks.com/fix-update/

... How do I uninstall? Should I uninstall?
   There is no reason to uninstall the libraries. Unless you call them, they do
   nothing. If you need disk space, you can delete the files with a file
   manager like Thonny or factory reset the hub through the LEGO software.

Getting Started
===============

The easiest way to get started is to copy and tweak one of the `mpy_robot_tools example projects <https://github.com/antonvh/mpy-robot-tools/tree/master/Example%20projects>`__.


Contributing
============

Please fork and help out this project by adding documentation. Could 
be docstrings, README, or tutorials.


Overview of the mpy_robot_tools modules
=======================================


mpy_robot_tools.bt module
---------------------------

The bt.py module abstracts low-level BLE characteristics and services. The way BLE works is well documented at https://learn.adafruit.com/introduction-to-bluetooth-low-energy/gatt. You can start communication with a UARTCentral on one side and a UART Peripheral on the other. The UARTCentral initiates the communication, and the peripheral waits for a connection, like a server. 

The nRF connect smartphone app is convenient to test and debug Bluetooth.

Remote control
^^^^^^^^^^^^^^

RCReceiver and RCTransmitter are subclasses of the UARTPeripheral and UARTCentral, respectively. They receive and transmit a short burst of bytes, enough to pass the state of any custom remote control device. You can build your own Micropython RC transmitter with any BLE Micropython device. You can also use the `MINDSTORMS Ble RC Anroid app <https://play.google.com/store/apps/details?id=com.antonsmindstorms.mindstormsrc>`__.

.. code:: python

   # RCReceiver() - Receives RC commands from the android app or RCTransmitter class.
   rcv = RCReceiver(name="snake")
   while rcv.is_connected():
      speed, turn, delay_setting = rcv.controller_state(R_STICK_VER, L_STICK_HOR, SETTING2)


.. code:: python

   # RCTransmitter() - Connects to an RCReceiver and transmits the state of 9 gamepad-like controls.
   remote_control = RCTransmitter()
   remote_control.connect(name="snake")
   remote_control.set_stick(L_STICK_HOR, steer_angle )
   remote_control.set_stick(R_STICK_VER, forward)
   remote_control.transmit()

Buffering
^^^^^^^^^

By default, the UART objects are buffered. They will remember everything written to them, and you should flush their buffer with ``_ = read()`` to start clean. For remote control and state communication, the buffer gets in the way. You want to read the most recent state when it arrives. In that case initialize with ``additive_buffer=False`` 

Example:
.. code-block:: python

   # Code for a snake tail segment, waiting for connections from the head.
   # Creates a link to the snake head and advertises self as "tail".
   # Additive buffer is disabled, since we are only interested 
   # in the most recent state information
   head_link = UARTPeripheral(name="tail", additive_buffer=False)

Complex networks
^^^^^^^^^^^^^^^^

The UARTCentral, and UARTPeripheral classes instantiate a BLEHandler automatically. You can pass your own handler for more complex BLE network setups. If you have multiple Bluetooth objects, like remote control, a
Serialtalk and a plain UART, you need to pass a single BLEHandler to all of them:

.. code-block:: python

   from projects.mpy_robot_tools.bt import BLEHandler, UARTCentral
   from projects.mpy_robot_tools.rc import RCReceiver, R_STICK_VER, L_STICK_HOR, SETTING2

   ble = BLEHandler()
   seg_1_link = UARTCentral(ble_handler=ble)
   seg_2_link = UARTCentral(ble_handler=ble)
   rcv = RCReceiver(name="snake", ble_handler=ble)


.. automodule:: mpy_robot_tools.bt
   :members:
   :undoc-members:
   :show-inheritance:


mpy\_robot\_tools.sen0539 module
--------------------------------

.. automodule:: mpy_robot_tools.sen0539
   :members:
   :undoc-members:
   :show-inheritance:

mpy\_robot\_tools.ctrl\_plus module
-----------------------------------

-  SmartHub() - Connects to a Technic smart hub and is able to control
   connected devices and read the states of the IMU and connected
   motors.

.. automodule:: mpy_robot_tools.ctrl_plus
   :members:
   :undoc-members:
   :show-inheritance:

mpy\_robot\_tools.helpers module
--------------------------------

.. automodule:: mpy_robot_tools.helpers
   :members:
   :undoc-members:
   :show-inheritance:


mpy\_robot\_tools.light module
------------------------------

.. automodule:: mpy_robot_tools.light
   :members:
   :undoc-members:
   :show-inheritance:

mpy\_robot\_tools.motor\_sync module
------------------------------------

.. automodule:: mpy_robot_tools.motor_sync
   :members:
   :undoc-members:
   :show-inheritance:

mpy\_robot\_tools.np\_animation module
--------------------------------------

.. automodule:: mpy_robot_tools.np_animation
   :members:
   :undoc-members:
   :show-inheritance:

mpy\_robot\_tools.pybricks module
---------------------------------

.. automodule:: mpy_robot_tools.pybricks
   :members:
   :undoc-members:
   :show-inheritance:

mpy\_robot\_tools.rc module
---------------------------

Legacy module for compatibility reasons. Don't use.

mpy\_robot\_tools.servo module
------------------------------

.. automodule:: mpy_robot_tools.servo
   :members:
   :undoc-members:
   :show-inheritance:

mpy\_robot\_tools.pyhuskylens module
------------------------------------


-  HuskyLens() - Connect to
   Huskylens over a
   serial port and get Image AI data.


.. automodule:: pyhuskylens
   :members:
   :undoc-members:
   :show-inheritance:

Stubs
=====

For programming convenience in VS Code I would love to collect stubs of
all LEGO hub libraries. I’ve been looking into micropython-stubber but
it didn’t work for me.

mpy\_robot\_tools.hub\_stub module
----------------------------------

.. automodule:: mpy_robot_tools.hub_stub
   :members:
   :undoc-members:
   :show-inheritance: