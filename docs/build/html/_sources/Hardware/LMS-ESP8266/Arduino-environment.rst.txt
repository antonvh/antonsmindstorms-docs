Arduino
=======

Although `Arduino <https://arduino.cc>`__ is well known from its Atmel
AVR based hardware platform, the Integrated Development Environment
(IDE) is an envirmonment well suited for beginning C developers. The
Arduino IDE has been ported to the ESP8266 and ESP32 platforms. ESP
users can now leverage from libraries supporting a vast amount of
hardware devices such as sensors and displays.

Compared to the deployment of MicroPython on the ESP8266, Arduino will
allow for faster and more complex programs, as the resources that are
used are less demanding. One drawback of using Arduino, is that the
program needs to be compiled and flashed on the ESP before it can run.
The development cycle will take longer

ESP8266 support
---------------

ESP8266 users should install the Arduino support packages for ESP8266 in
the Arduino IDE. This proces is described here:
(`https://arduino-esp8266.readthedocs.io/en/latest/ <https://arduino-esp8266.readthedocs.io/en/latest/>`__).

Installing OTA support
----------------------

The ESP8266 only has a single full bidirectional UART that normaly is
used for flashing firmare. In a development cycle using Arduino, every
iteration in the software makes flashing the firmware neccesary. Because
in our application, the ESP 8266 UART can not be used for flashing new
firmware, as it is connected to a Lego hub, we will need Over The Air
(OTA) programming. The OTA is not present in the bootloader of the
ESP8266. Consequently, each firmware will need to incorporate the OTA
support in order to use it for the next programming cycle.

Debugging Arduino code
----------------------

Through UART1
~~~~~~~~~~~~~

The ESP8266 has two hardware UARTs build in. However, the RX port of the
second UART is shared with pins for driving the Flash memeory, and can
not be used. The transmit pin is mapped on GPIO2 (please be aware that
the inter blue led on the ESP12F module is also mapped on GPIO2,
therefore, driving the LED from your program, prevents using the 2nd TX
UART port. Hook up an FTDI serial to USB concverter with its RX port
connected to GPIO2 and connect the GND of the FTDI to the GND of the esp
board. Below you will find an example of how to use the second UART for
debugging puposes.

::

   Serial1.begin(115200)


   Serial1.println("This is debugging output shown on the second UART on pin GPIO2")

Through RemoteDebug
~~~~~~~~~~~~~~~~~~~

In the MicroPython environment, we use the WebREPL to provide debugging
and interactive prototyping. In the Arduino environment non such thing
exists. However, the github project
(`https://github.com/JoaoLopesF/RemoteDebug <https://github.com/JoaoLopesF/RemoteDebug>`__)
a Wifi-based debugging tool is provided. RemoteDebug allows for remote
debugging through Telnet or through a `web-based debugging
app <https://github.com/JoaoLopesF/RemoteDebugApp>`__.

The RemoteDebug library can be installed from the Library Manager.
Search for remotedebug.
