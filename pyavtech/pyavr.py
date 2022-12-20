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
                self.output='off'
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
        try:
            if self.__is_open:
                return self._device.query('*IDN?').strip("\n")
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    @property
    def output(self) -> str:
        """
        Get output state

        :return: output state ("on" or "off")
        """
        try:
            if self.__is_open:
                resp = self._device.query('output?')
                return self.__get_output_state(str(resp).strip("\n"))
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

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

    @property
    def frequency(self) -> str:
        """
        Return device frequency value

        :return: frequency value
        :rtype: str
        """
        try:
            if self.__is_open:
                return self._device.query('frequency?').strip("\n")
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    @frequency.setter
    def frequency(self, value: int):
        """
        Set device frequency value

        :param value: frequency value
        :rtype value: int in Hz
        :return:
        """
        try:
            if self.__is_open:
                self._device.write('frequency ' + str(value) + ' Hz')
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    def get_delay(self, channel=1) -> str:
        """
        Return device delay value

        :param channel: channel number (default = 1)
        :return: pulse delay value
        """
        try:
            if self.__is_open:
                return self._device.query(f'pulse:delay{channel}?').strip("\n")
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    def set_delay(self, value: float, channel=1):
        """
        Set device delay value

        :param value: delay value string
        :param channel: channel number (default = 1)
        """
        try:
            if self.__is_open:
                self._device.write(f'pulse:delay{channel} {value} ns')
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    def get_width(self, channel=1):
        """
        Return device width value

        :param channel: channel number (default = 1)
        :return: pulse width value
        """
        try:
            if self.__is_open:
                return self._device.query(f'pulse:width{channel}?').strip("\n")
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    def set_width(self, value: float, channel=1):
        """
        Set device width value

        :param value: width value in ns
        :param channel: channel number (default = 1)
        """
        try:
            if self.__is_open:
                cmd = f'pulse:width{channel} {value} ns'
                result = self._device.write(cmd)
                return result
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    def get_amplitude(self, channel=1):
        """
        Return device amplitude value

        :param channel: channel number (default = 1)
        :return: amplitude value
        """
        try:
            if self.__is_open:
                return self._device.query(f'voltage{channel}?').strip("\n")
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    def set_amplitude(self, value: int, channel=1):
        """
        Set device amplitude value

        :param value: amplitude value string
        :param channel: channel number (default = 1)
        """
        try:
            if self.__is_open:
                return self._device.write(f'volt:ampl{channel} {value} mV')
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    @property
    def burst_count(self) -> str:
        """
        Return burst count value

        :return: burst count value
        """
        try:
            if self.__is_open:
                return self._device.query('pulse:count?').strip("\n")
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    @burst_count.setter
    def burst_count(self, value: int):
        """
        Set device burst count value

        :param value: burst count number
        """
        try:
            if self.__is_open:
                self._device.write('pulse:count ' + str(value))
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    @property
    def burst_spacing(self) -> str:
        """
        Return burst spacing time

        :return: burst spacing value in us
        """
        try:
            if self.__is_open:
                return self._device.query('pulse:sep?').strip("\n")
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    @burst_spacing.setter
    def burst_spacing(self, value: int):
        """
        Set device burst spacing value in us

        :return:
        """
        try:
            if self.__is_open:
                self._device.write('pulse:separation ' + str(value) + ' us')
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    @property
    def trigger_source(self) -> str:
        """
        Get the trigger source 
        
        :return: trigger source
        """

        try:
            if self.__is_open:
                return self._device.query('TRIGger:SOURce?').strip("\n")
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")

    @trigger_source.setter
    def trigger_source(self, value: str):
        """
        Set the trigger source 

        :param value: trigger source
        """

        try:
            if self.__is_open:
                self._device.write('TRIGger:SOURce ' + str(value))
        except visa.VisaIOError as err:
            self._logger.warning(f"{err}")
