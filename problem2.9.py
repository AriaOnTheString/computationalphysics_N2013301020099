#This is a program to calculate the ballistic trajectory
"""
Updated on 4/10/2016
Author:GUO Xiao
2013301020099
SI unit
"""
import numpy as np
from pylab import *
from math import *
import mpl_toolkits.mplot3d

x=[]
y=[]
z=[]
vx=[]
vy=[]
vz=[]
v=[]
t=[]
xp=[]
yp=[]
zp=[]

"""
input
"""
#parameter
w=2*pi/24/3600 #rotation angular speed of Earth(rad/s)
g=9.8 #local gravitational acceleration of Earth(m*s^(-2))
lat=pi*float(input('latitude(degree,North:+,South:-)='))/180
m=float(input('mass(kg)='))
B1=0
#parameter of B2
a=6.5e-3 #(K/m)
alpha=2.5
T0=288 # (K)
B20=4e-5*m  #initial value
#initial condition
x.append(0.0)
y.append(0.0)
z.append(0.0)
v0=float(input('v0='))
phi=pi*float(input('phi(degree)='))/180
theta=pi/2-pi*float(input('elevation angle(degree)='))/180
vx0=v0*sin(theta)*cos(phi)
vy0=v0*sin(theta)*sin(phi)
vz0=v0*cos(theta)
vx.append(vx0)
vy.append(vy0)
vz.append(vz0)
v.append(v0)
t.append(0.0)

dt=0.1
#parabola
xp.append(0)
yp.append(0)
zp.append(0)

'''
calculation
'''
i=0
f=open('problem2.9.txt','w')
while 1:
    B2=(1-a*z[i]/T0)**alpha*B20
    vx.append(vx[i]+dt*(-B1/m*vx[i]-B2/m*v[i]*vx[i]-2*w*vz[i]*cos(lat)+2*w*vy[i]*sin(lat)))
    vy.append(vy[i]+dt*(-B1/m*vy[i]-B2/m*v[i]*vy[i]-2*w*vx[i]*sin(lat)))
    vz.append(vz[i]+dt*(-g-B1/m*vz[i]-B2/m*v[i]*vz[i]+2*w*vx[i]*cos(lat)))
    x.append(x[i]+dt*vx[i+1])
    y.append(y[i]+dt*vy[i+1])
    z.append(z[i]+dt*vz[i+1])
    v.append(((vx[i+1])**2+(vy[i+1])**2+(vz[i+1])**2)**(1/2))
    t.append(t[i]+dt)
    xp.append(vx0*t[i+1])
    yp.append(vy0*t[i+1])
    zp.append(vz0*t[i+1]-g*t[i+1]**2/2)
    print t[-1],x[-1],y[-1],z[-1]
    print >> f,x[-1],y[-1],z[-1]
    i+=1
    if z[-1]<=0:
        break
f.close()

#plot 
plot(x,z,color='blue')
plot(xp,zp,'--',color='blue')
legend(('z-x','z-x parabola'))
title('Problem 2.9 z-x',fontsize=20)
xlabel('x(m)')
xlim(0,)
ylabel('z(m)')
ylim(0,)
savefig('problem2.9_x-z.png')
show()

plot(y,z,color='red')
plot(yp,zp,'--',color='red')
legend(('z-y','z-y parabola'))
title('Problem 2.9 z-y',fontsize=20)
xlabel('y(m)')
ylabel('z(m)')
ylim(0,)
savefig('problem2.9_y-z.png')
show()

#3D plot
fig = figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x,y,z,color='blue')
ax.set_xlabel('x/m')
ax.set_ylabel('y/m')
ax.set_zlabel('z/m')
savefig('problem2.9 3D.png')
show()


