.. _beagleconnect_freedom_home:

BeagleConnect Freedom
#####################

BeagleConnect™ Freedom is an open-hardware wireless hardware platform developed by BeagleBoard.org and built around the TI CC1352P7 microcontroller, which supports both 
2.4-GHz and long-range, low-power Sub-1 GHz wireless protocols. Rapidly prototyping of IoT applications is accelerated by hardware compatibility with over 1,000 mikroBUS add-on sensors,
acutators, indicators and additional connectivity and storage options, and backed with software support utilizing the Zephyr scalable and modular real-time operating system, allowing developers
to tailor the solution to their specific needs.  BeagleConnect Freedom further includes MSP430F5503 for USB-to-UART functionality, temperature and humidity sensor, light sensor, SPI flash,
battery charger, buzzer, LEDs, and JTAG connections to make it a comprehensive solution for IoT development and prototyping.

The TI CC1352P7 microcontroller (MCU) includes a 48-MHz Arm Cortex-M4F processor, 704KB Flash memory, 256KB ROM, 8KB Cache SRAM, 144KB of ultra-low leakage SRAM, and
over-the-air upgrades (OTA) capability. This MCU provides flexible support for many different protocols and bands making it suitable for many different communication requirements.

.. image:: media/BeagleConnect-Freedom-Hand.*
  :align: center
  :alt: BeagleConnect™ Freedom board

.. important::
   
    This is a work in progress, for latest documentation please 
    visit https://docs.beagleboard.org/latest/

.. grid:: 2

    .. grid-item::
        :columns: 12 12 12 4

         .. figure:: media/OSHW_mark_US002175.*
            :width: 200
            :target: https://certification.oshwa.org/us002175.html
            :alt: BeagleConnect™ Freedom OSHW Mark

    .. grid-item::
        :columns: 12 12 12 8

        .. admonition:: License Terms

            * This documentation is licensed under a `Creative Commons Attribution-ShareAlike 4.0 International License <http://creativecommons.org/licenses/by-sa/4.0/>`__
            * Design materials and license can be found in the `git repository <https://git.beagleboard.org/beagleconnect/freedom>`__
            * Use of the boards or design materials constitutes an agreement to the :ref:`boards-terms-and-conditions`
            * Software images and purchase links available on the `board page <https://www.beagleboard.org/boards/beagleconnect-freedom>`__
            * For export, emissions and other compliance, see :ref:`beagleconnect-freedom-support`

.. raw:: latex
   
   \begin{comment}

.. grid:: 1 1 2 3
   :margin: 4 4 0 0
   :gutter: 4

   .. grid-item-card::
      :link: beagleconnect-freedom-introduction
      :link-type: ref

      **1. Introduction**
      ^^^

      .. image:: media/chapter-thumbnails/01-introduction.*
         :align: center
         :alt: BeagleConnect™ Freedom Chapter1 thumbnail
      
      +++

      Introduction to BeagleConnect™ Freedom.


   .. grid-item-card:: 
      :link: beagleconnect-freedom-quick-start
      :link-type: ref

      **2. Quick start**
      ^^^

      .. image:: media/chapter-thumbnails/02-quick-start.*
         :align: center
         :alt: BeagleConnect™ Freedom Chapter2 thumbnail

      +++

      Getting started guide and tutorials.

   .. grid-item-card:: 
      :link: beagleconnect-freedom-design
      :link-type: ref

      **3. Design & Specifications**
      ^^^

      .. image:: media/chapter-thumbnails/03-design-and-specifications.*
         :align: center
         :alt: BeagleConnect™ Freedom Chapter3 thumbnail

      +++

      Hardware and mechanical design and specifications of the BeagleConnect Freedom
      board and enclosure for those who want to know their board inside and out.

   .. grid-item-card:: 
      :link: beagleconnect-freedom-expansion
      :link-type: ref

      **4. Expansion**
      ^^^

      .. image:: media/chapter-thumbnails/04-connectors-and-pinouts.*
         :align: center
         :alt: BeagleConnect™ Freedom Chapter4 thumbnail

      +++

      Connector pinout diagrams with expansion details so that you can 
      easily debug your connections and create custom expansion hardware.

   .. grid-item-card:: 
      :link: beagleconnect-freedom-demos
      :link-type: ref

      **5. Demos & tutorials**
      ^^^

      .. image:: media/chapter-thumbnails/05-demos-and-tutorials.*
         :align: center
         :alt: BeagleConnect™ Freedom Chapter5 thumbnail

      +++

      Demos and tutorials to quickly learn about the BeagleConnect capabilities.

   .. grid-item-card:: 
      :link: beagleconnect-freedom-support
      :link-type: ref

      **6. Support**
      ^^^

      .. image:: media/chapter-thumbnails/06-support-documents.*
         :align: center
         :alt: BeagleConnect™ Freedom Chapter6 thumbnail

      +++

      Additional supporting information, images, documents, change history and
      hardware & software repositories including issue trackers.

.. raw:: latex

   \end{comment}

.. toctree::
   :maxdepth: 1
   :hidden:

   01-introduction
   02-quick-start
   03-design
   04-expansion
   05-demos
   06-support
