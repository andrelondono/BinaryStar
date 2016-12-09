#elliptical orbit for binary stars - numerical

from visual import *
import numpy as np
M1=2.0e30
M2=2.0e30
G=6.67e-11
r0=2e11
v0=0.75e4

mywindow1 = gdisplay(xtitle = 'time(s)',ytitle = 'Energy (J)', title = 'Total energy of star 1')
f1 = gcurve(gdisplay = mywindow1, color = color.cyan)
f2 = gcurve(gdisplay = mywindow1, color = color.red)

star1=sphere(pos=(-r0,0,0),color=color.yellow,radius=5e9)
star2=sphere(pos=(r0,0,0),color=color.blue,radius=5e9)
v=vector(0,v0,0)
dt=45390856.1515/1e6
trace1=curve(color=color.yellow)
trace2=curve(color=color.red)
t=0.0
v1=-v
v2=v
while t<100000*24*3600:
    rate(20000000)
    r1=star1.pos-star2.pos
    r2=star2.pos-star1.pos
    R=(r1.x**2+r1.y**2+r1.z**2)**0.5
    r1hat=r1/R
    r2hat=r2/R

    F1=-(G*M1*M2/R**2)*r1hat
    F2=-(G*M1*M2/R**2)*r2hat
    a1=F1/M1
    a2=F2/M2
    star1.pos=star1.pos+v1*dt
    star2.pos=star2.pos+v2*dt
    v1=v1+a1*dt
    v2=v2+a2*dt
    
    star1KE = .5*(M1)*mag(v1)**2
    #star1GPE = G*(M1*M2)/mag(star1.pos-star2.pos)
    
    t=t+dt

    if abs(t-45390856.1515)<1:
        print star2.pos
        print star1.pos
        print t
        break
        
     f1.plot(pos = (t, star1KE))
    #f2.plot(pos = (t, star1GPE))    
    trace1.append(star1.pos)
    trace2.append(star2.pos)
    
