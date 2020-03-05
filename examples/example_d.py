from pyavtech import PyAvr
import sys
import logging

VERSION = '1.0'

USAGE = '''example_d: execute the avtech class example d
Usage:
    python example_c.py [options]

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
        device.close()


if __name__ == '__main__':
    sys.exit(main())
