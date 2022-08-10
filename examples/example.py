import pathlib, sys, os
from pyavtech.pyavr import PyAvr
from importlib.metadata import version
import sys
import logging

FILE_ABS_PATH = pathlib.Path(__file__).parent.resolve()
LIB_PATH = os.path.normpath(os.path.normpath(FILE_ABS_PATH) + "/../")
sys.path.append(LIB_PATH)

VERSION = '0.1.0'

USAGE = '''example: execute the avtech class example script
Usage:
    python example.py [options]

Options:
    -h, --help              this help message.
    -v, --version           version info.
    _l, --logging           enable logging.
    -a, --alias             avtech alias
    
example:
    python example.py -a MRS_GPIB_AVR_EMFI
    python example.py -a MRS_GPIB_AVRK_EMFI
    python example.py -a MRS_LAN_AVRK_EMFI
        -> execute script using alias
        
    python example.py -a GPIO0::8::INSTR
        -> execute script using VISA address
        
'''

"""
    To execute this example, ensure that device aliases are correctly initialized in our system:
    - MRS_LAN_AVRK_EMFI for AVRK-4-B-PN-TR-DPF
    - MRS_LAN_AVR_EMFI for AVR-3HE-B-PN
"""


def main(argv=None):
    import getopt

    if argv is None:
        argv = sys.argv[1:]
    try:
        opts, args = getopt.gnu_getopt(argv, 'hvla:', ['help', 'version', 'logging', 'alias='])
        alias = None
        log = False

        for o, a in opts:
            if o in ('-h', '--help'):
                print(USAGE)
                return 0
            if o in ('-v', '--version'):
                print(VERSION)
                return 0
            elif o in ('-l', '--logging'):
                log = True
            elif o in ('-a', '--alias'):
                alias = a

    except getopt.GetoptError:
        e = sys.exc_info()[1]  # current exception
        sys.stderr.write(str(e) + "\n")
        sys.stderr.write(USAGE + "\n")
        return 1

    if alias is None:
        sys.stderr.write("device alias or address is mandatory...\n")
        sys.stderr.write(USAGE + "\n")
        return 1

    if log is True:
        logging.basicConfig(level=logging.DEBUG)

    device = PyAvr(alias)
    print("Package version : {0}".format(version('pyavtech')))

    if device.is_open:
        # Common API
        print("Identity     : {0}".format(device.get_identifier))
        print("Frequency    : {0}".format(device.get_frequency()))
        print("Amplitude    : {0}".format(device.get_amplitude()))

        # Output command
        print("Output           : {0}".format(device.get_output()))
        print("Set output on...")
        device.set_output("on")
        print("Output           : {0}".format(device.get_output()))
        print("Set output off...")
        device.set_output("off")
        print("Output           : {0}".format(device.get_output()))
        print("Set output bad...")
        device.set_output("bad")

        # Trigger
        print("Trigger source   : {0}".format(device.get_trigger_source()))

        if alias == "MRS_LAN_AVR_EMFI":
            print("---------------------------------------------------------------------------------------------------")
            print(f"Alias = {alias}")
            print("---------------------------------------------------------------------------------------------------")
            # burst
            print("spacing          : {0}".format(device.get_burst_spacing()))
            print("burst count      : {0}".format(device.get_burst_count()))

            # Width command
            print("Width            : {0}".format(device.get_width()))
            print("Set width to 2000...")
            device.set_width(2000)
            print("Width            : {0}".format(device.get_width()))
            print("Set width to 1000...")
            device.set_width(1000)
            print("Width            : {0}".format(device.get_width()))

            # Delay command
            print("Set delay to 0...")
            device.set_delay(0)
            print("delay            : {0}".format(device.get_delay()))
            print("Set delay to 200...")
            device.set_delay(20)
            print("delay            : {0}".format(device.get_delay()))

            # Frequency command
            print("Set Frequency to 5 Hz...")
            device.set_frequency(5)
            print("Frequency        : {0}".format(device.get_frequency()))
            print("Set Frequency to 2000 Hz...")
            device.set_frequency(2000)
            print("Frequency        : {0}".format(device.get_frequency()))

            # Amplitude command
            print("Set Amplitude to 1000 mV...")
            device.set_amplitude(1000)
            print("Amplitude        : {0}".format(device.get_amplitude()))
            print("Set Amplitude to 2000 mV...")
            device.set_amplitude(2000)
            print("Amplitude        : {0}".format(device.get_amplitude()))
            print("Set Amplitude to zero...")
            device.set_amplitude(0)

        if alias == "MRS_LAN_AVRK_EMFI":
            print("---------------------------------------------------------------------------------------------------")
            print(f"Alias = {alias}")
            print("---------------------------------------------------------------------------------------------------")
            # get parameters for each channel
            for channel in [1, 2]:
                print(f"Width {channel}      : {device.get_width(channel=channel)}")
                print(f"Delay {channel}      : {device.get_delay(channel=channel)}")
                print(f"Volt  {channel}      : {device.get_amplitude(channel=channel)}")

            # set get parameters for each channel
            print("set/get width channel 1...")
            channel = 1
            for width in [5.0, 5.5, 5.6]:
                device.set_width(width, channel=channel)
                print(f"Width {channel}      : {device.get_width(channel=channel)}")
            device.set_width(4.5, 1)
            print("set/get width channel 2...")
            channel = 2
            for width in [5.0, 5.5, 5.6]:
                device.set_width(width, channel=channel)
                print(f"Width {channel}      : {device.get_width(channel=channel)}")
            device.set_width(4.5, channel)
            print("set/get Delay channel 1...")
            channel = 1
            for delay in [1.5, 2.0, 2.5, 5]:
                device.set_delay(delay, channel=channel)
                print(f"Delay {channel}      : {device.get_delay(channel=channel)}")
            device.set_delay(0, channel)
            print("set/get delay channel 2...")
            channel = 2
            for delay in [150, 160, 170, 180]:
                device.set_delay(delay, channel=channel)
                print(f"Delay {channel}      : {device.get_delay(channel=channel)}")
            device.set_delay(0, channel)
            print("set/get Volt channel 1...")
            channel = 1
            for delay in [1000, 1100, 1200, 1500]:
                device.set_amplitude(delay, channel=channel)
                print(f"Volt {channel}      : {device.get_amplitude(channel=channel)}")
            device.set_amplitude(0, channel)
            print("set/get Volt channel 2...")
            channel = 2
            for delay in [1000, 1100, 1200, 1500]:
                device.set_amplitude(delay, channel=channel)
                print(f"Volt {channel}      : {device.get_amplitude(channel=channel)}")
            device.set_amplitude(0, channel)
        device.close()

    # try to close again
    device.close()


if __name__ == '__main__':
    sys.exit(main())
