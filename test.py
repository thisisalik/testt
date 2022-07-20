from django.db import models
from models.models import Web_model
import uuid
import numpy as np
import datetime
import sys
import pylab as pl
import ionofunclib as myfunc
import ionoconslib as mycons
import nedm2020funclib as nedm
import timeit
#  user input parameters 

#1) our goal is to get ne, stec, Time vector,

# 1. lat_deg
# 2.lon_deg
# 3. UT_hrs
# 4. doy
# 5. F10p7_sfu
# 6. altmRx
# 7. altmTx
# 8. hmF2m
# 9. hmRefm
# 10. altm



# 2)  stec at arbitary many points, (Ne) and Slant TEC (STEC) in between two points, 
#electron density distribution and resultant slant TEC along a line connecting P1 and P2
#1. doyVect
#2. F10p7Vect - F10p7_sfu 
#3. UTVect
#4.x1, y1, z1, x2, y2, z2 -- lat_deg, lon_deg, altmRx, altmTx
#4. latrad -- x, y, z
#5. lonrad -- x, y, z
#6. altm -- x, y, z
#7. x, y, z, -- x1, y1, z1, x2, y2, z2 
#8. UTVect -- UT_hrs, 
#9. F10p7Vect -- F10p7Vect
#10. doyVect -- doy 

#general , necessary parameters 

#1. lat_deg
# 2.lon_deg
# 3. UT_hrs
# 4. doy
# 5. F10p7_sfu
# 6. altmRx
# 7. altmTx
#8. P1 coordinate -- x1, y1, z1
#9. P2 coordinate -- x2, y2, z2


# lat_deg = np.array([50., 60.])                                  #WGS84 geographic latitude Vector in deg
# lon_deg = np.array([5., 0.])                                  #WGS84 geographic longitude Vector in deg
# UT_hrs = np.array([1., 1.])                                   #Universal Time (UT) in hours Vector
# doy = np.array([1., 1.])                                      #day of year Vector
# F10p7_sfu = np.array([160., 80.]) 	                            #solar radio flux in flux units Vector
# altmRx = np.array([100., 100.])                                   #receiver altitude Vector in meters
# altmTx = np.array([20200000., 20200000.])                       #transmitter altitude Vector in meters
# hmF2m = 350 * 1000  * np.ones(1)													#
# hmRefm = np.array([300000, 350000])  #350 * 1000
# altm = np.array([350000., 1000000.])



# Ne, altkm, stec = nedm.nedm2020(doy, F10p7_sfu, UT_hrs, lat_deg, lon_deg, altm)
# print(stec )



models=Web_model.objects.all()
print(models)