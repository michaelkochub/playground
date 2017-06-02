import requests as req
from datetime import datetime as dt
from time import strftime, strptime
import sys
from re import match

def validate_time(t):
    regex = r'^([0-9]{1,2}:?[0-9]{2}|[0-9]{1,2})$'
    if not match(regex, t):
        return False

    time_data = t.split(':')
    hrs = time_data[0]
    mins = '0' if len(time_data) < 2 else time_data[1]

    if ':' in t:
        return t.split(':')
    else:
        if len(t) in (1, 2):
            hrs, mins = t, 0
        elif len(t) == 3:
            hrs, mins = t[0], t[1:]
        else:
            hrs, mins = t[:2], t[2:]

    # api will error if minute value is single digit
    return hrs, mins.zfill(2)



def get_data(use_args=True):
    # base uri
    url = 'https://www.wmata.com/node/wmata/wmataAPI/tripPlanner'

    # query params
    location = 'greensboro metro station'
    destination = 'wiehle-reston east metro station'

    travelby = 'R' # Rail
    arrdep = 'D' # Departure
    route = 'T' # Don't know
    period_leaving = 'PM'
    walk_distance = '1'

    now = dt.now()

    use_cmnd_arg = use_args and len(sys.argv) > 1
    time = ()

    # If command line argument is not given (or is bad format), use current time
    if use_cmnd_arg:
        time = validate_time(sys.argv[1])

    if not (use_cmnd_arg and time):
        time = strftime("%I:%M").split(':')
        period_leaving = strftime("%p")

    hour_leaving = time[0]
    minute_leaving = time[1]

    day_leaving = now.day
    month_leaving = now.month

    params = {
        'location': location,
        'destination': destination,
        'travelby': travelby,
        'arrdep': arrdep,
        'route': route,
        'minute-leaving': minute_leaving,
        'hour-leaving': hour_leaving,
        'day-leaving': day_leaving,
        'month-leaving': month_leaving,
        'period-leaving': period_leaving,
        'walk-distance': walk_distance
        }

    resp = {}

    try:
        resp = req.get(url, params=params)
    except req.exceptions.ConnectionError:
        # Sometimes Requests fails to establish a connection
        # so just retry the GET call
        resp = req.get(url, params=params)

    return resp.json()

def output_data(trips):
    times = []

    # Times are in military time, we want them
    # in 12-hour format
    from_format = "%H%M"
    to_format = "%I:%M %p"

    for i in range(1, 4):
        data = trips['Plantrip{}'.format(i)]['Itin']['Legs']['Leg']
        # Just in case time is like 230, left zero-pad it to 0230
        # Otherwise 230 would be interpreted to 11:00 (23 -> H and 0 -> M)
        start = data['Ontime'].zfill(4)
        end = data['Offtime'].zfill(4)
        times.append((dt.strptime(start, from_format), dt.strptime(end, from_format)))

    for t1,t2 in times:
        print("{} -> {}".format(t1.strftime(to_format), t2.strftime(to_format)))

def main():
    resp = {}
    trips = {}

    resp = get_data()
    # the json response returned is something like { "Error": { ... } }
    # which is usually caused by bad values in the query params
    # such as hour_leaving = 57 or one-character minute_leaving
    if not('Response' in resp and 'Plantrip' in resp['Response']):
        resp = get_data(use_args=False)
    trips = resp['Response']['Plantrip']

    output_data(trips)

if __name__ == '__main__':
    main()
