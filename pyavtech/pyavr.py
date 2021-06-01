import pyvisa as visa
import logging


class PyAvr:
    """
    Class to control an AVR device using VISA

    """
    version = "0.2.0"
    __version__ = version

    __output = {
        "0": "off",
        "1": "on"
    }

    def __init__(self, alias):
        self.__manager = None
        self.__resources = None
        self.__identifier = None

        self.__manager = visa.ResourceManager()
        self.__is_open = False
        self.__logger = logging.getLogger(__name__)

        try:
            self.__device = self.__manager.open_resource(alias)
            self.__device.timeout = 1000
            self.__identifier = self.__device.query('*IDN?').strip("\n")
            self.__is_open = True
        except visa.VisaIOError as err:
            self.__logger.warning("{}".format(err))

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

        :return:
        """
        try:
            if self.__is_open:
                self.__device.close()
        except visa.VisaIOError as err:
            self.__logger.warning("{}".format(err))

    @property
    def is_open(self):
        """
        Return device open flag

        :return:
        :rtype:
        """
        return self.__is_open

    @property
    def get_identifier(self):
        """
        Get device identifier

        :return: device identifier string
        :rtype: str
        """
        if self.__is_open:
            return self.__identifier

    def get_output(self):
        """
        Get output state

        :return: output state
        :rtype: str
        """
        try:
            if self.__is_open:
                resp = self.__device.query('output?')
                return self.__get_output_state(str(resp).strip("\n"))
        except visa.VisaIOError as err:
            self.__logger.warning("{}".format(err))

    def set_output(self, value):
        """
        Set output state

        :param value:
        :type value:
        :return:
        :rtype:
        """
        try:
            if self.__is_open and value in ("on", "off"):
                return self.__device.write('output ' + str(value))
            else:
                self.__logger.warning("Device not open, or bad parameter...")
        except visa.VisaIOError as err:
            self.__logger.warning("{}".format(err))

    def get_frequency(self):
        """
        Return device frequency value

        :return: frequency value
        :rtype: str
        """
        try:
            if self.__is_open:
                return self.__device.query('frequency?').strip("\n")
        except visa.VisaIOError as err:
            self._logger.warning("{}".format(err))

    def set_frequency(self, value):
        """
        Set device frequency value

        :param value: frequency value string
        :rtype value: int
        :return:
        """
        try:
            if self.__is_open:
                return self.__device.write('frequency ' + str(value) + ' Hz')
        except visa.VisaIOError as err:
            self.__logger.warning("{}".format(err))

    def get_delay(self):
        """
        Return device delay value

        :return: pulse delay value
        """
        try:
            if self.__is_open:
                return self.__device.query('pulse:delay?').strip("\n")
        except visa.VisaIOError as err:
            self.__logger.warning("{}".format(err))

    def set_delay(self, value):
        """
        Set device delay value

        :param value: delay value string
        :return:
        """
        try:
            if self.__is_open:
                return self.__device.write('pulse:delay ' + str(value) + ' ns')
        except visa.VisaIOError as err:
            self.__logger.warning("{}".format(err))

    def get_width(self):
        """
        Return device width value

        :return: pulse width value
        """
        try:
            if self.__is_open:
                return self.__device.query('pulse:width?').strip("\n")
        except visa.VisaIOError as err:
            self.__logger.warning("{}".format(err))

    def set_width(self, value):
        """
        Set device width value

        :param value: width value string
        :return:
        """
        try:
            if self.__is_open:
                return self.__device.write('pulse:width ' + str(value) + ' ns')
        except visa.VisaIOError as err:
            self.__logger.warning("{}".format(err))

    def get_amplitude(self):
        """
        Return device amplitude value

        :return: amplitude value
        """
        try:
            if self.__is_open:
                return self.__device.query('voltage?').strip("\n")
        except visa.VisaIOError as err:
            self.__logger.warning("{}".format(err))

    def set_amplitude(self, value):
        """
        Set device amplitude value

        :param value: amplitude value string
        :return:
        """
        try:
            if self.__is_open:
                return self.__device.write('volt:ampl ' + str(value) + ' mV')
        except visa.VisaIOError as err:
            self.__logger.warning("{}".format(err))

    def get_burst_count(self):
        """
        Return burst count value

        :return: burst count value
        :rtype: str
        """
        try:
            if self.__is_open:
                return self.__device.query('pulse:count?').strip("\n")
        except visa.VisaIOError as err:
            self.__logger.warning("{}".format(err))

    def set_burst_count(self, value):
        """
        Set device burst count value

        :return:
        """
        try:
            if self.__is_open:
                return self.__device.write('pulse:count ' + str(value))
        except visa.VisaIOError as err:
            self.__logger.warning("{}".format(err))

