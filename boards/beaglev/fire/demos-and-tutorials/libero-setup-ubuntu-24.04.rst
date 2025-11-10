.. _beglev-fire-libero-setup-ubuntu:

Libero Setup - Ubuntu 24.04
############################

This guide is intended to help users to setup the libero design tools on a fresh ubuntu 24.04.1 installation. 
Similar steps are followed to what is provided the the :ref:`beaglev-fire-mchp-fpga-2024-2-and-older-tools-installation-guide`, 
:ref:`beaglev-fire-mchp-fpga-2025-1-tools-installation-guide`, and that
`provided by Penguin <https://wiki.gentoo.org/wiki/User:Penguin/Installing_Microchip_FPGA_Tools#Gentoo_Specific_Libero_Fixes>`_ 
a member of the BeagleV-Fire Community.

At the time of writing this guide versions of Libero SOC web installer v2024.2 and SoftConsole v2022.2 were available. 
It is possible that other versions of the installation process will work by substituting the appropriate version
numbers but this has not been tested.

Steps
******

Download Tools
===============

- Download the Libero SOC web installer from `microchip website - libero-software-later-versions <https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/fpga/libero-software-later-versions>`_
- Download SoftConsole from `microchip website - softconsole <https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/soc-fpga/softconsole>`_

Prepare Install Files
=====================

Move and prepare the install tools in an isolated location

.. code-block:: bash

   mkdir -p ~/Documents/MicrochipInstallers
   cd ~/Documents/MicrochipInstallers
   mv ~/Downloads/Libero_SoC_v2024.2_Web_lin.zip .
   mv ~/Downloads/Microchip-SoftConsole-v2022.2-RISC-V-747-linux-x64-installer.run .
   unzip Libero_SoC_v2024.2_Web_lin.zip
   chmod +x Microchip-SoftConsole-v2022.2-RISC-V-747-linux-x64-installer.run

L 
The default installation of Libero tries to pop things in a root only location. We are going to move 
things to a unified location in the user home directory. For now just create the storage folder for the next step.

.. code-block:: bash

   mkdir -p ~/Microchip


Install the Tools
=================

Start by installing Libero SOC. Don't forget to update the paths for the install directory and common 
directory to be in ``~/Microchip`` We will be installing all of the tools.

.. code-block:: bash

   ~/Documents/MicrochipInstallers/launch_installer.sh


hold off on the post install script for the moment. It will be handled in a later step.

After Libero is completed run the installer for SoftConsole.

.. code-block:: bash
 
   ~/Documents/MicrochipInstallers/Microchip-SoftConsole-v2022.2-RISC-V-747-linux-x64-installer.run


Getting a Libero License
=========================
To use Libero you will need to get a license from Microchip. Follow the steps below to get a free 1 year floating license.

- Visit `Microchip's fpga license page <https://www.microchipdirect.com/fpga-software-products>`_.
- Choose ``Libero Silver 1Yr Floating License for Windows/Linux Server`` from the list.
- Enter your MAC address and click register.
- Download your new license from your email once it arrives.
- Extract the license to ``~/Microchip/license``.
- Update the hostname field on line 1 marked by ``<put.hostname.here>`` with ``localhost``

Post Install
=============

Updated Dependencies Install Script
------------------------------------

Libero comes packaged with a script to install a few tools after the initial installation. Some of these 
have been renamed for Ubuntu 24.04. Run The following commands instead.

.. code-block:: bash

   sudo dpkg --add-architecture i386
   sudo apt update 
   sudo apt install -y libc6:i386 \
                     libdrm2:i386 \
                     libexpat1:i386 \
                     libfontconfig1:i386 \
                     libfreetype6:i386 \
                     libglapi-mesa:i386 \
                     libglib2.0-0t64:i386 \
                     libgl1:i386 \
                     libice6:i386 \
                     libsm6:i386 \L 
                     libuuid1:i386 \
                     libx11-6:i386 \
                     libx11-xcb1:i386 \
                     libxau6:i386 \
                     libxcb-dri2-0:i386 \
                     libxcb-glx0:i386 \
                     libxcb1:i386 \
                     libxdamage1:i386 \
                     libxext6:i386 \
                     libxfixes3:i386 \
                     libxrender1:i386 \
                     libxxf86vm1:i386 \
                     zlib1g:i386 \
                     libflac12t64 \
                     libpcre3 \
                     libxcb-xinerama0 \
                     libxcb-xinput0 \
                     xfonts-intl-asian \
                     xfonts-intl-chinese \
                     xfonts-intl-chinese-big \
                     xfonts-intl-japanese \
                     xfonts-intl-japanese-big \
                     ksh \
                     libxft2:i386 \
                     libgtk2.0-0t64:i386 \
                     libcanberra-gtk-module:i386 \
                     libfreetype-dev \
                     libharfbuzz-dev

Remove libstdc++ References
----------------------------

Trying to run libero directly at this point will yield an error similar to this:

