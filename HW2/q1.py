#!/usr/bin/env python
""" GE 501 HW#2 Question 1

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q1.py [options]

Options:
    -h --help                   Show help
    -l --latitude <latitude>    Point of latitude (default: 42.15N)
    -o --longitude <longitude>  Point of longitude (default: 71.07W)
Question:

    You wish to make a measurement of beam and diffuse radiance using a radiometer with the
        sun in its highest position in the sky on September 22, 2016 here in Beantown
        (42.15 N 71.07 W). At what time (EDT) will you make your measurement? Considering
        that September 22 is the equinox, what will the solar zenith angle be *there
        is an easy answer for equinox conditions...)?

Example:

    > python q1.py -l 24.3S -o 65.10W

"""

import future
from docopt import docopt
import math
import sys

def get_time(longitude, latitude):
    TZ = 4
    print('The time zone is +5. However, daylight savings time is observed, so TZ = +4')

    if longitude[-1] == 'W' or longitude[-1] == 'E':
        long_int = float(longitude[:-1])
    else:
        print('Please specify E or W for longitude')
        sys.exit(1)
    if longitude[-1] == 'W':
        long_int *= -1
    print('')
    print('When the sun is at its highest position, the subsolar point will lie on the longitude meridian of {n}. That is, the solar longitude (SL) will be {l}'.format(n=longitude,l=long_int))
    print('')
    print('We can solve the formula SL = (ET - LT -TZ)*15 for LT:')
    print('LT = ET - TZ - (SL/15)')
    ET_hour = 11
    ET_min = 52
    ET_sec = 31.88
    print('')
    print('According to the Astronomical Almanac for 2016, ephemeris transit on 9/22/2016 is 11h 52m 31.88s')
    print('Filling in the variables, we get:')
    LT = ET_hour + (float(ET_min)/60) + (float(ET_sec)/3600) - TZ - (float(long_int) / 15)
    print('LT = {h} + {m}/60 + {s}/3600 - {t} - ({l}/15) = {q}'.format(h=ET_hour,m=ET_min,s=ET_sec,t=TZ,l=long_int,q=LT))
    print('')
    _hf1 = float(LT) % 1)
    hf1 = _hf1 * 60
    _hf2 = float(hf1 % 1)
    hf2 = _hf2 * 60
    hf0 = int(LT)
    print('Converting the hour fraction {f} to minutes and seconds:'.format(f=hf1))
    print('{h} * 60 = {m} minutes'.format(h=_hf1,m=hf1))
    print('{h} * 60 = {s} seconds'.format(h=_hf2,s=hf2))
    hf2 = int(hf2)
    hf1 = int(hf1)
    print('...and we get: {h}:{m}:{s} EDT'.format(h=hf0,m=hf1,s=hf2))
    print('')

def get_solar_zenith(longitude, latitude):
    print('For the solar zenith angle, we can note that on the equinox, the solar zenith angle at noon equals the latitude, or {l}. This follows from the formula for theta_sun with delta = 0 and omega = lambda).'.format(l=latitude))
    print('cos(theta_sun) = sin(delta)sin(beta) + cos(delta)cos(beta)cos(omega - lambda)')
    print('cos(theta_sun) = sin(0)sin(beta) + cos(0)cos(beta)cos(0)')
    print('cos(theta_sun) = 0 * sin(beta) + 1 * cos(beta) * 1')
    print('cos(theta_sun) = cos(beta)')

def main():
    if args['--longitude']:
        longitude = args['--longitude']
    else:
        longitude = '71.07W'

    if args['--latitude']:
        latitude = args['--latitude']
    else:
        latitude = '42.15N'

    get_time(longitude, latitude)

    get_solar_zenith(longitude, latitude)

if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
