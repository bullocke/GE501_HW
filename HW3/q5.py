#!/usr/bin/env python
""" GE 501 HW#3 Question 5

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q5.py [options]

Options:
    -h --help                   Show help
    -w --wave <wave>            Wavelength (default 3.0)

Question:

    Assume the surface of the sun is a blackbody at 6000 K. What are the ratios of solar energy emitted
        at .55, .65, .75, and .95 um to the solar energy flux at its lambda_max?

Example:

    > python q5.py -w .65

"""

import future
from docopt import docopt
import math
import sys


def main():
    print('')
    if args['--wave']:
        wave = float(args['--wave'])
    else:
        wave = 3.0
    wien = 2898/3.0

    print('From Wiens Law, lambda_max = 2898/T, so T = 2909/lambda_max and T = 2898/{w} = {k} K'.format(w=wave,k=wien))
    print('')
    print('From the Stefan-Boltzman equation, the total exitance from the burning surface is:')
    M = 5.67e-8 * wien**4
    print('M = sigmaT^4 = (5.67 * 10^-8 W m^-2 K^-4) * ({w})^4 = {m} W m^-2'.format(w=wien,m=M))

if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
