#elliptical orbit for binary stars - Numerical solution
#Physics 77 
from visual import *
import numpy as np

# Using to same mass stars
M1=2.0e30
M2=2.0e30
G=6.67e-11
r0=2e11
v0=1.5e4
m3=5.972e24

star1=sphere(pos=(-r0,0,0),color=color.yellow,radius=2e10)
star2=sphere(pos=(r0,0,0),color=color.red,radius=2e10)
planet3=sphere(pos=(18*r0,0,0),color=color.blue, radius=4e9)

v=vector(0,v0,0)
dt=5000
trace1=curve(color=color.yellow)
trace2=curve(color=color.green)
trace3=curve(color=color.red)
t=0
v1=-v
v2=v
v3=0.5*v

while t<100000*24*3600:
    rate(200000000)
   
   #stars
    r1=star1.pos-star2.pos
    r2=star2.pos-star1.pos
    R=(r1.x**2+r1.y**2+r1.z**2)**0.5
    r1hat=r1/R
    r2hat=r2/R
 
    F1=-(G*M1*M2/R**2)*r1hat
    F2=-(G*M1*M2/R**2)*r2hat
    a1=F1/M1
    a2=F2/M2
    #Eulers method
    star1.pos=star1.pos+v1*dt
    star2.pos=star2.pos+v2*dt
    v1=v1+a1*dt
    v2=v2+a2*dt

    #planet
    r31=planet3.pos-star1.pos
    r32=planet3.pos-star2.pos
    R31=(r31.x**2+r31.y**2+r31.z**2)**0.5
    R32=(r32.x**2+r32.y**2+r32.z**2)**0.5
    
    r31hat=r31/R31
    r32hat=r32/R32
    F31=-(G*M1*m3/R31**2)*r31hat
    F32=-(G*M2*m3/R32**2)*r32hat
    F3=F31+F32
    a3=F3/m3
    planet3.pos=planet3.pos+v3*dt
    v3=v3+a3*dt
        
    t=t+dt

    trace1.append(star1.pos)
    trace2.append(star2.pos)
    trace3.append(planet3.pos)


    
