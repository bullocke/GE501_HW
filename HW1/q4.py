#!/usr/bin/env python
""" GE 501 HW#1 Question 4

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q4.y [options]

Options:
    -a --approach <approach>    Approach to answer the problem (1 or 2; see notes)
    -i --inclination <inc>      Alternative inclination angle in degrees (default: 98.21)
    -o --orbit <height>         Alternative orbit height in km (default: 705.3)
    -h --help                   Show help

Question:

    Use the formulas of pp. 700-702 of the Manual of Remote Sensing (Chapter 16) to show that
        the Landsat-7 orbit is sun-synchronous. For Landsat, the orbit height is 705.3 km and
        the inclination angle is 98.21 degrees. (Hint: find the precession rate and shwo that it
        amounts to 360 degrees per year; or use formula 16-9 to show that the nodal day D. is
        exactly equal to a solar day of 86,400 s.)

Example:

    > python q4.py -h 400 -i 35

Note:

    Option 1: Find the length of the orbit's nodal day and compare that to the length of a
        solar day. If they are equal, then the orbit is keeping track with the sun. The nodal
        day is the earth rotation period relative to the orbit plane or node.

    Option 2 Calculate the rate of change of the nodal longitude (or the nodal precession rate)
        and apply that to a solar year. If the orbit is sun-synchronous, it should precess 360
        degrees or 2pi radians in a year.

"""
import future
from docopt import docopt
import math



def do_calc(inc, height, method):
    print('The formula for the rate of change of the nodal longitude in (rad/s):')
    print('omega = (-3/2)*J2*r0^2*sqrt(mu)*(r + hs)**(-7/2)*cos(inc)')
    print('Where:')
    print('J2 is the dimensionless constant 0.00108263')
    J2 = 0.00108263
    print('r0 is the earth radius: 6.378e6')
    r0 = 6.378e6
    print('mu is the earths gravitational constant: 3.98601e14')
    mu = 3.98601e14
    height = height * 1000
    inc_rad = math.radians(inc)
    exp=-float(7)/2
    print('hs is the orbit height: {h}'.format(h=height))
    print('inc in the inclination angle: {i}'.format(i=inc))
    print('')
    print('Substituting Landsats parameters in we get:')
    answer = (-float(3)/2) * J2 * r0**2 * math.sqrt(mu) * (r0 + height)**exp * math.cos(inc_rad)
    print('omega = (-3/2)*{a}*{b}^2*sqrt({c})*({d}+{e})**(-7/2)**cos({f}) = {g} rad/s'.format(a=J2,b=r0,c=mu,d=r0,e=height,f=inc,g=answer))
    print('')
    if method == 2:
        get_nodal_day(inc, height, answer)
    else:
        do_approach_1(inc, height, answer)

def get_nodal_day(inc,height, omega):
    print('From the Manual, we note the relationship between the nodal day, Dn, the sidereal day,')
    print('Ds, and the rotation period of the orbital plane, Tn (formula 16-9):')
    print('1/Dn = 1/Ds - 1/Tn')
    print('')
    print('The rotation period of the orbital plane, Tn, is the time (seconds) required for')
    print('the orbit to precess 360 degrees or 2pi radians:')
    print('Tn = 2pi/omega')
    print('')
    print('The sidereal day is 86,164.2 seconds, and we can solve for Dn:')
    print('1/Dn = 1/Ds - omega/2pi = ')
    sidereal = 86164.1
    answer = (1 / sidereal) - (omega/(2*math.pi))
    print('(1 / 86164.1) - ({n} / 2pi = {a}'.format(n=omega,a=answer))
    answer2 = float(1) / answer
    print('Dn = 1 / {n} = {p} s'.format(n=answer,p=answer2))
    print('')
    print('From Manual formula 16-10 we can find the solar time change per nodal day, deltat,')
    print('from Dn, and D, the length of the solar day (86,400 s) as')
    answer3 = answer2 - 86400
    print('deltat = Dn - D = {n} - 86400 = {d} s'.format(n=answer2,d=answer3))

def do_approach_1(inc,height, omega):
    print('Recall that the alternative approach was to see how many radians the orbit will')
    print('precess in a year and compare that to 2pi. To obtain this value, we multiply the')
    print('nodal precession rate by the number of seconds in a year, noting that a mean solar')
    print('year has 365.242 days')
    print('')
    answer = omega * 60 * 60 * 24 * 365.242
    print('omega_year = {n}/s * 60s/min * 60min/hr * 24hr/day * 365.242day/y = {a}'.format(n=omega,a=answer))
    print('')
    print('...which is the same as the value for 2pi to three decimal places = 6.283')

def main():
    print('')
    print('Question 4')
    print('')

    if args['--orbit']:
        height = float(args['--orbit'])
    else:
        height = 705.3

    if args['--inclination']:
        inc = float(args['--inclination'])
    else:
        inc = 98.21

    if args['--approach']:
        method = int(args['--approach'])
    else:
        method = 2

    do_calc(inc,height,method)


if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
