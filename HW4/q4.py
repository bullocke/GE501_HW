#!/usr/bin/env python
""" GE 501 HW#4 Question 4

    Author: Eric Bullock
    Date: October 2016
    Version: 1.1

Usage:
    q4.py [options] <TOA> <reflectance> <tau>

Options:
    -h --help                   Show help
    --zenith <zenith>           Solar zenith angle (default: 27)
    --angle <angle>             Satellite zenith angle (default: 12)
    <TOA>                       Top of atmosphere irradiance
    <reflectance>               Surface reflectance


Question:

    A satellite sesnor collects radiation in TM bands 3 and 4. At the same measurement, the sun is at
        63 degres above the horizon (solar zenith angle 27 degrees), and the sensor images at the edge
        of its scan with an angle 12 degrees away from nadir. A Lambertian surface (iso-tropic reflector)
        with a reflectance of 0.10 is imaged. Analysis of sun photometer data provides measurements
        of tau = 0.12 and 0.08 in the two bands, respectively. Considering only attenuation of beam radiation,
        what is the top-of-atmosphere NDVI of the surface calculated from TOA radiances? What is the
        NDVI if the surface reflectance is .70?

Example:

    > python q4.py 87.7 .1 .12

"""

import future
from docopt import docopt
import math
import sys


def main():
    #Options
    if args['--zenith']:
        zen = int(args['--zenith'])
    else:
        zen = 27

    if args['--angle']:
        ang = int(args['--angle'])
    else:
        ang = 12

    TOA = float(args['<TOA>'])
    ref = float(args['<reflectance>'])
    tau = float(args['<tau>'])
    LTOA = get_TOA(zen, ang, TOA, ref, tau)

def get_TOA(zen, ang, TOA, ref, tau):
    print('We can use the formula from class:')
    print('LTOA = (1 / pi)(R * ETOA * cos(theta1) * e^(-tau(sec(theta1) + sec(theta2)))')
    print('With:')
    print('theta1 = {n}'.format(n=zen))
    print('theta2 = {n}'.format(n=ang))
    print('ETOA = {n}'.format(n=TOA))
    print('R = {n}'.format(n=ref))
    print('tau = {n}'.format(n=tau))
    LTOA = (1 / math.pi) * (ref * TOA * math.cos(math.radians(zen)) * math.exp(-tau*((1/math.cos(math.radians(zen))) + (1/math.cos(math.radians(ang))))))
    print('LTOA = {n}'.format(n=LTOA))
    print('Now plug LTOA for the NIR and Red bands in to the NDVI formula:')
    print('NDVI = (NIR - Red) / (NIR + Red)')
    return LTOA

if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
