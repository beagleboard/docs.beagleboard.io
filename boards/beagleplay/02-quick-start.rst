.. _beagleplay-quick-start:

Quick Start Guide
####################

What's included in the box?
****************************

When you purchase a brand new BeaglePlay, In the box you'll get:

1. BeaglePlay board
2. One (1) sub-GHz antenna
3. Three (3) 2.4GHz/5GHz antennas
4. Plastic standoff hardware
5. Quick-start card

.. image:: images/product-pictures/45fontall.*
    :width: 1400
    :align: center
    :alt: BeaglePlay box contents

Attaching antennas
******************

You can watch this video to see how to attach the attennas.

.. only:: latex
    
    .. image:: images/attach-antennas.*
        :alt: YouTube video of BeaglePlay antenna connection
        :width: 1280
        :target: https://youtu.be/8zeIVd-JRc0

.. only:: html

    .. raw:: html

        <iframe style="display: block; margin: auto;" width="1280" height="720" style="align:center" 
        src="https://www.youtube.com/embed/8zeIVd-JRc0" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        allowfullscreen>
        </iframe>

Tethering to PC
****************

.. tip:: 
    Checkout :ref:`beagleboard-getting-started` for,

    1. Updating to latest software.
    2. Power and Boot.
    3. Network connection.
    4. Browsing to your Beagle.
    5. Troubleshooting.

For tethering to your PC you'll need a USB-C data cable.

.. figure:: images/tethered-connection.jpg
    :width: 1400
    :align: center
    :alt: Tethering BeaglePlay to PC

    Tethering BeaglePlay to PC

Access VSCode
****************

Once connected, you can browse to `192.168.7.2:3000 <http://192.168.7.2:3000>`_ to access the VSCode IDE 
to browse documents and start programming your BeaglePlay!

.. note::

   You may get a warning about an invalid or self-signed certificate. This is a limitation of
   not having a public URL for your board. If you have any questions about this, please as on
   https://forum.beagleboard.org/tag/play.

.. figure:: images/vscode.png
    :width: 1400
    :align: center
    :alt: BeaglePlay VSCode IDE (192.168.7.2:3000)

    BeaglePlay VSCode IDE (192.168.7.2:3000)

.. _beagleplay-demos-and-tutorials:

Demos and Tutorials
*******************

* :ref:`beagleplay-serial-console`
* :ref:`beagleplay-connect-wifi`
* :ref:`beagleplay-qwiic`
* :ref:`beagleplay-grove`
* :ref:`beagleplay-mikrobus`
* :ref:`beagleplay-oldi`
* :ref:`beagleplay-csi`
* :ref:`beagleplay-zephyr-development`
* :ref:`play-kernel-development`
* :ref:`play-understanding-boot`
