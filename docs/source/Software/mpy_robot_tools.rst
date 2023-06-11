#############################
mpy_robot_tools documentation
#############################

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


Contributing
============

Please fork and help out this project by adding documentation. Could 
be docstrings, README, or tutorials.


Overview of the mpy_robot_tools modules
=======================================


mpy_robot_tools.bt module
---------------------------

-  BLEHandler() - Base Bluetooth Low Energy handler
-  UARTCentral() - Connects to UARTPeripheral and implements read() and
   write() like serial uart.
-  UARTPeripheral() - Waits for a connection from UARTCentral and
   implements read() and write() like serial uart.

By default the UART objects are buffered. They will remember everything
ever written to them and you should flush their buffer with
``_ = read()`` to start clean. For remote control and state
communication the buffer gets in the way. You just want to read the most
recent state when it arrives. In that case initialize with
``additive_buffer=False`` Example:

::

   # Create link to the snake head, and advertise self as tail.
   head_link = UARTPeripheral(name="tail", additive_buffer=False)

If you have multiple Bluetooth objects, like a remote control, a
serialtalk and a plain UART, you need to pass a single BLEHandler to all
of them:

::

   from projects.mpy_robot_tools.bt import BLEHandler, UARTCentral
   from projects.mpy_robot_tools.rc import RCReceiver, R_STICK_VER, L_STICK_HOR, SETTING2

   ble = BLEHandler()
   seg_1_link = UARTCentral(ble_handler=ble)
   seg_2_link = UARTCentral(ble_handler=ble)
   rcv = RCReceiver(name="snake", ble_handler=ble)


-  Use the `MINDSTORMS Ble RC Anroid
   app <https://play.google.com/store/apps/details?id=com.antonsmindstorms.mindstormsrc>`__
   or another Smart Hub to `remote control your
   robot <https://gist.github.com/antonvh/1f1d9c563268b4a8e9e1d7297e62ad53>`__
   or `Hot
   Rod <https://gist.github.com/antonvh/88548d95e771043662f038de451e28f2>`__

-  Example

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

.. automodule:: mpy_robot_tools.bt
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