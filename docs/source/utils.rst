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

details of commands:

- **connect**

.. code-block:: console

    Welcome to the AVR shell.   Type help or ? to list commands.

    avr > connect  GPIB0::8::INSTR
    avr > identity
        Identity        : AVTECH ELECTROSYSTEMS,AVR-3HE-B-PN-BR,SN:13495,v6.2.17OL
    avr >

- **amplitude**

.. code-block:: console

    Welcome to the AVR shell.   Type help or ? to list commands.

    avr > connect  GPIB0::8::INSTR
    avr > help amplitude
     get / set device power in mA: power , power [value]
    avr > amplitude
      Amplitude value : 0.0000
    avr > amplitude 10
    avr > amplitude
      Amplitude value : 1.0000e-02
    avr > amplitude 0
    avr > amplitude
      Amplitude value : 0.0000
    avr >

- **amplitude**

.. code-block:: console

    Welcome to the AVR shell.   Type help or ? to list commands.

    avr > connect  GPIB0::8::INSTR
    avr > help count
     get / set device burst count : count , count [value]
    avr > count
      Burst count     : 1
    avr > count 2
    avr > count
      Burst count     : 2
    avr > count 1
    avr > count
      Burst count     : 1
    avr >

- **output**

.. code-block:: console

    Welcome to the AVR shell.   Type help or ? to list commands.

    avr > connect  GPIB0::8::INSTR
    avr > help output
     get / set device output: output , output ["on" / "off"]
    avr > output
      Output          : off
    avr > output on
    avr > output
      Output          : on
    avr > output off
    avr > output
      Output          : off
    avr >

- **delay**

.. code-block:: console

    Welcome to the AVR shell.   Type help or ? to list commands.

    avr > connect  GPIB0::8::INSTR
    avr > help delay
     get / set device delay (ns): delay , delay [value]
    avr > delay
      Delay           : 1.0000e-05
    avr > delay
      Delay           : 1.0000e-05
    avr > delay 0
    avr > delay
      Delay           : 0.0000
    avr > delay 10
    avr > delay
      Delay           : 1.0000e-08
    avr >

- **space**

.. code-block:: console

    Welcome to the AVR shell.   Type help or ? to list commands.

    avr > connect  GPIB0::8::INSTR
    avr > help space
     get / set device burst space : space , space [value]
    avr > space
      Burst space     : 5.0000e-06
    avr > space 10
    avr > space
      Burst space     : 1.0000e-05
    avr >

- **width**

.. code-block:: console

    Welcome to the AVR shell.   Type help or ? to list commands.

    avr > connect  GPIB0::8::INSTR
    avr > help width
     get / set device width (ns): width , width [value]
    avr > width
      Width           : 4.0000e-08
    avr > width 100
    avr > width
      Width           : 1.0000e-07
    avr > width 40
    avr > width
      Width           : 4.0000e-08
    avr >

- **frequency**

.. code-block:: console

    Welcome to the AVR shell.   Type help or ? to list commands.

    avr > connect  GPIB0::8::INSTR
    avr > help frequency
     get / set device frequency (hz): frequency , frequency [value]
    avr > frequency
      Frequency       : 1.0000e+00
    avr > frequency 2
    avr > frequency
      Frequency       : 2.0000e+00
    avr > frequency 1
    avr > frequency
      Frequency       : 1.0000e+00
    avr >
