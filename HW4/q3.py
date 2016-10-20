#!/usr/bin/env python
""" GE 501 HW#4 Question 3

    Author: Eric Bullock
    Date: October 2016
    Version: 1.1

Usage:
    q3.py [options] <wavelength> <TOA>

Options:
    -h --help                   Show help
    <wavelength>                Wavelength at band center
    <TOA>                       Top-of-atmosphere irradiance


Question:

    Using formula (2) in Kaufmann's chapter in Asrar, calculate the Rayleigh optical depth, and vertical path
        transmission of the atmosphere at the centers of the TM bands above. Then apply the transmissivity to
        the TOA irradiance in each band to give the bottom-of-atmosphere (BOA) in-band vertical irradiance for
        a Rayleigh atmosphere

Example:

    > python q3.py .485 145.2

"""

import future
from docopt import docopt
import math
import sys


def main():
    #Options
    wave = float(args['<wavelength>'])
    TOA = float(args['<TOA>'])

    opt = get_opt(wave)
    print('For a standard surface pressure of P = 1013.25 mbar, our equation for optical thickness is:')
    print('tau = (.008569 * lambda**-4) * (1 + (.0113 * lambda**-2) + (.00013 * lambda**-4))')
    print('tau(lambda = {n}) = {q}'.format(n=wave,q=opt))
    print('')
    trans = get_trans(opt)
    print('Transmittance = e**-tau')
    print('Transmittance(lambda = {n}) = {q}'.format(n=wave,q=trans))
    BOA = get_BOA(trans,TOA)
    print('BOA = TOA * Tr = {a} * {b} = {c} W m^-2'.format(a = TOA, b = trans, c = BOA))

def get_BOA(trans, TOA):
    BOA = trans * TOA
    return BOA


def get_opt(wave):
    opt = (.008569 * wave**-4) * (1 + (.0113 * wave**-2) + (.00013 * wave**-4))
    return opt

def get_trans(opt):
    trans = math.exp(-opt)
    return trans


if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
