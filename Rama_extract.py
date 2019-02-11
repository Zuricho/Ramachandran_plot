#!/usr/bin/python2

"""
Created on Wed Feb 11 12:40:00 2019
@author: Zuricho
"""


import Bio.PDB
import math
import numpy as np


# transform the rad angle into degree angles
def degrees(rad_angle) :
    """Converts any angle in radians to degrees.

    If the input is None, then it returns None.
    For numerical input, the output is mapped to [-180,180]
    """
    if rad_angle is None :
        return None
    angle = rad_angle * 180 / math.pi
    while angle > 180 :
        angle = angle - 360
    while angle < -180 :
        angle = angle + 360
    return angle


phi_psi_list = np.zeros([2])


for model in Bio.PDB.PDBParser().get_structure("analyzer","PTR_sim.md.pdb"):
    for chain in model:
        poly = Bio.PDB.Polypeptide.Polypeptide(chain)
        phi_psi = (degrees(poly.get_phi_psi_list()[1][0]),degrees(poly.get_phi_psi_list()[1][1]))
        v = np.array(phi_psi)
        phi_psi_list = np.vstack((phi_psi_list,v))


phi_psi_list = phi_psi_list[1:,:]

np.savetxt("phi_psi.txt",phi_psi_list) 