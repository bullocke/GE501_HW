#!/usr/bin/env python
""" GE 501 HW#3 Question 7

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q7.py [options] (part1 | part2 | part3 | part4 | part5)

Options:
    -h --help                    Show help

Part 1 (part1) Options:
    -t --temp <temp>             Sun's temperature in K (default 5720)
    -w --wave <wave>             Wavelength in micrometers (default: .66)
    -b --bandwidth <bandwidth>   Bandwidth of Landsat spectral band (default: .06)

Part 2 (part2) Options:
    -e --exitance <exitance>     Per-square meter full-band exitance (W m^-2)(No default)

Part 3 (part3) Options:
    -f --flux <flux>            Emitted flux (W) (No default)

Part 5 (part6) Options:
    -s --steradians <steradians> Steradians (No default)
    -i --intensity <intensity>  Radiant intensity of the sun as a point source (No default)

Question:

    Calculate the solar irradiance at the top of the atmosphere in TM bands 3 (.63-.69 um) and 7
        (2.08-2.35 um). Your answer should be in units of W m^-2. FYI the suns radius can be taken
        as 6.957 * 10^8 m. As per Slater, consider the suns temeprature at 5720 K for band 3 and
        6000 K for band 7. You may also use 1 au as the earth-sun distance, 1.496 * 10^11 m. Here
        are the steps to follow:

    1. Use the Planck equation to find the spectral exitance of the sun's surface at the center of
        each band (W m^-2 um^-1), then multiply by the bandwidth (um) to give per-square-meter full-
        band exitance W m^-2

    2. Find the surface area of the sun (m^2) and multiply that by the per-square-meter full-band
        exitance (W m^-2) in each band to give the total radiation flux (W) emitted by the sun
        into all directions in that band.

    3. Divide the emitted flux (W) by the 4pi steradians in a sphere to give the radiant intensity
        of the sun as a point source (W sr^-1).

    4. Find how many steradians are associated with a one-meter square area situated at the earth-sun
        distance of 1 au.

    5. Multiply this value (sr) by the radiant intensity of the sun (W sr^-1) to give watts falling
        on the one-square meter area (W m^-2), which will be the top-of-atmosphere irradiance in
        the landsat TM band.

Example:

    > python q7.py -w 2.215 -t 6000 part1

"""

import future
from docopt import docopt
import math
import sys

def do_planck(TK,wave):
    M = (3.742e8)/(((wave)**5)*(math.exp((1.439e4)/(wave*TK))-1))
    return M


def do_part2(ex):
    print('The surface area of a sphere is A = 4(pi)(r)^2')
    print('A = 4(pi)(6.957e8)^2 = 6.08e18 m^2')
    area = 6.08e18
    flux = area * ex
    print('The total emittance is {f} W'.format(f=flux))

def do_part1(temp,wave,bw):
    exitance = do_planck(temp,wave)
    print('For the solar blackbody temperature of {t} and wavelength {w} the Planck equation gives a spectral exitance of {m}'.format(t=temp,w=wave,m=exitance))
    print('')
    full_ex = exitance * bw
    print('Multiplying by the bandwidth of {b} you get the per-square-meter full band exitance:'.format(b=bw))
    print('{m} * {b} = {q} W m^-2'.format(m=exitance,b=bw,q=full_ex))

def do_part3(flux):
    intensity = flux / (4*math.pi)
    print('{f} / 4pi = {i} W sr^-1'.format(f=flux,i=intensity))


def do_part4():
    print('omega = A/r^2 = 1 / (1.496*10^11)^2 = 4.47 * 10^-23 wr m^-2')

def do_part5(steradians, intensity):
    top_ir = steradians * intensity
    print('Applying the factor of {s} sr m^-2 to {i} W sr^-1 we get {t} W m^-2'.format(s=steradians,i=intensity,t=top_ir))


def main():
    print('')
    if args['--temp']:
        temp = float(args['--temp'])
    else:
        temp = 5720

    if args['--wave']:
        wave = float(args['--wave'])
    else:
        wave = .66

    if args['--exitance']:
        ex = float(args['--exitance'])
    else:
        if args['part2']:
            print('Must specify a per-square-meter full band exitance')
            sys.exit(1)

    if args['--flux']:
        flux = float(args['--flux'])
    else:
        if args['part3']:
            print('Must specify a emitted flux (W)')
            sys.exit(1)

    if args['--steradians']:
        steradians = float(args['--steradians'])
    else:
        if args['part5']:
            print('Must specify steradians')
            sys.exit(1)

    if args['--intensity']:
        intensity = float(args['--intensity'])
    else:
        if args['part5']:
            print('Must specify band-specific radiant intesity of the sun')
            sys.exit(1)

    if args['--bandwidth']:
        bw = float(args['--bandwidth'])
    else:
        bw = .06

    if args['part1']:
        do_part1(temp,wave,bw)
    elif args['part2']:
        do_part2(ex)
    elif args['part3']:
        do_part3(flux)
    elif args['part4']:
        do_part4()
    elif args['part5']:
        do_part5(steradians, intensity)

if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
