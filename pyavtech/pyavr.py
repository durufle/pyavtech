import pyvisa as visa
import logging


class PyAvr:
    """
    Class to control an AVR device using VISA
    """
    __output = {
        "0": "off",
        "1": "on"
    }

    def __init__(self, alias):
        self.__is_open = False
        self._logger = logging.getLogger(__name__)
        self._frequency_range = {}
        self._delay_range = {}
        self._width_range = {}
        self._voltage_range = {}
        self._device_frequency_unit = 'Hz'

        try:
            self._device = visa.ResourceManager().open_resource(alias)
            self._device.timeout = 1000
            self.__is_open = True
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    def __get_output_state(self, number):
        """
        Return string message link to a output state

        :param number: output state (on./off)
        :return:
        """
        msg = self.__output.get(number, "output state not supported")
        if msg is None:
            return "{0}".format(number)
        return msg

    def close(self):
        """
        Close the device
        """
        try:
            if self.__is_open:
                self.set_amplitude(0)
                self.output = 'off'
                self._device.close()
                self.__is_open = False
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    @property
    def is_open(self):
        """
        Return device open flag

        :return: open session status
        :rtype: bool
        """
        return self.__is_open

    @property
    def identifier(self):
        """
        Get device identifier

        :return: device identifier string
        """
        return self._device.query('*IDN?').strip("\n")

    @property
    def output(self) -> str:
        """
        Get output state

        :return: output state ("on" or "off")
        """
        resp = self._device.query('output?')
        return self.__get_output_state(str(resp).strip("\n"))

    @output.setter
    def output(self, value: str):
        """
        Set output state

        :param value: output state ("on", "off")
        """
        try:
            if self.__is_open and value in ("on", "off"):
                self._device.write('output ' + value)
            else:
                self._logger.warning("Device not open, or bad parameter...")
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    def frequency_min(self, value: int):
        self._device.write('frequency min' + str(value) + 'Hz')

    @property
    def frequency(self) -> str:
        """
        Return device frequency value

        :return: frequency value
        :rtype: str
        """
        return self._device.query('frequency?').strip("\n")

    @frequency.setter
    def frequency(self, value: int):
        """
        Set device frequency value

        :param value: frequency value
        :rtype value: int in Hz
        :return:
        """
        self._device.write('frequency ' + str(value) + 'Hz')

    def get_delay(self, channel=1) -> str:
        """
        Return device delay value

        :param channel: channel number (default = 1)
        :return: pulse delay value
        """
        return self._device.query(f'pulse:delay{channel}?').strip("\n")

    def set_delay(self, value: float, channel=1):
        """
        Set device delay value

        :param value: delay value string
        :param channel: channel number (default = 1)
        """
        self._device.write(f'pulse:delay{channel} {value} ns')

    def width_range(self, channel=1):
        self._width_range['min'] = self._device.query(f'pulse:width{channel}? min').strip("\n")
        self._width_range['max'] = self._device.query(f'pulse:width{channel}? max').strip("\n")
        return self._width_range

    def get_width(self, channel=1):
        """
        Return device width value

        :param channel: channel number (default = 1)
        :return: pulse width value
        """
        return self._device.query(f'pulse:width{channel}?').strip("\n")

    def set_width(self, value: float, channel=1):
        """
        Set device width value

        :param value: width value in ns
        :param channel: channel number (default = 1)
        """
        cmd = f'pulse:width{channel} {value} ns'
        result = self._device.write(cmd)
        return result

    def amplitude_range(self, channel=1):
        self._voltage_range['min'] = self._device.query(f'volt:ampl{channel}? min').strip("\n")
        self._voltage_range['max'] = self._device.query(f'volt:ampl{channel}? max').strip("\n")
        return self._voltage_range

    def get_amplitude(self, channel=1):
        """
        Return device amplitude value

        :param channel: channel number (default = 1)
        :return: amplitude value
        """
        return self._device.query(f'voltage{channel}?').strip("\n")

    def set_amplitude(self, value: int, channel=1):
        """
        Set device amplitude value

        :param value: amplitude value string
        :param channel: channel number (default = 1)
        """
        return self._device.write(f'volt:ampl{channel} {value} mV')

    @property
    def burst_count(self) -> str:
        """
        Return burst count value

        :return: burst count value
        """
        return self._device.query('pulse:count?').strip("\n")

    @burst_count.setter
    def burst_count(self, value: int):
        """
        Set device burst count value

        :param value: burst count number
        """
        self._device.write('pulse:count ' + str(value))

    @property
    def burst_spacing(self) -> str:
        """
        Return burst spacing time

        :return: burst spacing value in us
        """
        return self._device.query('pulse:sep?').strip("\n")

    @burst_spacing.setter
    def burst_spacing(self, value: int):
        """
        Set device burst spacing value in us
        """
        self._device.write('pulse:separation ' + str(value) + ' us')

    @property
    def trigger_source(self) -> str:
        """
        Get the trigger source 
        
        :return: trigger source
        """
        return self._device.query('TRIGger:SOURce?').strip("\n")

    @trigger_source.setter
    def trigger_source(self, value: str):
        """
        Set the trigger source 

        :param value: trigger source
        """
        self._device.write('TRIGger:SOURce ' + str(value))
