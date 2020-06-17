'''This program takes a list of Right Ascension and declination in degrees for each source, calculates the distance
between each source and the high-mass protostar, and convert this distance into physical coordinates in parsec. 
The physical coordinates are written in a file.'''

import numpy as np

# X-ray sources positions
alpha, delta = np.loadtxt('All_protostars_with_unclass_Xray.txt', unpack=True,usecols=[1,2])

# High-mass protostar position RA and Dec in degrees
alpha_HM_proto = 254.923402
delta_HM_proto = 40.062132

##Calculation of the physical coordinates with high-mass protostar as center
i=0
coord = open('All_protostars_with_unclass_Xray_physical_coordinates.txt', 'w')
for i in range(957):
    RA = ((alpha_HM_proto - alpha[i])*np.cos(delta_HM_proto))*3600
    dec = (delta_HM_proto + delta[i])*3600    # to get the X and Y distance in arcsec
    X = -RA*1700./206265   # result will be in pc
    Y = dec*1700./206265
    print("{0:.10f} {1:.10f}".format(Y, X), file=coord)
coord.close
