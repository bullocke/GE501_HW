#!/usr/bin/env python
""" GE 501 HW#4 Question 1

    Author: Eric Bullock
    Date: October 2016
    Version: 1.1

Usage:
    q1.py [options] <wavelength>

Options:
    -h --help                   Show help
    <wavelength>              Wavelength


Question:

    Using formula (2) in Kaufmann's chapter in Asrar, calculate and plot (A) the Rayleigh optical depth; and (B)
        the vertical path transmission T, of the atmosphere for wavelengths from .2-1.0 um. Do the calculation for
        15-20 points.

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

    opt = get_opt(wave)
    print('For a standard surface pressure of P = 1013.25 mbar, our equation for optical thickness is:')
    print('tau = (.008569 * lambda**-4) * (1 + (.0113 * lambda**-2) + (.00013 * lambda**-4))')
    print('tau(lambda = {n}) = {q}'.format(n=wave,q=opt))
    print('')
    trans = get_trans(opt)
    print('Transmittance = e**-tau')
    print('Transmittance(lambda = {n}) = {q}'.format(n=wave,q=trans))

def get_opt(wave):
    opt = (.008569 * wave**-4) * (1 + (.0113 * wave**-2) + (.00013 * wave**-4))
    return opt

def get_trans(opt):
    trans = math.exp(-opt)
    return trans

if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
