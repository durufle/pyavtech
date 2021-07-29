import cmd
from pyavtech.pyavr import PyAvr
from importlib.metadata import version


class AvrShell(cmd.Cmd):
    intro = 'Welcome to the AVR shell.   Type help or ? to list commands.\n'
    prompt = 'avr > '
    device = None
    file = None
    version = "0.1.0"

    def do_version(self, arg):
        """ Get application and package version: version"""
        print('\n'.join(["  Executable    : {0}".format(self.version),
                         "  Package       : {0}".format(version('pyavtech')),
                         ]))

    def do_connect(self, arg):
        """ Connection to the device: connect address port """
        if arg:
            alias = arg
            self.device = PyAvr(alias.upper())

    def do_identity(self, arg):
        """ get device identity: identity """
        if self.device:
            print("  Identity        : " + self.device.get_identifier)

    def do_amplitude(self, arg):
        """ get / set device power in mA: power , power [value] """
        if self.device:
            if arg:
                try:
                    self.device.set_amplitude(int(arg))
                except Exception as e:
                    print("  Exception occur : {0}".format(e))
            else:
                print("  Amplitude value : " + self.device.get_amplitude())

    def do_frequency(self, arg):
        """ get / set device frequency: frequency , frequency [value] """
        if self.device:
            if arg:
                try:
                    self.device.set_frequency(int(arg))
                except Exception as e:
                    print("  Exception occur : {0}".format(e))
            else:
                print("  Frequency       : " + self.device.get_frequency())

    def do_delay(self, arg):
        """ get / set device delay: delay , delay [value] """
        if self.device:
            if arg:
                try:
                    self.device.set_delay(int(arg))
                except Exception as e:
                    print("  Exception occur : {0}".format(e))
            else:
                print("  Delay           : " + self.device.get_delay())

    def do_width(self, arg):
        """ get / set device width: width , width [value] """
        if self.device:
            if arg:
                try:
                    self.device.set_width(int(arg))
                except Exception as e:
                    print("  Exception occur : {0}".format(e))
            else:
                print("  Width           : " + self.device.get_width())

    def do_output(self, arg):
        """ get / set device output: output , output ["on" / "off"] """
        if self.device:
            if arg:
                try:
                    self.device.set_output(arg)
                except Exception as e:
                    print("  Exception occur : {0}".format(e))
            else:
                print("  Output          : " + self.device.get_output())

    def do_count(self, arg):
        """ get / set device burst count : count , count [value] """
        if self.device:
            if arg:
                try:
                    self.device.set_burst_count(int(arg))
                except Exception as e:
                    print("  Exception occur : {0}".format(e))
            else:
                print("  Burst count     : " + self.device.get_burst_count())

    def do_space(self, arg):
        """ get / set device burst space : space , space [value] """
        if self.device:
            if arg:
                try:
                    self.device.set_burst_spacing(int(arg))
                except Exception as e:
                    print("  Exception occur : {0}".format(e))
            else:
                print("  Burst space     : " + self.device.get_burst_spacing())

    def do_exit(self, arg):
        """ Close connection with the device and exit..."""
        print('Thank you for using AVR shell...')
        if self.device:
            self.device.close()
        raise SystemExit

    # ----- record and playback -----
    def do_record(self, arg):
        """ Save future commands to filename:  record [file] """
        try:
            self.file = open(arg, 'w')
        except FileNotFoundError as e:
            print("  Exception occur : {0}".format(e))

    def do_playback(self, arg):
        """ Playback commands from a file:  playback [file] """
        self.close_record()
        try:
            with open(arg) as f:
                self.cmdqueue.extend(f.read().splitlines())
        except FileNotFoundError as e:
            print("  Exception occur : {0}".format(e))

    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line

    def close_record(self):
        if self.file:
            self.file.close()
            self.file = None


def main(argv=None):
    AvrShell().cmdloop()


if __name__ == '__main__':
    main()
