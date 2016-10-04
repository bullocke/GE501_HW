#!/usr/bin/env python
""" GE 501 HW#2 Question 3

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q3.py [options]

Options:
    -h --help                   Show help
    -t --time <time>            Time in EST (default 15.00 or 3 PM)
Question:

    You are trying to measure the directly transmitted solar irradiance while ona field in
        Indianapolis, Indiana. However it turns out ot be a compeltely cloudy day and you
        cannot even see the sun. So, you decide to make a measurement of the downwelling
        radiance while pointing your instrument at the location in the sky where you think
        the sun should be. It is now 3:00 PM local time on October 15, 2016. At what solar
        zenith angle and compass azimuth angle would you expect the sun to be?

Example:

    To solve the problem at 4:30 PM local time:
    > python q3.py -t 16.50

"""

import future
from docopt import docopt
import math
import sys

def get_solar_longitude(ET,EST,TZ):
    omega = (ET - EST - TZ) * 15
    return omega

def get_zenith(delta, beta, omega, _lambda):
    cos_theta_sun = (math.sin(math.radians(delta))*(math.sin(math.radians(beta)))) + (math.cos(math.radians(delta))*math.cos(math.radians(beta))*math.cos(math.radians(omega) - math.radians(_lambda)))
    theta_sun = math.acos(cos_theta_sun)
    theta_deg = math.degrees(theta_sun)
    _t_min = abs(theta_deg) % 1
    t_min = _t_min * 60
    _t_sec = abs(t_min) % 1
    t_min = int(t_min)
    t_sec = round(_t_sec * 60,2)
    print('')
    print('Given the above information, the solar zenith angle of the sun is (make sure to convert degrees to radians!):')
    print('cos_theta_sun = sin(delta)sin(beta) + cos(delta)cos(beta)cos(omega - lambda)')
    print('cos_theta_sun = sin({d})sin({b}) + cos({d})cos({b})cos({o} - {l})'.format(d=delta,b=beta,o=omega,l=_lambda))
    print('cos_theta_sun = {c}'.format(c=cos_theta_sun))
    print('theta_sun = arccosine({c}) = {t} = {d} deg'.format(c=cos_theta_sun,t=theta_sun,d=theta_deg))
    theta_deg = int(theta_deg)
    print('theta_sun = {d} deg {m} min {s} sec'.format(d=theta_deg,m=t_min,s=t_sec))

def get_aziumuth(delta, beta, omega, _lambda):
    print('')
    print('The solar azimuth is given by:')
    print('tan_phi_sun = (cos(delta)sin(omega - lambda)) / (cos(delta)sin(beta)cos(omega - lambda) - sin(delta)cos(beta))')
    print('tan_phi_sun = (cos({d})sin({o} - {l})) / (cos({d})sin({b})cos({o} - {l}) - sin({d})cos({b}))'.format(d=delta,o=omega,b=beta,l=_lambda))
    delta = math.radians(delta)
    beta = math.radians(beta)
    omega = math.radians(omega)
    _lambda = math.radians(_lambda)
    tan_phi_sun = (math.cos(delta)*math.sin(omega - _lambda)) / ((math.cos(delta)*math.sin(beta)*math.cos(omega - _lambda)) - (math.sin(delta) * math.cos(beta)))
    print('tan_his_sun = {t}'.format(t=tan_phi_sun))
    atan = math.degrees(math.atan(tan_phi_sun))
    print('phi_sun = {a} degrees'.format(a=atan))
    comp = 180 - atan
    print('The compass azimuth is: 180 - ({a}) = {c} degrees'.format(a=atan,c=comp))

def main():
    if args['--time']:
        EST = float(args['--time'])
    else:
        EST = 15.00

    TZ = 4
    print('Indianapolis is in the Eastern Time Zone (+5), and with daylight savings time the effective time zone is +4')
    print('')
    print('The latitude (beta) of Indianapolis is 39 deg 46 min 1 in N (39.77 deg)')
    print('The longitude (lambda) of Indianapolis is 86 deg 9 in 0 in W (-86.15 deg)')
    ET_h = 11
    ET_m = 45
    ET_s = 40.08
    ET = ET_h + float(ET_m)/60 + float(ET_s)/3600


    app_h = -8
    app_m = -35
    app_s = -30.6
    app = app_h + float(app_m)/60 + float(app_s)/3600
    print('')
    print('For 15 October 2016, from the Almanac, the ephermis transit ET is {h} h {m} m {s} s = {q} h'.format(h=ET_h,m=ET_m,s=ET_s,q=ET))
    print('The apparent declination delta is {h} deg {m} min {s} sec = {q}'.format(h=app_h,m=app_m,s=app_s,q=app))
    print('')
    print('Solar longitude omega = (ET - LT - TZ) * 15')
    print('omega = ({h} + {m}/60 + {s}/3600 - {l} - {t}) * 15'.format(h=ET_h,m=ET_m,s=ET_s,l=EST,t=TZ))
    omega = get_solar_longitude(ET,EST,TZ)
    print('omega = {o} degrees'.format(o=omega))

    get_zenith(app,39.77,omega,-86.15)


    get_aziumuth(app,39.77,omega,-86.15)

if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
