#!/usr/bin/env python
""" GE 501 HW#1 Question 3

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q3.y [options]

Options:
    -o --orbit <orbit>          Orbit height of TRMM in km (default: 403.5)
    -i --inclination <inc>      Orbital inclination in degrees (default: 35)
    -g --gravity <gravity>      Alternative gravitational constant (default: 3.986e14)
    -h --help                   Show help

Question:

    The Tropical Rainfall Measurement Mission platform is in an Earth orbit at a height of
        403.5 km that is inclined at 35.0 degrees. What is the orbital period of the platform
        in minutes? Given the inclination angle, what is the precession rate of the nodal longitude
        of the orbit in degrees per day? Is the orbit prograde or retrograde?

Example:

    > python q3.py -o 403.5 -i 35

Note:

    The options are simply for seeing the effect of changing the variables.

"""
import future
from docopt import docopt
import math

def get_radius(orbit):
    orbitm = orbit*1000
    print('')
    print('To find the orbital radius: r = rearth + hs')
    answer = 6.378e6 + orbitm
    print('6.378e6 + {n} = {p}'.format(n=orbitm,p=answer))
    print('')
    return answer

def get_t(r, mu):
    print('Here we can use the formula for the orbital period (MRS 16-4, p. 700):')
    print('T = (2*pi)*(sqrt(r^3/mu))')
    print('')
    answer = (2*math.pi)*(math.sqrt(r**3/mu))
    answer_m = float(answer) / 60
    print('(6.283)*[({n}**3)/{m}]^1/2 = {a} s = {q} minutes'.format(n=r,m=mu,a=answer,q=answer_m))
    print('')
    return answer

def get_precession(r, r0, mu, hs, inc):
    exp=-float(7)/2
    J2 = float(.00108263)
    inc_rad = math.radians(inc)
    print('To find the precession rate, we use formula 16-6 (p. 701):')
    print('omega = (-3/2)*J2*r0^2*sqrt(mu)*(r + hs)**(-7/2)*cos(inc)')
    answer = (-float(3)/2) * J2 * r0**2 * math.sqrt(mu) * (r + hs)**exp * math.cos(inc_rad)
    print('omega = (-3/2)*{a}*{b}^2*sqrt({c})*({d}+{e})**(-7/2)**cos({f}) = {g} rad/s'.format(a=J2,b=r0,c=mu,d=r,e=hs,f=inc,g=answer))
    print('')
    answer_rad = answer * (float(180)/math.pi) * (24 * 60 * 60)
    print('To convert to degrees to day:')
    print('omega_deg = {a}(rad/s) * (180 deg/pi rad) * (24 * 60 * 60 s)/(1 day) = {b} deg/day'.format(a=answer,b=answer_rad))
    if answer_rad < 0:
        orbit_type = 'prograde'
    else:
        orbit_type = 'retrograde'
    print('')
    print('From the direction of the sign, the orbit is {n}'.format(n=orbit_type))

def main():
    print('')
    print('Question 3')
    print('')

    if args['--orbit']:
        orbit = float(args['--orbit'])
    else:
        orbit = 403.5


    if args['--inclination']:
        inc = float(args['--inclination'])
    else:
        inc = 35

    if args['--gravity']:
        gravity = float(args['--gravity'])
    else:
        gravity = 3.986e14

    r0 = 6.378e6
    r = get_radius(orbit)

    t = get_t(r, gravity)

    omega = get_precession(r,r0, gravity, orbit, inc)

if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
