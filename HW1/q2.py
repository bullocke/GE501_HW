#!/usr/bin/env python
""" GE 501 HW#1 Question 2

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q2.py [options]

Options:
    -r --radius <radius>        Alternative radius for earth (default: 6.378e6)
    -g --gravity <gravity>      Alternative gravitational force of earth (default: 9.799 m/s^2)
    -h --help                   Show help
    -s --sidereal               Seconds for Earth to rotate once around axis (default 86164.1)

Question:

    Mars is a planet with about one-tenth the Earth's mass; a radius about half of that of
        Earth; and an axial rotation rate about the same rate as the Earth. Assuming then that
        the radius of Mars (rmars) is r0/2; that the gravitational constant for Mars is:
        mu_mars = (gearth / 10)*rmars^2; and that the Martian sidereal is Ds, find the altitude
        of a Martian geostationary orbiter.

Example:

    > python q2.py -g 6.5

Note:
    The options are simply for seeing the effect of changing the variables.

"""
import future
from docopt import docopt
import math

def get_rmars(radius):
    answer = radius / 2
    print('')
    print('The radius of Mars is {n} m'.format(n=answer))
    print('')
    return answer

def get_mu(gravity, rmars):
    answer = (gravity/10) * rmars**2
    print('')
    print('mu_mars = (gearth/10) * rmars^2 = ({n}/10)*({m})^2 = {p}'.format(n=gravity, m=rmars, p=answer))
    print('')
    return answer

def get_h24(mu_mars, rmars, Ds):
    print('')
    print('Manual chapter 16 (formula 16-5 p. 700): h24 = [mu_mars*(Ds/2pi)^2]^1/3 - rmars')
    print('')
    exp = float(1)/3
    answer = float(mu_mars * (Ds / (2*math.pi))**2)**exp - rmars
    print('[({n})*({m}/2pi)**2]**1/3 - {p} = {q} m'.format(n=mu_mars, m=Ds,p=rmars, q=answer))

def main():
    print('')
    print('Question 2')
    print('')

    if args['--gravity']:
        gravity = float(args['--gravity'])
    else:
        gravity = 9.799


    if args['--radius']:
        radius = float(args['--radius'])
    else:
        radius = 6.378e6

    if args['--sidereal']:
        sidereal = float(args['--sidereal'])
    else:
        sidereal = 86164.1

    rmars = get_rmars(radius)

    mu_mars = get_mu(gravity, rmars)

    h24 = get_h24(mu_mars, rmars, sidereal)


if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
