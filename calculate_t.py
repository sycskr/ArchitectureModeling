import numpy as np
from sympy.polys.polyoptions import Symbols 

#VUW
vanishing_points=np.load("./data/vanishing_points.npy",allow_pickle=True)
# vanishing_points=[(2159079/944, 11343149/3186), (-5188908/2305, 299896/2305), (32505163/6754, -15696743/6754)]
v1,v2=vanishing_points[0]
u1,u2=vanishing_points[1]
w1,w2=vanishing_points[2]
test_points=np.load("./data/test_points.npy")
p1,p2=test_points[0]
a1,a2=test_points[1]
b1,b2=test_points[2]
c1,c2=test_points[3]
t_points=[]
t1=(((a1-p1)/(u1-a1))/((a2-p2)/(u2-a2)))/2
t2=(((b1-p1)/(v1-b1))/((b2-p2)/(v2-b2)))/2
t3=(((c1-p1)/(w1-c1))/((c2-p2)/(w2-c2)))/2
t_points.append(t1)
t_points.append(t2)
t_points.append(t3)

np.save("./data/t_points.npy",t_points)

if __name__=="__main__":
    print("t1:\n{}\nt2:\n{}\nt3:\n{}".format(t1,t2,t3))
    print(t_points)
