#!/usr/bin/env python
""" GE 501 HW#4 Question 2

    Author: Eric Bullock
    Date: October 2016
    Version: 1.1

Usage:
    q1.py [options] <wavelength> <solar_temp> <band_width>

Options:
    -h --help                   Show help
    --<wavelength>              Wavelength at band center
    --<solar_temp>              Solar temperature at given a wavelength
    --<band_width>              Band width


Question:

    Find the top-of-atmosphere (TOA) irradiance for the six TM bands as indicated below, using
        Planck temperatures as shown.

Example:

    > python q1.py .485

"""

import future
from docopt import docopt
import math
import sys


def main():
    #Options
    wave = float(args['<wavelength>'])
    temp = float(args['<solar_temp>'])
    width = float(args['<band_width>'])

    #Define variables
    sun_diameter = 1.3914e9
    sun_distance = 1.496e11

    F = (sun_diameter / 2)**2 / (sun_distance)**2
    print('F = r^2/R^2 = 1.3914e9^2/1.496e11^2 = {n}'.format(n=F))
    print('')
    print('Now applying the Planck equation for solar temperatures and the factor F:')
    print('')
    M = do_planck(temp,wave)
    print('Band Center Exitance from sun: {n} w m^-2 um^-1'.format(n=M))
    ex = inband_ex(width, M)
    print('')
    print('Multiplying by band width we get:')
    print('In-Band Exitance from sun: {n} W m^-2'.format(n=ex))
    print('')
    print('With the factor F we get:')
    TOA = get_TOA(F, ex)
    print('TOA Irradiance = {n} W m^-2'.format(n=TOA))

def get_TOA(F, ex):
    TOA = F * ex
    return TOA

def inband_ex(width, M):
    ex = width * M
    return ex

def do_planck(TK,wave):
    M = (3.742e8)/(((wave)**5)*(math.exp((1.439e4)/(wave*TK))-1))
    return M

if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
