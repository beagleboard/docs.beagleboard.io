.. _capes:

Capes
#####

.. note::
   This page is under development.

Capes are add-on boards for BeagleBone or PocketBeagle families of boards.  Using a Cape add-on board, you can easily add
sensors, communication peripherals, and more.

Please visit `BeagleBoard.org - Cape <https://beagleboard.org/capes>`_ for the list of currently available Cape add-on boards.

In the BeagleBone board family, there are many variants, such as :ref:`beagleboneblack-home`, :ref:`beaglebone-ai-home`,
:ref:`bbai64-home` and compatibles such as `SeeedStudio BeagleBone Green <https://beagleboard.org/green>`_,
`SeeedStudio BeagleBone Green Wireless <https://beagleboard.org/green-wireless>`_, `SeeedStudio BeagleBone Green Gateway
<https://wiki.seeedstudio.com/BeagleBone-Green-Gateway/>`_ and more.

The :ref:`beaglebone-cape-interface-spec` enables a common set of device tree overlays and software to be utilized
on each of these different BeagleBone boards.

Each hardware has different internal pin assignments 
and the number of peripherals in the SoC, but the device tree overlay absorbs these differences.

The user of the Cape add-on boards are essentially able to use it 
across the corresponding Boards without changing any code at all.

Find the instructions below on using each cape:

* :ref:`bone-cape-relay`

.. toctree::
   :maxdepth: 2
   :hidden:

   /boards/capes/cape-interface-spec
   /boards/capes/relay

