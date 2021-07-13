
# AVTECH Python package

This package allow to drive AVTECH pulse generator. 

To install this package in your environment
```bash
pip install pyavtech
```

To import the module in your code:
```python
from pyavtech.pyavr import PyAvr

```

To open a communication with the device using its alias string:
```python
device = PyAvr(alias)

```

To open a communication with the device using its GPIB VISA resource name:
```python
device = PyAvr("GPIB0::2::INSTR")
```


