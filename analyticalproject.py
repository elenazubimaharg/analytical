import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from numpy import linspace



def num_solve(max,c,m,g):
    range=np.arange(0,max,0.005)
    def eqn(Y, t):
        v=((Y[0]**2)+(Y[1]**2))**0.5
        eq =[(-1*c/m)*v*Y[0],-1*g-(c/m)*v*Y[1]] 
        return eq
    sol=integrate.odeint(eqn,[20,20],range)
    return sol
def solve_again(sol,max):
    x=np.arange(0,max,0.005)
    y1=sol[:,0]
    y2=sol[:,1]
    result1=integrate.cumtrapz(y1,x=x,initial=0)
    result2=integrate.cumtrapz(y2,x=x,initial=0)
    solution=[result1,result2]
    return solution
def plot(sol):
    x=sol[0]
    y=sol[1]
    fig,ax=plt.subplots()
    ax.plot(x,y)
    fig.savefig('plot1.png')
def main():
    sol=num_solve(40,0.5,0.5,-9.8)
    solution=solve_again(sol,40)
    plot(solution)
main()


