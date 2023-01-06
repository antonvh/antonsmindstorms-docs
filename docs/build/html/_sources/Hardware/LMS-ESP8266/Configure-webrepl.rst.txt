The MicroPython WebREPL
=======================

This is just the short guide. There is a full guide here:
`https://learn.adafruit.com/micropython-basics-esp8266-webrepl/access-webrepl <https://learn.adafruit.com/micropython-basics-esp8266-webrepl/access-webrepl>`__

Configuring for access point mode
---------------------------------

1. Open *regular* REPL connection to your ESP over the serial port. See
   the last step of `Flashing the esp <Flashing-esp-i2c-board>`__ for
   details.
2. Paste this (no paste mode needed) to have the esp board create a WiFi
   access point you can connect to.

::

   import webrepl_setup

3. See `Connecting via WebREPL <Connecting-via-webrepl>`__ for details
   on how to connect.

Configuring for connection to your WLAN
---------------------------------------

Optional: Connect to your WLAN. After you have set up the WebREPL as
described above, you can configure the esp to connect to your LAN. This
is how:

1. Connect to a REPL and paste the code below, but replace ``ssid`` and
   ``password`` with the right text for your WLAN.

::

   import network
   wlan = network.WLAN(network.STA_IF)
   wlan.active(True)
   wlan.connect('ssid', 'password')

2. Find your ESP on the network via your router. On my router it showed
   up as 'ESP-99731D'
3. See `Connecting via WebREPL <Connecting-via-webrepl>`__ for details
   on how to connect.
