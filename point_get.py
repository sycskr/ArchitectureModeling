import cv2
import numpy as np
import math

path="C:\\Users\\syc\\Pictures\\picture\\9.jpg"
img=cv2.imread(path)

def length_get(point,i,j):
    x0,y0=point[i]
    x1,y1=point[j]
    return math.sqrt(abs(y0-y1)**2+abs(x0-x1)**2)

points=[]
time=0
def click_fpo(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global time
        xy = "%d,%d" % (x, y)
        cv2.circle(img, (x, y), 10, (255,0,0), thickness = -1)    #(,,)内填写想采用的标注颜色
        cv2.putText(img, "point"+str(time)+":"+xy, (x+15, y), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0,0,255), thickness = 5)
        if __name__=='__main__':
            print("the point{} position:({},{})".format(time,x,y))
        global points
        points.append((x,y))
        cv2.imshow("fpoint obtain", img)  
        time+=1
    
cv2.namedWindow("fpoint obtain",0)
cv2.setMouseCallback("fpoint obtain", click_fpo)

while(1):
    cv2.namedWindow("fpoint obtain",0)
    cv2.imshow("fpoint obtain", img)
    if cv2.waitKey(0)&0xFF==27:#ESC退出
        break
np.save("./data/points.npy",points)

np.save("./data/test_points",points)

if __name__=='__main__':
    print(points)
    print(length_get(points,0,1),"\n")
    print(length_get(points,0,2),"\n")
    print(length_get(points,0,3),"\n")
    cv2.destroyAllWindows()