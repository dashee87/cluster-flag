import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from clusterflag.country_flags import *

irelandFlag = simple_flag(npoints=[100000]*3)
japanFlag = japan_flag(npoints=[100000]*2)
laosFlag = laos_flag(npoints=[100000]*3)
swedenFlag = cross_flag(npoints=[100000]*5, colours=['blue']*4+['yellow'],
                        cenx=0.4)
turkeyFlag = crescent_flag(npoints=[100000]*3+[0]*2,rect=0,ratio=1.5,
                            colours=['white','white','red','',''],
                            bcx=0.35, bcy=0.5, 
                            scx=0.4, scy=0.5, bradius=0.25, sradius=0.2, 
                            starcx=0.5, starcy=0.5, starrx=0.125, 
                            starry=0.125)
libyaFlag = crescent_flag(npoints=[100000]*5)
countryFlags= [irelandFlag, japanFlag, laosFlag, swedenFlag, turkeyFlag, 
               libyaFlag]
f, axarr = plt.subplots(3, 2, figsize=(14, 14), dpi=80)
for pos,flag in enumerate(countryFlags):
    fig_row = int(pos/2)
    fig_col = pos%2
    axarr[fig_row, fig_col].set_xlim([0,1.5])
    axarr[fig_row, fig_col].set_ylim([0,1])
    axarr[fig_row, fig_col].set_xticks([])
    axarr[fig_row, fig_col].set_yticks([])
    axarr[fig_row, fig_col].set_axis_bgcolor('#e6e6e6')
    axarr[fig_row, fig_col].scatter(flag['x'], flag['y'],
                                    c=flag['flag_col'], marker='o',
                                    linewidths=0)
plt.show()

