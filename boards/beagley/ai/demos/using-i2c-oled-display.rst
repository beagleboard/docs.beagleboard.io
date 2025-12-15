.. _beagley-ai-using-i2c-oled-display:

Using I2C OLED Display
#######################

Using I2C on BeagleY-AI is similar to using it on any Raspberry Pi compatible board. 
The image below shows the BeagleY-AI I2C pinout. For more information check `pinout.beagley.ai/pinout/i2c <https://pinout.beagley.ai/pinout/i2c>`_.

.. figure:: ../images/i2c/i2c-pinout.*
    :align: center
    :alt: BeagleY-AI I2C pinout

    BeagleY-AI I2C pinout

OLED (ssd1306) displays
************************

Wiring/connection
==================

Following the I2C pinout shown above let's make the connection of our OLED display with BeagleY-AI. 
Connection for both ``128x64`` and ``128x32`` resolution displays are demonstrated in the images below:

.. figure:: ../images/i2c/oled-128x32.*
    :align: center
    :alt: OLED display 128x32

    OLED display 128x32

.. figure:: ../images/i2c/oled-128x64.*
    :align: center
    :alt: OLED display 128x64

    OLED display 128x64

To check if your OLED is correctly connected to your BeagleY-AI you 
can use ``i2cdetect`` command as shown below.

.. code:: console

    i2cdetect -y -r 1

The above command should show ``3c`` address occupied in the output, which is the default I2C address of our OLED display.

.. code:: console

    debian@BeagleBone:~$ i2cdetect -y -r 1
        0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:                         -- -- -- -- -- -- -- -- 
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- -- 
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
    70: -- -- -- -- -- -- -- --

.. _beagley-ai-ssd1306-using-kernel-driver:

Using kernel driver
===================

To use the kernel driver to drive the SSD1306 oled, we have created an overlay ``/boot/firmware/overlays/k3-am67a-beagley-ai-i2c1-ssd1306.dtbo``. 
To load the overlay you have to add ``fdtoverlays /overlays/k3-am67a-beagley-ai-i2c1-ssd1306.dtbo`` to ``/boot/firmware/extlinux/extlinux.conf`` as shown below.

.. note:: Current overlay is created for 128x64 OLED displays, you can update the overlay to use it for other resolution OLED displays.

.. code:: text

    ...
    ...
    ...

    label microSD (default)
    kernel /Image
    append console=ttyS2,115200n8 root=/dev/mmcblk1p3 ro rootfstype=ext4 resume=/dev/mmcblk1p2 rootwait net.ifnames=0 quiet
    fdtdir /
    fdt /ti/k3-am67a-beagley-ai.dtb
    fdtoverlays /overlays/k3-am67a-beagley-ai-i2c1-ssd1306.dtbo

After rebooting the board you should see ``/dev/fb0`` available.

.. code:: shell

    debian@BeagleBone:~$ ls /dev | grep fb
    fb0

To show random noise on the display you can use ``/dev/urandom`` and feed it to ``/dev/fb0``,

.. code:: shell

    cat /dev/urandom > /dev/fb0

.. figure:: ../images/i2c/oled-urandom-fb0.*
    :align: center
    :alt: Random noise on SSD1306 OLED

    Random noise on SSD1306 OLED

To show blank screen you can use ``/dev/zero`` and feed it to ``/dev/fb0``,

.. code:: shell

    cat /dev/zero > /dev/fb0

.. figure:: ../images/i2c/oled-zero-fb0.*
    :align: center
    :alt: Blank (black/zero) SSD1306 OLED pixels

    Blank (black/zero) SSD1306 OLED pixels

To fill the screen with white pixels you can create a python script 
called ``fill-oled.py`` to create ``data.out`` file and feed it to ``/dev/fb0``,

.. code:: shell

    nano fill-oled.py

Copy paste the below code to ``fill-oled.py``,

.. code:: python

    xsize = 128
    ysize = 64

    with open('data.out', 'wb') as f:
    for y in range(0, ysize):
        for x in range(0, xsize):
        pixel = 255
        f.write((pixel).to_bytes(1, byteorder='little'))

To get the ``data.out`` from ``fill-oled.py`` file execute the command below,

.. code:: shell

    python fill-oled.py

The above command should create a file called ``data.out``. 
To feed ``data.out`` to ``/dev/fb0`` execute the command below,

.. code:: shell

    cat data.out > /dev/fb0

.. figure:: ../images/i2c/oled-rect-fb0.*
    :align: center
    :alt: Fill (white/ones) SSD1306 OLED pixels

    Fill (white/ones) SSD1306 OLED pixels

.. todo:: Add instructions to use OLED for console and printing text via ``/dev/fb0`` interface.

Using Python with smbus2
=========================

For users who prefer a pure Python approach without kernel drivers, you can use the ``smbus2`` library 
to directly control the SSD1306 OLED display. This method provides low-level control and works well 
for custom display logic.

