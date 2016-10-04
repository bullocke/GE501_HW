#!/usr/bin/env python
""" GE 501 HW#1 Question 1

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q1.py [options]

Options:
    -h --help                   Show help
    -o --orbit <orbit>          Satellite orbit in km (default 833)
Question:

    NOAA's POESS (Polar Orbiting Environmental Satellite System) platforms, which include
        the AVHRR sensor, have a sun-synchronous orbit with a height of 833 km (<orbit>).
        Find the angular speed theta associated with this orbit and the orbital period in
        minutes.

Example:

    > python q1.py -o 833

"""

import future
from docopt import docopt
import math

#Logging

def get_r(oheight):
    rs = 6.378e6
    print('')
    print('NOTE: The radius of the sun is: 6.378 x 10^6')
    answer = rs + oheight
    print('')
    print('r = r0 + hs = 6.378 x 10^6 + {n} = {k}'.format(n=oheight, k=answer))
    return answer

def get_theta(r):
    mu = 3.986e14
    answer = math.sqrt(mu/r**3)
    print('')
    print('theta = sqrt(mu/r^3) = sqrt({n}/{l}) = {a} rad s^-1'.format(n=mu,l=r,a=answer))
    return answer

def get_t(theta):
    answer = (2*math.pi)/theta
    minutes = answer/60
    minutes = round(minutes,1)
    print('')
    print('T = 2pi/theta = {n} seconds = {m} minutes'.format(n=answer, m=minutes))
    print('')

def main():
    print('')
    print('Question 1')
    print('')
    if args['--orbit']:
        oheight = int(args['--orbit']) * 1000
    else:
        oheight = 833 * 1000

    r = get_r(oheight)

    theta = get_theta(r)

    get_t(theta)

if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
