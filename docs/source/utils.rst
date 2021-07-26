Utils
=====

Utils script are installed during package installation process

avtech_info
-----------
This utility return avtech's parameter. It's useful to check if everything is setup properly.

.. code-block:: bash

    > avtech_info

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

Example:

.. code-block:: console

    > avtech_info -a "GPIB0::8::INSTR"
    > pyavr package version : 0.2.0
    > Identity     : AVTECH ELECTROSYSTEMS,AVR-3HE-B-PN-BR,SN:13495,v6.2.17OL
    > Frequency    : 1.0000e+00
    > Width        : 4.0000e-08
    > Delay        : 0.0000
    > Amplitude    : 0.0000
    > Output       : off
    > burst count  : 1

    > Process finished with exit code 0

avr_cli
-------
This utility is a line-oriented command interpreter given access to a set of command.

list of command:

.. code-block:: console

    Welcome to the AVR shell.   Type help or ? to list commands.

    avr > ?

    Documented commands (type help <topic>):
    ========================================
    amplitude  count  exit       help      output    record  version
    connect    delay  frequency  identity  playback  space   width

    avr >