Install smbus2
--------------

First, install the required Python package:

.. code:: console

    pip install smbus2

Python script for SSD1306
-------------------------

Create a Python script to control the OLED display. Below is an example that demonstrates 
basic display initialization and control:

.. code:: python

    import time
    import smbus2 as smbus

    _COMMAND_MODE = 0x80
    _DATA_MODE = 0x40

    _DISPLAY_OFF = 0xAE
    _DISPLAY_ON = 0xAF
    _INVERSE_DISPLAY = 0xA7
    _SET_BRIGHTNESS = 0x81

    BasicFont = [[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                 [0x00, 0x00, 0x5F, 0x00, 0x00, 0x00, 0x00, 0x00],
                 # ... (additional font data)
                ]

    class i2c_display:
        def __init__(self, bus_id=1, address=0x3c):
            self.bus = smbus.SMBus(bus_id)
            self.address = address
            self.width = 128
            self.height = 64
            self.pages = self.height // 8
            self.buffer = [0] * (self.width * self.pages)
            
        def command(self, cmd):
            self.bus.write_byte_data(self.address, _COMMAND_MODE, cmd)
            
        def data(self, data):
            self.bus.write_byte_data(self.address, _DATA_MODE, data)
            
        def init_display(self):
            # Display initialization sequence
            self.command(_DISPLAY_OFF)
            self.command(0x20)  # Set memory addressing mode
            self.command(0x00)  # Horizontal addressing mode
            self.command(0xB0)  # Set page start address
            self.command(0xC8)  # Set COM output scan direction
            self.command(0x00)  # Set low column address
            self.command(0x10)  # Set high column address
            self.command(0x40)  # Set start line address
            self.command(0xA1)  # Set segment re-map
            self.command(0xA6)  # Set normal display
            self.command(0xA8)  # Set multiplex ratio
            self.command(0x3F)  # 1/64 duty
            self.command(0xA4)  # Display all on resume
            self.command(0xD3)  # Set display offset
            self.command(0x00)  # No offset
            self.command(0xD5)  # Set display clock divide ratio
            self.command(0x80)  # Default ratio
            self.command(0xD9)  # Set pre-charge period
            self.command(0xF1)
            self.command(0xDA)  # Set com pins hardware configuration
            self.command(0x12)
            self.command(0xDB)  # Set VCOMH deselect level
            self.command(0x40)
            self.command(0x8D)  # Enable charge pump regulator
            self.command(0x14)
            self.command(_DISPLAY_ON)
            
        def clear(self):
            self.buffer = [0] * (self.width * self.pages)
            
        def show(self):
            # Write buffer to display
            for page in range(self.pages):
                self.command(0xB0 + page)  # Set page address
                self.command(0x00)          # Set lower column address
                self.command(0x10)          # Set higher column address
                
                for col in range(self.width):
                    self.data(self.buffer[page * self.width + col])

    # Example usage
    display = i2c_display(bus_id=1, address=0x3c)
    display.init_display()
    display.clear()
    display.show()

.. note:: 
    This is a simplified example. For a complete font rendering system and advanced features,
    consider using existing Python libraries like ``luma.oled`` or ``Adafruit_SSD1306``.

.. tip::
    The smbus2 approach is particularly useful when you need fine-grained control over the display
    or want to integrate OLED control into existing Python applications without kernel driver dependencies.

Setup ssd1306 linux software
=============================

There are several examples available online to use OLED (ssd1306) displays under linux. 
We are using `ssd1306_linux <https://github.com/armlabs/ssd1306_linux>`_ from ``armlabs`` to 
demonstrate how you can write to an OLED (ssd1306) display.

.. tip:: For detailed usage examples of the library check `Examples section of the Readme <https://github.com/armlabs/ssd1306_linux?tab=readme-ov-file#example>`_.

.. note:: 
    If you tried :ref:`beagley-ai-ssd1306-using-kernel-driver`, you must remove the 
    ``fdtoverlays /overlays/k3-am67a-beagley-ai-i2c1-ssd1306.dtbo`` line from 
    ``/boot/firmware/extlinux/extlinux.conf`` and ``reboot`` your BeagleY-AI board 
    before following the instructions provided below.

Clone the ``ssd1306_linux`` github repository on your BeagleY-AI.

.. code:: console

    git clone https://github.com/armlabs/ssd1306_linux.git

Change directory to your cloned ``ssd1306_linux`` github repository.

.. code:: console

    cd ssd1306_linux

Execute ``make`` to build the binary to control your I2C OLED display.

.. code:: console

    make 

Now, you should have ``ssd1306_bin`` binary file generated in the folder that you can use to easily 
write text on you I2C OLED (ssd1306) display. 

Example1: Hello World!!!!
---------------------------

let's create a script inside the repository (ssd1306 folder) to print ``Hello World!!!!`` on the screen.

.. code:: console

    nano hello-world.sh

Now copy paste the code shown below in your ``hello-world.sh`` file. Update the code if your display resolution 
is not ``128x64``, comment out first line and uncomment second line to choose ``128x32`` display size.

.. code:: bash

    ./ssd1306_bin -n 1 -I 128x64
    #./ssd1306_bin -n 1 -I 128x32


    ./ssd1306_bin -n 1 -c
    ./ssd1306_bin -n 1 -r 0
    ./ssd1306_bin -n 1 -x 1 -y 1
    ./ssd1306_bin -n 1 -l "Hello World!!!!"

Execute the ``hello-world.sh`` script using command below,

.. code:: console

    source hello-world.sh

Executing the command above should print ``Hello World!!!!`` on your OLED display.

.. figure:: ../images/i2c/oled-128x64-hello-world.*
    :align: center
    :alt: Hello World!!!! on 128x64 OLED

    Hello World!!!! on 128x64 OLED

.. figure:: ../images/i2c/oled-128x32-hello-world.*
    :align: center
    :alt: Hello World!!!! on 128x32 OLED

    Hello World!!!! on 128x32 OLED


Understanding the code
~~~~~~~~~~~~~~~~~~~~~~~

.. callout::

    .. code-block:: bash

        ./ssd1306_bin -n 1 -I 128x64 <1>
        #./ssd1306_bin -n 1 -I 128x32 <2>


        ./ssd1306_bin -n 1 -c <3>
        ./ssd1306_bin -n 1 -r 0 <4>
        ./ssd1306_bin -n 1 -x 1 -y 1 <5>
        ./ssd1306_bin -n 1 -l "Hello World!!!!" <6>

    .. annotations::

        <1> Use this command to set OLED display resolution to ``128x64``

        <2> Use this command to set OLED display resolution to ``128x32``

        <3> Clear the display

        <4> Set rotation to ``0/normal``

        <5> Set cursor to location ``x:1 y:1``

        <6> Write ``Hello World!!!!`` to display as line using ``-l`` command.

        Note: We are using ``-n 1`` because our OLED display is connected to ``/dev/i2c-1`` port.

Example2: Date and time
------------------------

To print the date and time on our OLED screen we will be using ``date`` command but you 
can also use ``hwclock`` command to show date and time from onboard RTC. For details on using 
``date`` and ``hwclock`` you can check :ref:`beagley-ai-using-rtc` demo.

Let's create ``date-time.sh`` in the same folder.

.. code:: console

    nano date-time.sh

Now copy paste the code shown below in your ``date-time.sh`` file. Make sure to update the code if your display resolution 
is not ``128x64``, comment out first line and uncomment second line to choose ``128x32`` display size.

.. code:: bash

    ./ssd1306_bin -n 1  -I 128x64
    #./ssd1306_bin -n 1 -I 128x32

    ./ssd1306_bin -n 1 -c
    ./ssd1306_bin -n 1 -r 0

    while :
    do
    ./ssd1306_bin -n 1 -x 1 -y 1
    ./ssd1306_bin -n 1 -f 1 -m "$(date +%Y:%m:%d)\n\n$(date +%H:%M:%S)"
    done

Execute the ``date-time.sh`` script using command below,

.. code:: console

    source date-time.sh

Executing the command above should print ``Date & Time`` on your OLED display.

.. figure:: ../images/i2c/oled-128x64-date-time.*
    :align: center
    :alt: Date & Time on 128x64 OLED

    Date & Time on 128x64 OLED

.. figure:: ../images/i2c/oled-128x32-date-time.*
    :align: center
    :alt: Date & Time on 128x32 OLED

    Date & Time on 128x32 OLED

Understanding the code
~~~~~~~~~~~~~~~~~~~~~~~

.. callout::

    .. code-block:: bash

        ./ssd1306_bin -n 1  -I 128x64 <1>
        #./ssd1306_bin -n 1 -I 128x32 <2>

        ./ssd1306_bin -n 1 -c <3>
        ./ssd1306_bin -n 1 -r 0 <4>

        while : <5>
        do
        ./ssd1306_bin -n 1 -x 1 -y 1 <6>
        ./ssd1306_bin -n 1 -f 1 -m "$(date +%Y:%m:%d)\n\n$(date +%H:%M:%S)" <7>
        sleep 0.2 <8>
        done

    .. annotations::

        <1> Use this command to set OLED display resolution to ``128x64``

        <2> Use this command to set OLED display resolution to ``128x32``

        <3> Clear the display

        <4> Set rotation to ``0/normal``

        <5> Run infinite loop to regularly update screen.
        
        <6> Set cursor to location ``x:1 y:1``

        <7> Write ``Date and Time`` to display on separate lines as message using ``-m`` command.

        <8> Sleep for 200ms (200 milli seconds)

        Note: We are using ``-n 1`` because our OLED display is connected to ``/dev/i2c-1`` port.

.. tip:: Other I2C devices can also be connected and used with BeagleY-AI in the same way shown in this demo.









