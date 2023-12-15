import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from numpy import linspace

def dydt(Y, t,c,m,g ):
    x,y,vx,vy = Y[0],Y[1],Y[2],Y[3]
    v = np.sqrt(vx**2 + vy**2)
    eq = [vx, vy, (-c/m) * v * vx, -g - (c/m) * v * vy]
    return eq
def num_solve(tmax,Y0,c,m,g):
    t=np.linspace(0,tmax,1001)
    sol=integrate.odeint(dydt,Y0,t, args=(c,m,g))
    return sol
def xnormal(t,vx,x0):
    x = vx*t+x0
    return x

def ynormal(t,vy,y0,g):
    y = vy*t-(1/2)*g*t**2+y0
    return y
def plot_position(sol,tmax,g,y0,x0,vx,vy):
    t = np.linspace(0, tmax, 1001)
    x_normal = xnormal(t,vx,x0)
    y_normal = ynormal(t,vy,y0,g)
    x = sol[:, 0]
    y = sol[:, 1]
    fig, ax = plt.subplots()
    ax.plot(x, y, label='Quadratic Drag')
    ax.plot(x_normal, y_normal, label='No Drag')
    plt.legend(loc='best')
    ax.set_xlabel('X-position')
    ax.set_ylabel('Y-position')
    ax.set_title('Projectile Motion with Quadratic Drag - Position')
    plt.savefig('plot_position.png')

def plot_velocity(sol,tmax):
    t = np.linspace(0, tmax, 1001)
    vx = sol[:, 2]
    vy = sol[:, 3]
    fig, ax = plt.subplots()
    ax.plot(t, vx, label='X-Velocity')
    ax.plot(t, vy, label='Y-Velocity')
    plt.legend(loc='best')
    ax.set_xlabel('Time')
    ax.set_ylabel('Velocity')
    ax.set_title('Projectile Motion with Quadratic Drag - Velocity')
    plt.savefig('plot_velocity.png')

def main():
    sol = num_solve(10, [0, 0, 50, 50], 0.5, 10, 9.8)
    plot_position(sol,10,9.8,0,0,50,50)
    plot_velocity(sol,10)

main()
