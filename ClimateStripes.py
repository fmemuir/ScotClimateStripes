#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 18:25:59 2019

@author: freyamuir
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import matplotlib as mpl
import glob

## set parameters for plotting
params = {"ytick.color" : "k",
          "xtick.color" : "k",
          "axes.labelcolor" : "k",
          "axes.edgecolor" : "k",
          "font.sans-serif" : "Gill Sans MT",
          "font.family" : "sans-serif",
          "font.size" : "14"}
plt.rcParams.update(params)

## read in annual SLR dataset filenames
files = sorted(glob.glob('./psmsl/psmsl_1992_2017/*.txt')) 

tfiles = sorted(glob.glob('./avtemp/*.txt')) 


## call figure and define plot titles
fig1 = plt.figure(figsize=(8,8),frameon=False, )

## define gauge names
gauges = ['Lerwick','Kinlochbervie','Wick',
         'Stornoway']

## initiate loop through filenames, loop counter and gauge names  
for f, n, g, tfile in zip(files,range(1,len(files)+1), gauges, tfiles):
    
    ## read in datasets, reformat first col to integers (years)
    x=np.loadtxt(fname=f, usecols=[1])
    t=np.loadtxt(fname=f, usecols=[0])
    t=t.astype(np.int64)
    
    ## read in temp data
    yr=np.loadtxt(fname=tfile, usecols=[0], skiprows=7)
    mo=np.loadtxt(fname=tfile, usecols=[1], skiprows=7)
    tmax=np.loadtxt(fname=tfile, usecols=[2], skiprows=7)
    tmin=np.loadtxt(fname=tfile, usecols=[3], skiprows=7)
    yr=yr.astype(np.int64)
    mo=mo.astype(np.int64)
    
    tav=(tmax+tmin)/2
    tavyr=[]
    for i in np.arange(1,25):
        tavyr.append(np.average(tav[np.where(yr==1991+i)]))
    
    
    ## calculate anomalies
    meanx = np.nanmean(x)
    print('Mean SLR for',g+':',meanx)
    xanoms = x-meanx
    
    ## normalised anomalies
    norm = mpl.colors.Normalize(vmin=np.nanmin(xanoms),vmax=np.nanmax(xanoms))
    
    ## define subplot using loop counter, other plot params
    ax = fig1.add_subplot(len(files),1,n)
    ax.set_xlim(1991,2016)
    ax.set_ylabel(g,rotation='horizontal',ha='right',va='baseline')
    ax.set_yticks([])
    ax.set_xticks([])
    
    ## loop through data and plot vertical line for each year
    ## axvline only plots one line at a time
    for i in range(0,len(x)):
        plt.axvline(t[i],color = plt.cm.RdBu_r(norm(xanoms[i])),linewidth=18) # Red to Blue colormap reversed to be blue to red (_r)

    ax2 = ax.twinx()    
    ax2.plot(t,tavyr,'w-')
    
    ax.axis('off')
    ax2.axis('off')    

    
 # turn off all frames and edges for clean look
plt.subplots_adjust(wspace=0, hspace=0)    
plt.savefig('psmsl_climatestripes_1992_2015.png')            
#plt.savefig('psmsl_climatestripes.png',facecolor='#303030') # dark mode version
plt.show()
