Tree Valuation
==============

** This tool is still Work In Progress **

Automates form filling when having a bunch of trees  to  valuate.   The  program
expects trees to be in an Excell file. It parses the file and valuates each tree
via endpoint located in [2]. It than writes the valuation data to an Excell file.


Installation
------------

To install the program execute the following command where "cz.val-tree"  is  an
example name of the built container:

    docker build . -t cz.val-tree


Usage
-----

To run the program, mount a folder containing an input sheet into the container
and provide the path to the input sheet in the container. This can be done with
the following command:

    docker run -v $(pwd)/data:/mnt -t cz.val-tree /mnt/trees.xlsm

Where "$(pwd)/data" is  an  example  of  a  folder  containing  an  input  sheet
trees.xlsm.  The folder is mounted into the  container's  "/mnt".   Results  are
written into trees.val.xlsm.


Possible Improvements [TODO]
----------------------------


References
----------

  [1]: https://www.ochranaprirody.cz/res/archive/434/075767.pdf?seek=1648738598
  [2]: https://ocenovanidrevin.nature.cz/

