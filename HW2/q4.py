#!/usr/bin/env python
""" GE 501 HW#2 Question 4

    Author: Eric Bullock
    Date: September 2016
    Version: 1.1

Usage:
    q4.py [options]

Options:
    -h --help                   Show help

Question:

    A high resolution image satellite in a 500 km altitude orbit will be passing over your
        field site (39 deg 55 min N, 166 deg 25 min E) at 1 PM local time on october 31,
        2016. The sub-satellite point will be 38 deg 30 min N, 114 deg, 56 min E. You would
        like to make a ground truth reflectance measurement from the same look angle and
        direction as the satellite. Calculate the satellite view and azimuth angles and
        describe how you would orient the field radiometer so it is looking at the Earth's
        surface from the same line-of-sight as the satellite.

Example:

    > python q4.py

"""

import future
from docopt import docopt
import math
import sys

def do_theta(R,r_sat,lsat,bsat,_lambda,beta):
    Rr = math.radians(R)
    lsatr = math.radians(lsat)
    bsatr = math.radians(bsat)
    _lambdar = math.radians(_lambda)
    betar = math.radians(beta)

    print('cos_theta_sat = (Rsat(cos(lambda_sat - lambda)cos(beta_sat)cos(beta) + sin(beta_sat)sin(beta)) - R) / [Rsat^2 + R^2 - 2R*Rsat(cos(lambda_sat - lambda)*cos(beta_sat)*cos(beta)+sin(beta_sat)sin(beta))]^(1/2)')
    print('')
    print('The equation seems overwhelming, but we can break it up into parts. First, evaluate the term that appears in both the numerator and the denominator:')
    print('term1 = cos(lambda_sat - lambda)cos(beta_sat)cos(beta) + sin(beta_sat)sin(beta)')
    t1 = math.cos(lsatr - _lambdar) * math.cos(bsatr)*math.cos(betar) + math.sin(bsatr)*math.sin(betar)
    print('term1 = cos({s} - {l})cos({r})cos({b}) + sin({r})sin({b}) = {t}'.format(s=lsat,l=_lambda,r=bsat,b=beta,t=t1))
    print('')
    numerator = r_sat * t1 - R
    print('Now we can evaluate the numerator:')
    print('num = Rsat * term1 - R = {r} * {t} - {f} = {q}'.format(r=r_sat,t=t1,f=R,q=numerator))
    print('')
    print('..and then the denominator:')
    den = (r_sat**2 + R**2 - (2*R*r_sat*t1))**float(.5)
    print('den = [Rsat^2 + R^2 - 2(R)(Rsat)(term1)]^(1/2) = [{s}^2 + {r}^2 - 2(({r})({s})({t})]^(1/2) = {q}'.format(s=r_sat,r=R,t=t1,q=den))
    print('')
    print('Putting it together:')
    cos_theta_sat = float(numerator) / den
    theta_sat = math.acos(cos_theta_sat)
    theta_sat_deg = math.degrees(theta_sat)
    print('{n}/{d} = {q}'.format(n=numerator,d=den,q=cos_theta_sat))
    print('theta_sat = {t} = {q} degrees'.format(t=theta_sat,q=theta_sat_deg))
    return theta_sat_deg

def do_phi(R,r_sat,lsat,bsat,_lambda,beta):
    Rr = math.radians(R)
    lsatr = math.radians(lsat)
    bsatr = math.radians(bsat)
    _lambdar = math.radians(_lambda)
    betar = math.radians(beta)
    print('')
    print('For the satellite azimuth,')
    phi_num = math.sin(lsatr - _lambdar)*math.cos(bsatr)
    phi_den = math.cos(lsatr - _lambdar) * math.cos(bsatr)*math.sin(betar) - math.sin(bsatr)*math.cos(betar)
    phi = float(phi_num) / phi_den
    at_phi = math.atan(phi)
    at_phi_deg = math.degrees(at_phi)
    print('tan_phi_sat = (sin(lambda_sat - lambda)cos(beta_sat))/(cos(lambda_sat - lambda)cos(beta_sat)sin(beta) - sin(beta_sat)cos(beta)) = {n}/{d} = {q}'.format(n=phi_num,d=phi_den,q=phi))
    print('phi_sat = {a} = {d} degrees'.format(a=at_phi,d=at_phi_deg))
    print('')
    comp = 180 - at_phi_deg
    print('Following the table in the handout, since the numerator is negative and the denominator positive, the compass azimuth is 180-phi_sat = {q} degrees'.format(q=comp))
    print('')
    return at_phi_deg, comp

def main():

    R = 6378140
    H = 500000
    r_sat = R + H
    l_h = 114
    l_m = 56
    lsat = l_h + float(l_m)/60
    b_h = 38
    b_m = 30
    bsat = b_h + float(b_m)/60
    l2_h = 116
    l2_m = 25
    _lambda = l2_h + float(l2_m)/60
    b2_h = 39
    b2_m = 55
    beta = b2_h + float(b2_m) / 60


    print('The solution uses the equations from the handout on Sun-Earth relationships for satellite viewing with the inputs:')
    print('R = {r}'.format(r=R))
    print('Rsat = {r}'.format(r=r_sat))
    print('lambda_sat = {l} deg {m} min = {q}'.format(l=l_h,m=l_m,q=lsat))
    print('beta_sat = {l} deg {m} min = {q}'.format(l=b_h,m=b_m,q=bsat))
    print('lambda = {l} deg {m} min = {q}'.format(l=l2_h,m=l2_m,q=_lambda))
    print('beta = {l} deg {m} min = {q}'.format(l=b2_h,m=b2_m,q=beta))
    print('')
    theta = do_theta(R,r_sat,lsat,bsat,_lambda,beta)

    phi, comp = do_phi(R,r_sat,lsat,bsat,_lambda,beta)
    el_angle = 90 - theta
    comp_dir = comp - 180
    print('To orient the field radiometer so it is looking in the same direction as the satellite, you should place it so it is looking toward the northeast at an off-nadir look angle of {t} with a compass direction of {c} - 180 = {p} degrees. That is, the radiometer should be looking down in a northeasterly direction at an elevation angle of {e} degrees'.format(t=theta,c=comp,p=comp_dir,e=el_angle))


if __name__ == '__main__':
    args = docopt(__doc__,)

    main()
