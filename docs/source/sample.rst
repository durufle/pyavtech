Examples
========

Example showing how to connect to the device and get parameter values.
In this example, the device alias name is used for the connection.

See :file:`../../examples/example.py`.

.. code-block:: python

    from pyavtech.pyavr import PyAvr
            device = PyAvr("GPIB0::8::INSTR")
            if device.is_open:
                print("Identity     : {0}".format(device.get_identifier))
                ...
            device.close()