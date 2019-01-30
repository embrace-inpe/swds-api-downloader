#!/usr/bin/env python
import getopt
import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "s:", ['source='])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        sys.exit(2)
    source = 'src'
    for opt, arg in opts:
        if opt in ("-s", "--source"):
            source = arg
        else:
            assert False, "unhandled option"
    os.system('coverage run --source="{}" -m unittest discover'.format(source))
    os.system('coverage report')
    sys.exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])

