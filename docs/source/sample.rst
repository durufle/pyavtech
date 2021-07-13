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
