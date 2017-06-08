# The original wmata file wasn't that good. This one will
# leverage argparse library for better user experience

import argparse
from datetime import datetime

def valid_time(time):
    valid_formats = ('%I%M', '%I:%M') if len(time) > 2 else ('%I',)
    target_format = '%I%M'
    datetime_obj = None

    for format in valid_formats:
        try:
            datetime_obj = datetime.strptime(time, format)
            break
        except ValueError:
            pass

    if not datetime_obj:
        raise argparse.ArgumentTypeError('{} is not a valid time'.format(time))

    return datetime_obj.strftime(target_format)

parser = argparse.ArgumentParser(description='Get metro train departure times')

parser.add_argument('start_time', metavar='time', nargs='?', default=datetime.now().strftime('%I%M'),
    type=valid_time, help='Leave at time')

parser.add_argument('-a', '--am', dest='period', action='store_const', const='am',
    default='pm', help='specify AM (default is PM)')

args = parser.parse_args()
print(args.start_time, args.period)
