.. _pocketbeagle-2-support:

Additional Support Information
##############################

All support for this design is through BeagleBoard.org community 
at `BeagleBoard.org forum <https://forum.beagleboard.org/tag/pocketbeagle-2>`_.

.. _pocketbeagle-2-certifications:

Certifications and export control
*********************************

Export designations
===================

* ECCN: 3A991.a
* HSCODE: 8517180050
* USHSCODE: 8543708800
* EUHSCODE: 8543709099
* UPC number: 841454123484

.. _pocketbeagle-2-hardware-design:

Hardware Design
***************

You can find all PocketBeagle 2 hardware files 
`here <https://openbeagle.org/pocketbeagle/pocketbeagle-2>`_ under the `design` folder.

Production board boot media
***************************

.. todo:: Add production image link with board revision information.

.. _pocketbeagle-2-rma-support:

RMA Support
***********

If you feel your board is defective or has issues, request an Return Merchandise Application (RMA) 
by filling out the form at http://www.beagleboard.org/support/rma. You will need the serial number and 
revision of the board. The serial numbers and revisions keep moving. Different boards can have different 
locations depending on when they were made.

To see what SW revision is loaded into the running software image, check `/etc/dogtag`.
It should look something like as shown in example below,

.. code-block:: shell

   root@BeagleBone:~# cat /etc/dogtag
   BeagleBoard.org Debian Image 2024-02-24

Additionally, you can also collect information with:

.. code-block:: shell

   sudo beagle-version

This information will in most cases expedite your query considerably.

.. _pocketbeagle-2-getting-help:

Getting Help
************

If you need some up to date troubleshooting techniques, you can post your 
queries on link: `BeagleBoard.org forum <https://forum.beagleboard.org/tag/pocketbeagle-2>`_

| If you don't get a reasonable response in 24 hours, you are welcome to provide a link to the forum post
| in a meeting invite to me via https://calendly.com/jkridner (link also on https://www.beagleboard.org/about/jkridner).

.. _pocketbeagle-2-mechanical:

Mechanical Details
******************

.. _pocketbeagle-2-dimensions-and-weight:

Dimensions and Weight
=====================

.. table:: Dimensions & weight

   +--------------------+----------------------------------------------------+
   | Parameter          | Value                                              |
   +====================+====================================================+
   | Size               | 56 x 35mm                                          |
   +--------------------+----------------------------------------------------+
   | Max height         | 13.6                                               |
   +--------------------+----------------------------------------------------+
   | PCB Size           | 55 x 35mm                                          |
   +--------------------+----------------------------------------------------+
   | PCB Layers         | 10--layers                                         |
   +--------------------+----------------------------------------------------+
   | PCB Thickness      | 1.6mm                                              |
   +--------------------+----------------------------------------------------+
   | RoHS compliant     | Yes                                                |
   +--------------------+----------------------------------------------------+
   | Net Weight         | 12.7g                                              |
   +--------------------+----------------------------------------------------+
   | Gross Weight       | 19g                                                |
   +--------------------+----------------------------------------------------+


