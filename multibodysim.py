#multi-planet binary start system

from visual import *
import numpy as np
G=6.67e-11
scene.height=600
scene.center=(0,0,0)
scene.range=4.9e12

#initial conditions for stars/planets
r0=2e11
v0=1.5e4
M1=2.0e30
M2=2.0e30
m3=5.972e24
m4=5.972e24
m5=5.972e24

star1=sphere(pos=(-r0,0,0),color=color.yellow,radius=8e10)
star2=sphere(pos=(r0,0,0),color=color.red,radius=8e10)
planet3=sphere(pos=(3.0*r0,0,0),color=color.blue, radius=4e9)
planet4=sphere(pos=(10*r0,0,0),color=color.blue, radius=4e9)
planet5=sphere(pos=(5*r0,0,0),color=color.blue, radius=4e9)

#initial vector velocities
v1=vector(0,-v0,0)
v2=vector(0,v0,0)
v3=vector(0,1.5*v0,0)
v4=vector(0,0.8*v0,0)
v5=vector(0,1.7*v0,0)

#simulation animation
trace1=curve(color=color.blue)
trace2=curve(color=color.blue)
trace3=curve(color=color.yellow)
trace4=curve(color=color.white)
trace5=curve(color=color.orange)

t=0
dt=5000

while t<100000*24*3600:
    rate(100000000)
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
    star1.pos=star1.pos+v1*dt
    star2.pos=star2.pos+v2*dt
    v1=v1+a1*dt
    v2=v2+a2*dt

    #planets
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


    r41=planet4.pos-star1.pos
    r42=planet4.pos-star2.pos
    R41=(r41.x**2+r41.y**2+r41.z**2)**0.5
    R42=(r42.x**2+r42.y**2+r42.z**2)**0.5
    r41hat=r41/R41
    r42hat=r42/R42
    F41=-(G*M1*m4/R41**2)*r41hat
    F42=-(G*M2*m4/R42**2)*r42hat
    F4=F41+F42
    a4=F4/m4
    planet4.pos=planet4.pos+v4*dt
    v4=v4+a4*dt


    r51=planet5.pos-star1.pos
    r52=planet5.pos-star2.pos
    R51=(r51.x**2+r51.y**2+r51.z**2)**0.5
    R52=(r52.x**2+r52.y**2+r52.z**2)**0.5
    r51hat=r51/R51
    r52hat=r52/R52
    F51=-(G*M1*m5/R51**2)*r51hat
    F52=-(G*M2*m5/R52**2)*r52hat
    F5=F51+F52
    a5=F5/m5
    planet5.pos=planet5.pos+v5*dt
    v5=v5+a5*dt
    
    
    t=t+dt

    trace1.append(star1.pos)
    trace2.append(star2.pos)
    trace3.append(planet3.pos)
    trace4.append(planet4.pos)
    trace5.append(planet5.pos)

