import requests as req
from datetime import datetime as dt
from time import strftime, strptime
import sys
from re import match

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

    regex = r'^([0-9]{1,2}:?[0-9]{2}|[0-9]{1,2})$'
    use_cmnd_arg = use_args and len(sys.argv) > 1 and match(regex, sys.argv[1])

    # If command line argument is not given (or is bad format), use current time
    if use_cmnd_arg:
        time_data = sys.argv[1]
        num = len(time_data)
        time = time_data.split(':')
        if len(time) < 2:
            if num > 2:
                time_data = time_data.zfill(4) # could use rjust(4, '0')
            else:
                if num == 1:
                    time_data = time_data.rjust(2, '0')
                time_data = time_data.ljust(4, '0')
            time = [time_data[:2], time_data[2:]]
    else:
        time = strftime("%I:%M").split(':')

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

    # try:
    #     resp = get_data()
    #     trips = resp['Response']['Plantrip']
    # except KeyError:
    #     # the json response returned is something like { "Error": { ... } }
    #     # which is usually caused by bad values in the query params
    #     # such as hour_leaving = 57
    #     resp = get_data(use_args=False)
    #     trips = resp['Response']['Plantrip']

    # Better approach
    resp = get_data()
    if not('Response' in resp and 'Plantrip' in resp['Response']):
        resp = get_data(use_args=False)
    trips = resp['Response']['Plantrip']

    output_data(trips)

if __name__ == '__main__':
    main()
