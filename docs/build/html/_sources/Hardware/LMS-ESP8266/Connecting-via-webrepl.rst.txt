WebREPL
=======

Your WiFi ESP board came flashed and configured with a WebREPL. This
means you can type micropython code and upload files (e.g. main.py and
boot.py) to your board, pretty much hassle free from any modern laptop
or pc. No FTDI cable needed.

Connecting to the WebREPL
-------------------------

1. Download the WebREPL html file here:
   `https://github.com/micropython/webrepl/archive/master.zip <https://github.com/micropython/webrepl/archive/master.zip>`__
2. By default your WiFi ESP generates a WiFi access point. Find it in
   your wifi networks. (If you have `connected your esp-wifi board to
   your wireless lan <Configure-webrepl>`__, find it's name or ip on
   your router and skip to step 4. Replace the ip number in the topleft
   window with the ip of your wifi-esp board.)
3. Change your wifi access point to that of the esp. The password in
   ``micropythoN`` |wifi setup|
4. Open the html file in the zip file you downloaded in step 1.
5. Just press the connect button. The ip address is fine.
6. The password is just ``python`` by default.

.. |wifi setup| image:: images/Wifi-connect.png
