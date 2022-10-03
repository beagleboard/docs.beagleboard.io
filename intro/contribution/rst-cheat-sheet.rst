.. _rst-cheat-sheet:

ReStructuredText Cheat Sheet
############################

BeagleBoard docs is mostly writted with ReStructuredText (r)

Headings
*********

For each document we divide sections with headings and in ReStructuredText we can use 
matching overline and underline to indicate a heading. 

1. Document heading (H1) use ``#``.
2. First heading (H2) use ``*``.
3. First heading (H2) use ``=``.
4. First heading (H2) use ``-``.
5. First heading (H2) use ``~``.

.. note::
    You can include only one (H1) ``#`` in a single documentation page.

Make sure the length of your heading symbol is atleast (or 
more) the lenth of the heading text, for example:


.. callout::

    .. code-block:: ReStructuredText

        incorrect H1
        ##### <1>

        correct H1
        ############ <2>
    
    .. annotations::

        <1> Length of heading sybol ``#`` is smaller than the content above.

        <2> Shows the correct way of setting the document title (H1) with ``#``.

    
