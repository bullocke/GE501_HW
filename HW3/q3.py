#!/usr/bin/env python
""" GE 501 HW#3 Question 3

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q3.py [options] <temp>

Options:
    -h --help                   Show help

Question:

    Fill in the blanks in the table below for radiation from a blackbody at the spefied
        temperatures.

Example:

    > python q3.py 250

"""

import future
from docopt import docopt
import math
import sys


def main():
    temp = int(args['<temp>'])
    wien = float(2898)/temp
    print('From Wiens Law, lambda_max = 2898/T = 2898/{t} = {k} um'.format(t=temp,k=wien))
    ex = 5.67e-8 * temp**4
    print('')
    print('From the Stefan-Boltzman equation:')
    print('M = sigma*T^4 = 5.67 * 10^-8 W m^-2 K^-4 * {t}**4 = {q} W m^-2'.format(t=temp,q=ex))


if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
