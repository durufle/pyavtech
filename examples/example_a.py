from pyavtech import PyAvr
import sys
import logging

VERSION = '1.0'

USAGE = '''example_a: execute the avtech class example a
Usage:
    python example_a.py [options]

Options:
    -h, --help              this help message.
    -v, --version           version info.
    _l, --logging           logging
    -a, --alias             avtech alias 
'''


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
        e = sys.exc_info()[1]     # current exception
        sys.stderr.write(str(e)+"\n")
        sys.stderr.write(USAGE+"\n")
        return 1

    if alias is None:
        alias = "LCT_GPIB_AVR_EMFI"

    if log is True:
        logging.basicConfig(level=logging.INFO)

    device = PyAvr(alias)

    if device.is_open:
        print("Identity     : {0}".format(device.get_identifier))
        print("Frequency    : {0}".format(device.get_frequency()))
        print("Width        : {0}".format(device.get_width()))
        print("Delay        : {0}".format(device.get_delay()))
        print("Amplitude    : {0}".format(device.get_amplitude()))
        print("Output       : {0}".format(device.get_output()))
        print("burst count  : {0}".format(device.get_burst_count()))
        device.close()


if __name__ == '__main__':
    sys.exit(main())
