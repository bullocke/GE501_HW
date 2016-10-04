#!/usr/bin/env python
""" GE 501 HW#3 Question 2

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q2.py [options] (partA | partB)

Options:
    -h --help                   Show help

Question:

    The cosntants used in the Planck equation, Wien's Law, and the Stefan-Boltzman
        equation yield answers in units of watts (W), meters of area(m^2), and meters
        of wavelength (m). However, the plots of blackbody quantities are often
        expressed in different units, as an examination of the graphs in your books and
        the Manual chapter will show.

    A) Convert the constants C1 = 3.742 * 10^-16 W m^2 and C2 = 1.439 * 10^-2 m K in
        the Planck equation so that they yield an exitance in W m^-2 um^-1 rather than
        W m^-2 m^-1 when the input wave-length is entered in micrometers.

    B) Convert the constant in Wien's law to yield an answer in um.

Example:

    > python q2.py partA

"""

import future
from docopt import docopt
import math
import sys

def do_b():
    print('lambda_max = (2.898*10^-3 M K / T) * (10^6 um / 1 m) = (2.898 * 10^3 um K / T')

def do_a():
    print('The Plack equation gives blackbody spectral exitance as:')
    print('Mlambda = (C1)/(lambda^5(e^(C2/lambdaT) - 1))')
    print('C1 = 3.74151 * 10^016 W m^2')
    print('C2 = 1.43879 * 10^-2m K')
    print('Mlambda is in units W m^-2 m^-1 and lambda is in metersu. However, we want to use lambda in units of um instead. since C2/lambdaT must remain unitless, C2 must then be in units of um K, so')
    print('C2 = 1.43879 * 10^-2 m K * (10^6 um / 1 m) = 1.43879 * 10^4 um K')
    print('For C1, we need to have C1/lambda^5 in units of Wm^-2um^-1, so C1 must be in units of Wm^-2um^4.')
    print('C1 = 3.74151 * 10^-16 Wm^2 * (10^24 um^4 / 1m^4) = 3.74151 * 10^8 W m^-2 um^4')

def main():
    if args['partA']:
        do_a()
    else:
        do_b()

if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
