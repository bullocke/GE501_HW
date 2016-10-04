#!/usr/bin/env python
""" GE 501 HW#2 Question 2

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q2.py [options]

Options:
    -h --help                   Show help
    -t --time <time>            Time in UT (default: 18.00)
Question:

    Where on the Earth (latitude and longitude, in degrees, minutes, seconds) would you need
        to stand for the sun to be directly above you at 1800 UT on November 15, 2016? Can
        you actually stand on dry ground at this location, or will you need a boat?

Example:

    > python q2.py -t 16.50

"""

import future
from docopt import docopt
import math
import sys

def get_location(UT):
    print('The solution is the subsolar point.')
    print('The latitude of the subsolar point is the apparent declination')
    app = '-18 deg 31 min 53.8 sec'
    print('According to the Astronomical Almanac, the apparent declination for this date is {a}'.format(a=app))
    print('')
    print('To find the longitude, we need the ephemeris transit time...')
    ET_h = 11
    ET_m = 44
    ET_s = 39.52

    #2011:
    #ET_h = 11
    #ET_m = 44
    #ET_s = 31.34
    hours = ET_h + (float(ET_m)/60) + (float(ET_s)/3600)
    print('For 15 November 2016, the ET = {h} h {m} m {s} s = {q} hours'.format(h=ET_h, m=ET_m, s=ET_s, q=hours))
    print('')
    print('Thus, Solar Longitude = (ET - UT) * 15')
    print('SL = ({e} - {u}) * 15'.format(e=hours,u=UT))
    SL = (hours - UT) * 15
    _sl_min = abs(SL) % 1
    sl_min = (_sl_min) * 60
    _sl_sec = (sl_min % 1)
    sl_sec = _sl_sec * 60
    sl_h = int(SL)
    sl_min = int(sl_min)
    sl_sec = round(sl_sec,2)
    print('SL = {s} or {h} deg {m} min {q} sec '.format(s=SL,h=sl_h,m=sl_min,q=sl_sec))
    print('Since this is off the coast of Peru, you would need a boat!')

def main():
    if args['--time']:
        UT = args['--time']
    else:
        UT = 18.00

    get_location(UT)

if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
