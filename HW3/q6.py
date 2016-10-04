#!/usr/bin/env python
""" GE 501 HW#3 Question 6

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q6.py [options]

Options:
    -h --help                    Show help
    -t --temp <temp>             Temperature in degrees C (default 52)
    -e --emissivity <emissivity> Spectral emissivity (deafult: .38)
    -w --wave <wave>             Wavelength in micrometers (default: 10)

Question:

    A shiny metal roof is at a temperature of 52 degrees C. The metal roofing has a spectral
        emissivity of .38 at 10 um. What is the temperature of a blacbody in degrees C that emits
        the same amount of energy (W m^-2 um^-1) at 10 um?

Example:

    > python q6.py -t 66

"""

import future
from docopt import docopt
import math
import sys


def main():
    print('')
    if args['--temp']:
        temp = float(args['--temp'])
    else:
        temp = 52

    if args['--wave']:
        wave = float(args['--wave'])
    else:
        wave = 10

    if args['--emissivity']:
        emissivity = float(args['--emissivity'])
    else:
        emissivity = .38

    #To get Kelvin from Celsius:
    TK = temp + 273.15

    print('Solving the Planck equation for temeprature given wavelength and spectral emission gives:')
    print('T = (C2) / (lambda)ln((C1)/(lambda^5*M_lambda) + 1')
    print('')
    print('To get the spectral emissivity of a surface:')
    print('Mroof/(M_lambda = {w}um),(T = {T} K) = {e}'.format(w=wave,T=TK,e=emissivity))
    print('')
    print('(M_lambda = {w}um),(T = {T} K) can be found using the Plancks equation'.format(w=wave,T=TK))
    M = (3.742e8)/(((wave)**5)*(math.exp((1.439e4)/(wave*TK))-1))
    print('(M_lambda = {w}um),(T = {T} K) = (C1) / (lambda^5*(e^((c2/lambda*T))-1))'.format(w=wave,T=TK))
    print('(M_lambda = {w}um),(T = {T} K) = {q} W m^-2 um^-1'.format(w=wave,T=TK,q=M))
    print('')
    print('Thus, the spectral exitance will be:')
    Mroof = emissivity * M
    print('Mroof = {e} * (M_lambda = {w}um),(T = {T} K) = {e} * {w} W m^-2 um^-1 = {m}'.format(e=emissivity,w=wave,T=TK,m=Mroof))
    print('')
    print('To get the temperature associated with this spectral exitance? Substituting the solution of the Planck equation for T with lambda and M_lambda gives:')
    print('T = (C2) / (lambda*ln((C1/lambda^5M_lambda) + 1))')
    T = 1.439e4 / (10*math.log((3.742e8/((10**5)*Mroof)) + 1))
    celc = T - 273.15
    print('T = (1.439 * 10^4) / ({w}*ln(3.742*10^8/(({w}^5)*{r}) + 1)) = {t} K = {c} deg C'.format(w=wave,r=Mroof,t=T,c=celc))

if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
