from pyavtech.pyavr import PyAvr
import sys
import logging

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
    python example.py -a LCT_GPIB_AVR_EMFI
        -> execute script using alias
        
    python example.py -a GPIO0::8::INSTR
        -> execute script using VISA address
        
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
        sys.stderr.write("device alias or address is mandatory...\n")
        sys.stderr.write(USAGE+"\n")
        return 1

    if log is True:
        logging.basicConfig(level=logging.INFO)

    device = PyAvr(alias)
    print("pyavr package version : {0}".format(PyAvr.__version__))

    if device.is_open:
        print("Identity     : {0}".format(device.get_identifier))
        print("Frequency    : {0}".format(device.get_frequency()))
        print("Width        : {0}".format(device.get_width()))
        print("Delay        : {0}".format(device.get_delay()))
        print("Amplitude    : {0}".format(device.get_amplitude()))
        print("Output       : {0}".format(device.get_output()))
        print("burst count  : {0}".format(device.get_burst_count()))

        # Width command
        print(" Set width to 2000...")
        print(device.set_width(2000))
        print(" Width : {0}".format(device.get_width()))

        print(" Set width to 1000...")
        device.set_width(1000)
        print(" Width : {0}".format(device.get_width()))

        # Delay command
        print(" Set delay to 0...")
        device.set_delay(0)
        print(" delay : {0}".format(device.get_delay()))

        print(" Set delay to 200...")
        device.set_delay(20)
        print(" delay : {0}".format(device.get_delay()))

        # Frequency command
        print(" Set Frequency to 5 Hz...")
        device.set_frequency(5)
        print(" Frequency : {0}".format(device.get_frequency()))

        print(" Set Frequency to 2000 Hz...")
        device.set_frequency(2000)
        print(" Frequency : {0}".format(device.get_frequency()))

        # Amplitude command
        print(" Set Amplitude to 1000 mV...")
        device.set_amplitude(1000)
        print(" Amplitude : {0}".format(device.get_amplitude()))

        print(" Set Frequency to 2000 mV...")
        device.set_amplitude(2000)
        print(" Amplitude : {0}".format(device.get_amplitude()))

        device.set_amplitude(0)
        print(" Output : {0}".format(device.get_output()))
        print(" Set output on...")
        device.set_output("on")
        print(" Output : {0}".format(device.get_output()))
        print(" Set output off...")
        device.set_output("off")
        print(" Output : {0}".format(device.get_output()))
        print(" Set output bad...")
        device.set_output("bad")
        
        device.close()

    # try to close again
    device.close()


if __name__ == '__main__':
    sys.exit(main())
