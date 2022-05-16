# -*- coding: utf-8 -*-
"""
Created on Thu May 12 13:42:35 2022

@author: gijsl
"""

"""
Created on Tue May 10 14:48:39 2022

@author: Yorick Vos
"""

# Import standard modules
import numpy as np
import matplotlib.pyplot as plt
import fplsqlib as fp


def kracht(G,x1,y1,x2,y2,m1,m2):
    F = G*(m1 * m2)/((x1 - x2)**2 + (y1 - y2)**2)
    rFx = (x2 - x1)/((x1 - x2)**2 + (y1 - y2)**2)**(0.5) * F
    rFy = (y2 - y1)/((x1 - x2)**2 + (y1 - y2)**2)**(0.5) * F

    return rFx, rFy

def versnellingen(N,G,x,y,m):

    ax2 = np.zeros(N)
    ay2 = np.zeros(N)
    
    for i in range(N):
        ax = np.zeros(N)
        ay = np.zeros(N)
        for j in range(N):
            if i != j:
                ax1, ay1 = kracht(G, x[i], y[i], x[j] ,y[j], m[i], m[j])
                ax[j] = ax1/m[i]
                ay[j] = ay1/m[i]
                # print(i, j)
                # print(f"ay = {ay1}")
                # print(f"ax = {ax1} \n")
                
        ax2[i] = np.sum(ax)
        ay2[i] = np.sum(ay)
        # print(f"ax2 = {ax2}")
        # print(f"ay2 = {ay2}\n")
        
    return ax2, ay2
        
def simulatie(N,G,x,y,vx,vy,m,t,steps,planeet):
    e = 0
    k = 0
    
    plt.figure()
    
    dt = t/steps
    colors = np.array(['r','b','c','k']) #kan uitgebreid worden met meer kleuren
    for r in range(steps):
        if(r == 0):
            ax, ay = versnellingen(N,G,x,y,m)
            vx += 1/2*dt*ax
            vy += 1/2*dt*ay
            k += 1
        else:
            x += dt*vx
            y += dt*vy
            for z in range(N):
                if e <= N-1:
                    plt.plot(x[z], y[z], f'{colors[z]}.', label=f"{planeet[z]}")
                    e += 1
                else:
                    plt.plot(x[z], y[z], f'{colors[z]}.')
            
            ax, ay = versnellingen(N,G,x,y,m)
            vx += dt*ax
            vy += dt*ay
            # print(f"vx = {vx}")
            # print(f"vy = {vy} \n")
    plt.legend()
    plt.show()
    return

# gebruik de arrays voor de bijbehorende waardes

simulatie(3,1.20e-4,np.array([0.,1,1+2.67*10**-3]), np.array([0.,0,0]), np.array([0.,0,0]), np.array([0.,6.32,6.32+0.212]),np.array([3.33e5,1,1.23*10**-2]),1,300,np.array(["Zon", "Aarde", "Maan"]))