from importlib.metadata import version
from pyavtech.pyavr import PyAvr
import sys
import logging

VERSION = '0.1.0'

USAGE = '''
Return avtech information

Usage:
    python avtech_info.py [options]

Options:
    -h, --help              this help message.
    -v, --version           version info.
    -a, --alias             alias or VISA address

example:
    python avtech_info.py -a GPIB0::8::INSTR
        -> execute script using VISA address

    python avtech_info.py -a AVTECH
        -> execute script using an alias name
'''


def main(argv=None):
    import getopt

    if argv is None:
        argv = sys.argv[1:]
    try:
        opts, args = getopt.gnu_getopt(argv, 'hva:', ['help', 'version', 'alias='])
        alias = None

        for o, a in opts:
            if o in ('-h', '--help'):
                print(USAGE)
                return 0
            if o in ('-v', '--version'):
                print(VERSION)
                return 0
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

    device = PyAvr(alias)
    print("pyavr package version : {0}".format(version("pyavtech")))

    if device.is_open:
        print("Identity     : {0}".format(device.get_identifier))
        print("Frequency    : {0}".format(device.get_frequency()))
        print("Width        : {0}".format(device.get_width()))
        print("Delay        : {0}".format(device.get_delay()))
        print("Amplitude    : {0}".format(device.get_amplitude()))
        print("Output       : {0}".format(device.get_output()))
        print("burst count  : {0}".format(device.get_burst_count()))

        device.close()

    # try to close again
    device.close()


if __name__ == '__main__':
    sys.exit(main())
