#!/usr/bin/env python
""" GE 501 HW#3 Question 4

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q4.py [options] <wavelength>

Options:
    -h --help                   Show help
    <wavelength>                Wavelength to return ratios for

Question:

    Assume the surface of the sun is a blackbody at 6000 K. What are the ratios of solar energy emitted
        at .55, .65, .75, and .95 um to the solar energy flux at its lambda_max?

Example:

    > python q4.py .55

"""

import future
from docopt import docopt
import math
import sys


def main():
    wave = float(args['<wavelength>'])
    print('From Wiens law, lambda_max = .483 um, and the Planck equation evaluates to:')
    print('M_lambda_max = (3.784 * 10^8) / ((.483^5)(e^((1.44 * 10^4)/(.483 * 6000)) - 1))')
    print('M_lambda_max = 1.00 * 10^8 W m^-2 um ^-1')
    print('Note: with the (near) even result, which is coincidental, makes the ratio easy to find!')
    h = 6.626e-34
    #h = 1
    c = 3e8
    k = 1.3806503e-23
    T = 6000
    c1 = 3.74e8
    c2 = 1.44e4
    energy =  (c1) / (((wave**5))*((math.exp((c2) / (wave*T))-1)))
    print('M_lambda {w} = (3.784 * 10^8) / (({w}^5)(e^((1.44 * 10^4)/({w} * 6000)) - 1))'.format(w=wave))
    print('M_lambda {w} = {e} W m^-2 um^-1 = {e} M lamda_max'.format(w=wave,e=energy))

if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
