import numpy as np

P=np.array(np.load("./data/P.npy",allow_pickle=True))
if __name__=="__main__":
    print("P:\n",P)

#VUW
vanishing_points=np.load("./data/vanishing_points.npy",allow_pickle=True)
if __name__=="__main__":
    print("vanishing_points:\n",vanishing_points)
# vanishing_points=[(2159079/944, 11343149/3186), (-5188908/2305, 299896/2305), (32505163/6754, -15696743/6754)]
v1,v2=vanishing_points[0]
u1,u2=vanishing_points[1]
w1,w2=vanishing_points[2]

t_points=np.load("./data/t_points.npy",allow_pickle=True)
if __name__=="__main__":
    print("t_points:\n",t_points)
t1=t_points[0]
t2=t_points[1]
t3=t_points[2]

r1_0=(v1*t2)/P[0][1]
r1_1=(v2*t2)/P[1][1]
r1_2=t2/P[2][1]
r1=(abs(r1_0)+abs(r1_1)+abs(r1_2))/3
print("r1:{},{},{}\n".format(r1_0,r1_1,r1_2))


r2_0=(w1*t3)/P[0][2]
r2_1=(w2*t3)/P[1][2]
r2_2=t3/P[2][2]
r2=(abs(r2_0)+abs(r2_1)+abs(r2_2))/3
print("r2:{},{},{}\n".format(r2_0,r2_1,r2_2))
print("r1:\n",r1)
print("r2:\n",r2)