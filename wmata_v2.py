# The original wmata file wasn't that good. This one will
# leverage argparse library for better user experience

import argparse
from time import strftime, strptime

parser = argparse.ArgumentParser(description='Get metro departure times')

parser.add_argument('start_time', metavar='time', nargs='?', default=strftime('%I:%M'),
    help='The time at which you depart for the metro')
