import sys
import os
import yaml
from gooey import Gooey, GooeyParser
from pyavtech.pyavr import PyAvr


def main():
    # Read config file, get device address and connection
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # open yaml file
    config = os.path.join(current_dir, "avtech_gui.yml")
    try:
        with open(config, 'r') as file:
            cfg = yaml.safe_load(file)
    except FileNotFoundError as e:
        print(f"Configuration file opening error: {e}")
        sys.exit(-1)
    # get device address
    address = cfg['visa']['address']
    # open device
    device = PyAvr(address)

    parameters(device)


@Gooey(program_name='AVTECH Control Panel', program_description="AVTECH remote control utility")
def parameters(device):
    parser = GooeyParser(description='AVTECH Pulse generator GUI')
    parser.add_argument('-t', '--trigger', choices=['INT', 'EXT', 'MAN', 'HOL', 'IMM'], default='INT',
                        help="Pulse generator trigger mode", )
    parser.add_argument('-f', '--frequency', help="Pulse generator frequency value in Hz", widget='DecimalField')
    parser.add_argument('-o', '--output', choices=['on', 'off'], default='off', help="Pulse generator output state")
    parser.add_argument('-b', '--burst', default=device.burst_count, help="Pulse generator burst count number")
    parser.add_argument('-s', '--spacing', default=device.burst_spacing, help="Pulse generator burst count spacing")

    parser.add_argument('-c', '--channel', default=1, help="Select active channel")
    group = parser.add_argument_group('Channel parameters', gooey_options={'show_border': True})
    group.add_argument('-d', '--delay', default=device.get_delay(1), help="Set active channel delay")
    group.add_argument('-v', '--voltage', default=device.get_amplitude(1), help="Set active channel pulse voltage")
    group.add_argument('-w', '--width', default=device.get_width(1), help="Set active channel pulse width")

    args = parser.parse_args()
    # set all parameters
    device.frequency = args.frequency
    device.trigger_source = args.trigger
    device.output = args.output
    device.burst_count = args.burst
    device.burst_spacing = args.spacing
    device.set_delay(value=args.delay, channel=args.channel)
    device.set_amplitude(value=args.voltage, channel=args.channel)
    device.set_width(value=args.width, channel=args.channel)


if __name__ == '__main__':
    sys.exit(main())
