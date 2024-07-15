import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, pi

u0 = int(input("Enter initial velocity in m/s: "))
g = 9.81 #gravity
theta = int(input("Enter projectile angle in degrees: "))

uX = u0*cos(theta*pi/180)
uY = u0*sin(theta*pi/180)

t = (2*uY)/g #time of flight
h = (uY**2)/(2*g) #maximum height reached
r = ((u0**2)*sin(theta*pi/90))/g #maximum range
m = max([r,h])

t0 = np.linspace(0,t,200) #time intervals

sx = uX*t0 #horizontal distance
sy = uY*t0-((g*t0**2)/2) #vertical distance

plt.figure(figsize=(7,7))
plt.plot(sx,sy,color="orange",linestyle="--")
plt.ylim(-2,m+2)
plt.xlim(-2,m+2)
plt.text(m*0.27,m*0.27,f"Time of flight = {round(t,2)} sec\nMaximum height = {round(h,2)} m\nMaximum range = {round(r,2)} m")
plt.grid()
plt.show()