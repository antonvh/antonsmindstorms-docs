`ulab`-library
===============

`ulab` is a numpy-like array manipulation library for MicroPython and CircuitPython. The module is written in native C, 
defines compact containers (ndarrays) for numerical data of one to four dimensions, and is fast. `ulab`` uses the extra 4MByte pf PSRAM of the ESP32-wrover very effienctly and can thus
be used for handling larger arrays. 8-, and 16-bit signed and unsigned integer dtypes, as well as float, and, optionally,  
complex are supported. The float implementation of micropython (32-bit float, or 64-bit double) is automatically detected and handled.
Furthermore, some `scipy` library functions are also incorportaed in the `ulab` library.
See `micropython-ulab.readthedocs.io <https://micropython-ulab.readthedocs.io/>`__ for more information.

Audio application of ulab
-------------------------

The ESP32 support with the I2S a direct way for handling audio streams. 

In the code snippets below, the signal of an I2S microphone is read in an array.

.. code:: python
    
    from machine import I2S, Pin
    from ulab import numpy as np
    from ulab import scipy as spy
    import time
    from uartremote import *


    SCK_PIN=33
    SD_PIN=32
    WS_PIN=27

    I2S_ID=0

    WAV_SAMPLE_SIZE_IN_BITS = 16
    FORMAT = I2S.MONO
    SAMPLE_RATE_IN_HZ = 5000 # up to 2500Hz, enough for voice
    BUFFER_LENGTH_IN_BYTES = 4192

    audio_in=I2S(I2S_ID,
                sck=Pin(SCK_PIN),
                ws=Pin(WS_PIN),
                sd=Pin(SD_PIN),
                mode=I2S.RX,bits=16,
                format=FORMAT,
                rate=SAMPLE_RATE_IN_HZ,
                ibuf=BUFFER_LENGTH_IN_BYTES)


    def hamming(N):
        # hamming filter for removing sharp artefacts of finite sampling signal
        n=np.linspace(0,N,num=N)
        w=0.54-0.46*np.cos(2*3.1415*n/N)
        return w


    # initialize 
    #neop=neopixel.NeoPixel(Pin(21),64)

    def level(l):
        for i in range(8):
            if i<l:
                neop[i]=(5*i,5*(7-i),0)
            else:
                neop[i]=(0,0,0)
            neop.write()


    def led_xy(x,y,col):
        iy=y%8
        neop[iy*8+x]=col

    def led_power(q):
        m=3000 #max(q)
        f=m/8
        for i,qi in enumerate(q):
            l=qi
            if l>m:
                l=m
            iy=int(l/f)
            for ii in range(iy):
                led_xy(i,ii,(30,0,0))
            for ii in range(iy,8):
                led_xy(i,ii,(0,0,0))
        neop.write()
        
        


    mic_samples = bytearray(256)
    mic_samples_mv = memoryview(mic_samples) # efficient pointer to original array

    # we use efficient ulab functions (written in C) 

    def spec():
        num_bytes_read_from_mic = audio_in.readinto(mic_samples_mv)
        # interpret raw buffer to signed int16 array
        q=np.frombuffer(mic_samples,dtype=np.int16)
        # multiply each array elemelt with hamming windows
        q=q*hamming(128)
        # perform FFT and take abolute value of complex numbers
        z=spy.signal.spectrogram(q)
        # reshape only positive frequency elements in n bins
        zs=z[64:64+60].reshape((5,12))
        # calculate sum of each bin
        sq=np.sum(zs,axis=1)
        return tuple(sq)

    u=UartRemote(port=1,esp32_tx=26,esp32_rx=27)

    u.add_command(spec,'5f')

    u.loop()


LVGL library
============

A micrpython port of the LVGL library is incorporated in the firmware. This allows to program GUI's on TFT screens very easily from within the MicroPython environment.
