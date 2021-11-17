# ArchitectureModeling

## 建模使用流程

## 1、求取矩阵P

#### 运行point_get

中左右，由上到下，取点顺序如下图所示（非常重要）

![image-20211112155359678](C:\Users\syc\AppData\Roaming\Typora\typora-user-images\image-20211112155359678.png)

#### 运行get_vanishingpoint

#### 运行get_point

#### 运行calculate_t

![image-20211112155844324](C:\Users\syc\AppData\Roaming\Typora\typora-user-images\image-20211112155844324.png)

#### 运行calculate_P

注意代码第三至五行

```python
import numpy as np

height=19.01  #建筑的标高
length=20.1986  #长
width=61.94   #宽
r1=length/height
r2=width/height
```

参数测量如图所示

![image-20211112155844324](C:\Users\syc\AppData\Roaming\Typora\typora-user-images\image-20211112155844324.png)

### 2、求取测量边长比

#### 运行point_get

以下图为例，第一个点应该标坐标轴原点point0，第二个点标point1使其与原点连线为高

![image-20211112160121055](C:\Users\syc\AppData\Roaming\Typora\typora-user-images\image-20211112160121055.png)

#### 运行calculate_t

#### 运行calculate_r

![image-20211112160522171](C:\Users\syc\AppData\Roaming\Typora\typora-user-images\image-20211112160522171.png)
