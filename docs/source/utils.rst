Utils
=====

Utils script are installed during package installation process

avtech_info
-----------
This utility return avtech's parameter. It's useful to check if everything is setup properly.

.. code-block::

    (venv) avtech_info

    device alias or address is mandatory...

    Return avtech information

    Usage:
        python avtech_info.py [options]

    Options:
        -h, --help              this help message.
        -v, --version           version info.
        -a, --alias             alias

    example:
        python avtech_info.py -a GPIB0::8::INSTR
            -> execute script using VISA address

        python avtech_info.py -a AVTECH
            -> execute script using an alias name

