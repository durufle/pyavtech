Examples
========

- Open a session using the VISA address

.. code-block:: python

    from pyavtech.pyavr import PyAvr

    device = PyAvr("GPIB0::8::INSTR")
    if device.is_open:
        print("Identity     : {0}".format(device.get_identifier))
        ...
    device.close()


If an alias has been setup in the system , the alias name can be used instead

.. code-block:: python

    from pyavtech.pyavr import PyAvr

    device = PyAvr("AVTECH")
    if device.is_open:
        print("Identity     : {0}".format(device.get_identifier))
        ...
    device.close()

- Get information and parameters

.. code-block:: python

    from pyavtech.pyavr import PyAvr

    device = PyAvr("GPIB0::8::INSTR")
    if device.is_open:
        print("Identity     : {0}".format(device.get_identifier))
        print("Frequency    : {0}".format(device.get_frequency()))
        print("Width        : {0}".format(device.get_width()))
        print("Delay        : {0}".format(device.get_delay()))
        print("Amplitude    : {0}".format(device.get_amplitude()))
        print("Output       : {0}".format(device.get_output()))
        print("burst count  : {0}".format(device.get_burst_count()))

        device.close()

- set parameters

.. code-block:: python

    from pyavtech.pyavr import PyAvr

    device = PyAvr("GPIB0::8::INSTR")
    if device.is_open:
            # Width command
        print(" Set width to 2000...")
        print(device.set_width(2000))
        print(" Width : {0}".format(device.get_width()))

        print(" Set width to 1000...")
        device.set_width(1000)
        print(" Width : {0}".format(device.get_width()))

        # Delay command
        print(" Set delay to 0...")
        device.set_delay(0)
        print(" delay : {0}".format(device.get_delay()))

        print(" Set delay to 20 ns...")
        device.set_delay(20)
        print(" delay : {0}".format(device.get_delay()))

        # Frequency command
        print(" Set Frequency to 5 Hz...")
        device.set_frequency(5)
        print(" Frequency : {0}".format(device.get_frequency()))

        print(" Set Frequency to 2000 Hz...")
        device.set_frequency(2000)
        print(" Frequency : {0}".format(device.get_frequency()))

        # Amplitude command
        print(" Set Amplitude to 1000 mV...")
        device.set_amplitude(1000)
        print(" Amplitude : {0}".format(device.get_amplitude()))

        # Amplitude command
        print(" Set Amplitude to 2000 mV...")
        device.set_amplitude(2000)
        print(" Amplitude : {0}".format(device.get_amplitude()))

        # Output command
        device.set_amplitude(0)
        print(" Output : {0}".format(device.get_output()))
        print(" Set output on...")
        device.set_output("on")
        print(" Output : {0}".format(device.get_output()))
        print(" Set output off...")
        device.set_output("off")
        print(" Output : {0}".format(device.get_output()))
        print(" Set output bad...")
        device.set_output("bad")

        device.close()