`<https://circuitpython.org/>`is a MicroPython spin-off maintained by AdaFruit. It has a vast 
library for all different kinds of sensors and actuators. Originally, CircuitPython only ran on boards using a native USB port. 
These devices monifests themselves as a mass storgae device on which python programs can be dropped. 
Lately, CircuitPython brings the so-called 
`Wi-Fi Workslow <https://learn.adafruit.com/circuitpython-with-esp32-quick-start/setting-up-web-workflow>`__ 
to boards lacking the native USB port, such as our LMS-ESP32.


Fashing

 - Download .bin image from `<https://circuitpython.org/board/espressif_esp32_eye/>`__
 - Flash this image to you board using: `<https://adafruit.github.io/Adafruit_WebSerial_ESPTool/>`__
 - Reset your board
 - Connect serial terminal or e.g. Thonny (using CiurcuitPython)
 - setup `Wifi workflow <https://learn.adafruit.com/circuitpython-with-esp32-quick-start/setting-up-web-workflow>`__
