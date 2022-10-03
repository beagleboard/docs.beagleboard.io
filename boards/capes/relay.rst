.. _bone-cape-relay:

BeagleBoard.org BeagleBone Relay Cape
#####################################

Relay Cape, as the name suggests, is a simple Cape with a relay on it.
It contains four relays, each of which can be operated independently from the BeagleBone.

.. image:: images/BeagleBoneRelayCapeA2-400x274.png
   :align: center

* `Order page <https://beagleboard.org/capes#relay>`_
* `Schematic <https://git.beagleboard.org/beagleboard/capes/-/tree/master/beaglebone/Relay>`_

.. note:: 
    The following describes how to use the device tree overlay under development.
    The description may not be suitable for those using older firmware.

Installation
************

No special configuration is required. When you plug Cape into your BeagleBoard, 
it is automatically recognized by the Cape Universal function.

You can check to see if Relay Cape is recognized with the following command.

.. code-block::

    ls /proc/device-tree/chosen/overlay

A list of currently loaded device tree overlays is displayed here. 
If you see `BBORG_RELAY-00A2.kernel` in this list, it has been loaded correctly.

If it is not loaded correctly, you can also load it directly 
by adding the following to the U-Boot options 
(which can be reflected by changing /boot/uEnv.txt).

.. code-block::

    uboot_overlay_addr0=BBORG_RELAY-00A2.dtbo


Usage
******

.. code-block::

    ls /sys/class/leds

The directory "relay*" exists in the following directory.
The LEDs can be controlled by modifying the files in this directory.

.. code-block::

    echo 1 > relay1/brightness

This allows you to adjust the brightness; 
entering 1 for brightness turns it ON, and entering 0 for OFF.

The four relays can be changed individually 
by changing the number after "relay.
