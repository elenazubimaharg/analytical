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
    ax.plot(x, y, label='Quadratic Drag, C = 0.2')
    ax.plot(x_normal, y_normal, label='No Drag')
    plt.legend(loc='best')
    ax.set_xlabel('X-position')
    ax.set_ylabel('Y-position')
    ax.set_title('Projectile Motion with Quadratic Drag - Position')
    plt.savefig('plot_position.png')

def plot_position_c(tmax,g,y0,x0,vx,vy):
    m=10
    c=0.01
    Y0=[0, 0, 20, 20]
    xy_list=[]
    for i in range(10):
        sol = num_solve(tmax,Y0,c,m,g)
        x_temp=sol[:,0]
        y_temp=sol[:,1]
        xy_temp=[x_temp,y_temp,c]
        xy_list.append(xy_temp)
        c+=0.005
    t = np.linspace(0, tmax, 1001)
    x_normal = xnormal(t,vx,x0)
    y_normal = ynormal(t,vy,y0,g)
    x_1 = xy_list[0][0]
    y_1 = xy_list[0][1]
    x_2 = xy_list[1][0]
    y_2=xy_list[1][1]
    x_3=xy_list[2][0]
    y_3=xy_list[2][1]
    x_4=xy_list[3][0]
    y_4=xy_list[3][1]
    x_5=xy_list[4][0]
    y_5=xy_list[4][1]
    x_6 = xy_list[5][0]
    y_6 = xy_list[5][1]
    x_7 = xy_list[6][0]
    y_7 = xy_list[6][1]
    x_8 = xy_list[7][0]
    y_8 = xy_list[7][1]
    x_9 = xy_list[8][0]
    y_9 = xy_list[8][1]
    x_10 = xy_list[9][0]
    y_10 = xy_list[9][1]
    fig, ax = plt.subplots()
    ax.plot(x_normal, y_normal, label='No Drag')
    ax.plot(x_1, y_1,label='C=0.01')
    ax.plot(x_2, y_2,label='C=0.015')
    ax.plot(x_3, y_3, label='C=0.02')
    ax.plot(x_4, y_4, label='C=0.025')
    ax.plot(x_5, y_5, label='C=0.03')
    ax.plot(x_6, y_6, label='C=0.035')
    ax.plot(x_7, y_7, label='C=0.04')
    ax.plot(x_8, y_8, label='C=0.045')
    ax.plot(x_9, y_9, label='C=0.05')
    ax.plot(x_10, y_10, label='C=0.055')

    plt.legend(loc='best')
    ax.set_xlabel('X-position')
    ax.set_ylabel('Y-position')
    ax.set_title('Projectile Motion with Quadratic Drag - Position')
    plt.savefig('plot_position_c.png')

def plot_velocity(sol,tmax):
    t = np.linspace(0, tmax, 1001)
    vx = sol[:, 2]
    vy = sol[:, 3]
    fig, ax = plt.subplots()
    ax.plot(t, vx, label='X-Velocity (C = 0.2)')
    ax.plot(t, vy, label='Y-Velocity (C = 0.2)')
    plt.legend(loc='best')
    ax.set_xlabel('Time')
    ax.set_ylabel('Velocity')
    ax.set_title('Projectile Motion with Quadratic Drag - Velocity')
    plt.savefig('plot_velocity.png')

def main():
    sol = num_solve(10, [0, 0, 20, 20], 0.2, 10, 9.8)
    plot_position(sol,10,9.8,0,0,20,20)
    plot_position_c(10, 9.8, 0, 0, 20, 20)
    plot_velocity(sol,10)

main()