.. code-block:: bash

   /home/lucien/Microchip/Libero_SoC_v2024.2/Libero/bin64/libero_bin: /home/lucien/Microchip/Libero_SoC_v2024.2/Libero/lib64/rhel/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /usr/lib/x86_64-linux-gnu/libicuuc.so.74)

This is expected because a packaged version of stdlibc++ is being used that was shipped with the installation. 
We need to delete all of the local versions so the system libs can be used instead.

.. code-block:: bash

   find ~/Microchip/Libero_SoC_v2024.2 -name "libstdc++.so.6" -type f -delete

Create tmp dir
--------------

Running the license server will cause issues with a folder that cant be created because of permission issues.

.. code-block:: bash

   12:46:59 (lmgrd) Can't make directory /usr/tmp/.flexlm, errno: 2(No such file or directory)

It is best to pre-create it with the appropriate permissions for use.

.. code-block:: bash

   sudo mkdir /usr/tmp
   sudo chown $USER:$USER /usr/tmp

Missing lib
-------------

This step is only required if you are using older versions of the license tool i.e. the ones packaged with 
versions of liber older than 2024.2/ Licensing tools v11.19.6.0. This guide is using the bundled tools 
with a version new enough that this shouldnt be an issue.

Older versions of the license tools depend on the `lsb` and `lsb-core` packages. These have been phased 
out in Ubuntu 24.04. We now end up with a missing link which causes a strange `no such file or directory` 
error when launching the license daemon. We need to create an equivalent link for this. I suggest:

.. code-block:: bash

   sudo ln -s /lib64/ld-linux-x86-64.so.2 /lib/ld-lsb-x86-64.so.3

Setup Script
-------------

This setup script is based on the one provided by Beagle. Is has been updated to use the versions of Libero 
suggested in this guide and the licensing tools that are provided with the installation.

.. code-block:: bash

   #!/bin/bash

   #===============================================================================
   # Edit the following section with the location where the following tools are
   # installed:
   #   - SoftConsole (SC_INSTALL_DIR)
   #   - Libero (LIBERO_INSTALL_DIR)
   #===============================================================================
   export SC_INSTALL_DIR=/home/$USER/Microchip/SoftConsole-v2022.2-RISC-V-747
   export LIBERO_INSTALL_DIR=/home/$USER/Microchip/Libero_SoC_v2024.2
   export LICENSE_FILE_DIR=/home/$USER/Microchip/license

   #===============================================================================
   # The following was tested on Ubuntu 24.04.1 with:
   #   - Libero 2024.2
   #   - SoftConsole 2022.2
   #===============================================================================

   #
   # SoftConsole
   #
   #
   # Libero
   #
   export PATH=$PATH:$LIBERO_INSTALL_DIR/Libero/bin:$LIBERO_INSTALL_DIR/Libero/bin64
   export PATH=$PATH:$LIBERO_INSTALL_DIR/Synplify/bin
   export PATH=$PATH:$LIBERO_INSTALL_DIR/Model/modeltech/linuxacoem
   export LOCALE=C
   export LD_LIBRARY_PATH=/usr/lib/i386-linux-gnu:$LD_LIBRARY_PATH

   #
   # Libero License daemon
   #
   export LM_LICENSE_FILE=1702@localhost
   export SNPSLMD_LICENSE_FILE=1702@localhost

   $LIBER
   export PATH=$PATH:$SC_INSTALL_DIR/riscv-unknown-elf-gcc/bin
   export FPGENPROG=$LIBERO_INSTALL_DIR/Libero/bin64/fpgenprog

   #
   # Libero
   #
   export PATH=$PATH:$LIBERO_INSTALL_DIR/Libero/bin:$LIBERO_INSTALL_DIR/Libero/bin64
   export PATH=$PATH:$LIBERO_INSTALL_DIR/Synplify/bin
   export PATH=$PATH:$LIBERO_INSTALL_DIR/Model/modeltech/linuxacoem
   export LOCALE=C
   export LD_LIBRARY_PATH=/usr/lib/i386-linux-gnu:$LD_LIBRARY_PATH

   #
   # Libero License daemon
   #
   export LM_LICENSE_FILE=1702@localhost
   export SNPSLMD_LICENSE_FILE=1702@localhost

   $LIBERO_INSTALL_DIR/Libero/bin64/lmgrd -c $LICENSE_FILE_DIR/License.dat -l $LICENSE_FILE_DIR/license.log

I suggest popping the code snippet above in a file called ``setup-microchip-tools.sh``, similar to the instructions from Beagle.

before executing Libero you will need to source this script from whatever location you decide to leave it.

.. code-block:: bash

   source setup-microchip-tools.sh

after this you will be able to run `libero` from the terminal you sourced the script in. Don't forget to 
re-source the script when starting a new terminal environment if you want access to the tools.

Support and Acknowledgements
*****************************

Getting this all to work was a bit of a journey. I received support from the friendly folk over in the
`BeagleBone Discord <https://bbb.io/discord>`_. If you come across anything maybe head over there and try your luck!

Thanks to everyone who gave me a hand working through some of the quirks in getting this setup, Leoh in particular!

Written by Lucien Morey - 16/10/24
