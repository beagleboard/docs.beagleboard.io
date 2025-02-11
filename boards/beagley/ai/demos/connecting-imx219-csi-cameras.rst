.. _beagley-ai-imx219-csi-cameras:

.. todo::

   Need to add `gstreamer` and/or `cheese` commands to show how to make use of connected cameras.

Using IMX219 CSI Cameras
############################

To enable an IMX219 CSI camera, modify the following file: `/boot/firmware/extlinux/extlinux.conf`

We can check the available list of Device Tree Overlays as such:

.. code:: console

   debian@BeagleBone:~$ ls /boot/firmware/overlays/ | grep "beagley"
   k3-am67a-beagley-ai-csi0-imx219.dtbo
   k3-am67a-beagley-ai-csi0-ov5640.dtbo
   k3-am67a-beagley-ai-csi1-imx219.dtbo
   k3-am67a-beagley-ai-dsi-rpi-7inch-panel.dtbo
   k3-am67a-beagley-ai-lincolntech-185lcd-panel.dtbo

Using CSI Port 0
**************************************

Then, add the following line to load the IMX219 CSI0 DTBO: 

.. code:: bash

   fdtoverlays /overlays/k3-am67a-beagley-ai-csi0-imx219.dtbo

Your /boot/firmware/extlinux/extlinux.conf file should look something like this:

.. code:: bash

   label microSD (default)
      kernel /Image
      append console=ttyS2,115200n8 root=/dev/mmcblk0p2 ro rootfstype=ext4 rootwait net.ifnames=0
      fdtdir /
      fdt /ti/k3-j722s-beagley-ai.dtb
      fdtoverlays /overlays/k3-am67a-beagley-ai-csi0-imx219.dtbo
      initrd /initrd.img

Now reboot...

.. code:: console

   debian@BeagleBone:~$ ls /dev/ | grep "video"
   video0
   video1
   video2

Using CSI Port 1
*******************


Troubleshooting
*******************

.. code:: console
   
   Found /extlinux/extlinux.conf
   Retrieving file: /extlinux/extlinux.conf
   beagley-ai microSD (extlinux.conf)
      1:      microSD Recovery
      2:      microSD (RPI 7inch panel)
      3:      microSD (lincolntech-185lcd panel)
      4:      microSD (csi0 imx219)
      5:      microSD (csi1 imx219)
      6:      microSD (csi0 ov5640)
      7:      microSD (default)
   Enter choice: 4
      4:      microSD (csi0 imx219)
