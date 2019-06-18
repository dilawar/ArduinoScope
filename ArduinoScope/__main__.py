__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2019-, Dilawar Singh"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"

from ArduinoScope import scope

def main(args):
    scope.main(args)

if __name__ == '__main__':
    import argparse
    # Argument parser.
    description = '''Arduino NeuroScope.'''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--port', '-p', type=str
            , default = '/dev/ttyACM0'
            , required = False, help = 'Input file'
            )
    parser.add_argument('--baudrate', '-B'
            , required = False, default = 115200
            , help = 'Baudrate of Arduino board.'
            )
    class Args: pass
    args = Args()
    parser.parse_args(namespace=args)
    main(args)
