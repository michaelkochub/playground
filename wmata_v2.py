# The original wmata file wasn't that good. This one will
# leverage argparse library for better user experience

import argparse
from time import strftime, strptime
from datetime import datetime

def valid_time(time):
    valid_formats = '%H%M', '%H:%M', '%H'
    try:
        for format in valid_formats:
            datetime.strptime(time, format)
    except ValueError:
        raise argparse.ArgumentTypeError('{} is not a valid time'.format(time))
    return time

parser = argparse.ArgumentParser(description='Get metro train departure times')

parser.add_argument('start_time', metavar='time', nargs='?', default=strftime('%I:%M'),
    type=valid_time, help='The time at which you depart for the metro')

args = parser.parse_args()
print(args.start_time)
