import numpy as np

height=19.01
length=20.1986
width=61.94
r1=length/height
r2=width/height

#VUW
vanishing_points=[(2159079/944, 11343149/3186), (-5188908/2305, 299896/2305), (32505163/6754, -15696743/6754)]
v1,v2=vanishing_points[0]
u1,u2=vanishing_points[1]
w1,w2=vanishing_points[2]
t_points=[-0.03086767426593458, 2.953253183435323, 0.5000000000000001]
t1=t_points[0]
t2=t_points[1]
t3=t_points[2]

points=[(2565, 1612), (2484, 2180), (940, 1112), 
        (1068, 1567), (2786, 1225), (2651, 1857)]
p1,p2=points[0]

P=np.zeros((3,4),dtype="float")
P[0][0]=u1*t1
P[0][1]=(v1*t2)/r1
P[0][2]=(w1*t3)/r2
P[0][3]=p1

P[1][0]=u2*t1
P[1][1]=(v2*t2)/r1
P[1][2]=(w2*t3)/r2
P[1][3]=p2

P[2][0]=t1
P[2][1]=t2/r1
P[2][2]=t3/r2
P[2][3]=1

np.save("./data/P.npy",P)
if __name__=="__main__":
        print("P:\n",P)