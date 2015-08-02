"""
polywarp.py
Trey Wenger - August 2015

Implementation of IDL's polywarp.pro
Shamelessly copied, well tested against IDL procedure
"""

import sys
import numpy as np
from scipy.optimize import curve_fit

def polywarp(xi,yi,xo,yo,degree=1):
    """
    Fit a function of the form
    xi = sum over i and j from 0 to degree of: kx[i,j] * xo^j * yo^i
    yi = sum over i and j from 0 to degree of: ky[i,j] * xo^j * yo^i
    Return kx, ky
    len(xo) must be greater than or equal to (degree+1)^2
    """
    if len(xo) != len(yo) or len(xo) != len(xi) or len(xo) != len(yi):
        print "Error: length of xo, yo, xi, and yi must be the same"
        return
    if len(xo) < (degree+1.)**2.:
        print "Error: length of arrays must be greater than (degree+1)^2"
        return
    # ensure numpy arrays
    xo = np.array(xo)
    yo = np.array(yo)
    xi = np.array(xi)
    yi = np.array(yi)
    # set up some useful variables
    degree2 = (degree+1)**2
    x = np.array([xi,yi])
    u = np.array([xo,yo])
    ut = np.zeros([len(xo),degree2])
    u2i = np.zeros(degree+1)
    for i in range(len(xo)):
        u2i[0] = 1.
        zz = u[1,i]
        for j in range(1,degree+1):
            u2i[j]=u2i[j-1]*zz
        print "u2i",u2i
        ut[i,0:degree+1] = u2i
        for j in range(1,degree+1):
            ut[i,j*(degree+1):j*(degree+1)+degree+1]=u2i*u[0,i]**j
        print "ut",ut
    uu = ut.T
    print "uu",uu
    kk = np.dot(np.linalg.inv(np.dot(uu,ut)),uu).T
    print "kk",kk
    print "x[0,:]",x[0,:]
    kx = np.dot(kk.T,x[0,:]).reshape(degree+1,degree+1)
    print "kx",kx
    ky = np.dot(kk.T,x[1,:]).reshape(degree+1,degree+1)
    print "ky",ky
    return kx,ky
