# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:54:14 2019

@author: nickh
"""

def albedo(alphaw, alphab, alphag, aw, ab, ag):
    """Caluclate the average planetary albedo. 
    alphaw*aw + alphab*ab + alphag*ag
    
    Arguments
    ---------
    alphaw : float
        Surface fraction of white daisies.
    alphab : float
        Surface fraction of black daisies.
    alphag : float
        Surface fraction of bare ground.
    aw = 0.7 : float
        Albedo of white daisies.
    ab = 0.8 : float
        Albedo of black dasies.
    ag = 0.5 : float
        Albedo of bare ground
    """
    return alphaw*aw + alphab*ab + alphag*ag