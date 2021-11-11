from sympy import *
import math
import numpy as np


points=np.load("./data/points.npy")
vanishing_points=[]
x,y=symbols('x y')
x0,y0=points[0]
x1,y1=points[1]
x2,y2=points[4]
x3,y3=points[5]


eq1=((x-x0)/(x1-x0))-((y-y0)/(y1-y0))
eq2=((x-x2)/(x3-x2))-((y-y2)/(y3-y2))

result=solve([eq1,eq2],[x,y])
vanishing_points.append((result[x],result[y]))
v1,v2=(result[x],result[y])
if __name__=='__main__':
        print("V:",result,"\n")

x0,y0=points[0]
x1,y1=points[2]
x2,y2=points[1]
x3,y3=points[3]

eq1=((x-x0)/(x1-x0))-((y-y0)/(y1-y0))
eq2=((x-x2)/(x3-x2))-((y-y2)/(y3-y2))

result=solve([eq1,eq2],[x,y])
vanishing_points.append((result[x],result[y]))
u1,u2=(result[x],result[y])
if __name__=='__main__':
        print("U:",result,"\n")

x0,y0=points[0]
x1,y1=points[4]
x2,y2=points[1]
x3,y3=points[5]

eq1=((x-x0)/(x1-x0))-((y-y0)/(y1-y0))
eq2=((x-x2)/(x3-x2))-((y-y2)/(y3-y2))

result=solve([eq1,eq2],[x,y])
vanishing_points.append((result[x],result[y]))
w1,w2=(result[x],result[y])
if __name__=='__main__':
        print("W",result,"\n")
if __name__=='__main__':
        print(vanishing_points)

eq3=(w1-u1)*(v1-x)+(w2-u2)*(v2-y)
eq4=(v1-u1)*(w1-x)+(v2-u2)*(w2-y)
# print(float((w1-u1)*(v1-w1)+(w2-u2)*(v2-w2)))
result=solve([eq3,eq4],[x,y])
if __name__=='__main__':
        print("K",result,"\n")

np.save("./data/vanishing_points.npy",vanishing_points)

# p1,p2=(2565, 1612)
# a1,a2=(2484, 2180)
# b1,b2=(940, 1112)
# c1,c2=(2786, 1225)
# t1=(((a1-p1)/(u1-a1))/((a2-p2)/(u2-a2)))/2
# t2=(((b1-p1)/(v1-b1))/((b2-p2)/(v2-b2)))/2
# t3=(((c1-p1)/(w1-c1))/((c2-p2)/(w2-c2)))/2

# print("t1:\n{}\nt2:\n{}\nt3:\n{}".format(t1,t2,t3))
