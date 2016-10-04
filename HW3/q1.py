#!/usr/bin/env python
""" GE 501 HW#3 Question 1

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q1.py [options] <wavelength>

Options:
    -h --help                   Show help
    <wavelength>                Wavelength to calculate photon energy

Notes:
    This code returns the photon energy at a specified wavelength. Each wavelength must be
        computed to complete the question.

Question:

    A) Calculate the energy in a photon at the center of each Landsat TM waveband.
    B) Silicon detectors are effective at wavelengths between 0.3 and 1.05 um. What is
       the range of photo energies to which silicon detectors will respond.

Example:

    > python q1.py .485

"""

import future
from docopt import docopt
import math
import sys


def main():
    wave = float(args['<wavelength>']) * 10**-6
    print('Plancks Law for the energy contained with a photon is E = hf = h(c/lambda)')
    print('h = 6.626 * 10^-34 Js')
    print('c - 3.00 * 10^8 m/s')
    en = (6.628e-34)*(3e8/wave)
    print('E = {e} J'.format(e=en))

if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
