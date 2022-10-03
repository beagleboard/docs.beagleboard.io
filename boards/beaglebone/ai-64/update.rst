.. _bbai64-update:

Update software on BeagleBone AI-64
###################################

Production boards currently ship with the factory-installed 2022-01-14-8GB image. To upgrade from the software image on your BeagleBone AI-64 to the latest, you don't need to completely reflash the board. If you do want to reflash it, visit the flashing instructions on the getting started page.
Factory Image update (without reflashing)…

.. code-block:: bash
   :linenos:

   sudo apt update
   sudo apt install --only-upgrade bb-j721e-evm-firmware generic-sys-mods
   sudo apt upgrade

Update U-Boot:
==============

to ensure only tiboot3.bin is in boot0, the pre-production image we tried to do more in boot0, but failed…

.. code-block:: bash
   :linenos:

   sudo /opt/u-boot/bb-u-boot-beagleboneai64/install-emmc.sh
   sudo /opt/u-boot/bb-u-boot-beagleboneai64/install-microsd.sh
   sudo reboot

Update Kernel and SGX modules:
==============================

.. code-block:: bash
   :linenos:

   sudo apt install bbb.io-kernel-5.10-ti-k3-j721e    

Update xfce:
============

.. code-block:: bash
   :linenos:

   sudo apt install bbb.io-xfce4-desktop

Update ti-edge-ai 8.2 examples
==============================

.. code-block:: bash
   :linenos:

   sudo apt install ti-edgeai-8.2-base ti-vision-apps-8.2 ti-vision-apps-eaik-firmware-8.2

Cleanup:
========

.. code-block:: bash
   :linenos:

   sudo apt autoremove --purge


