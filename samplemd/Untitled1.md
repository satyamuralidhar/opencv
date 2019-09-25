

```python
pip install opencv-python
```

    Collecting opencv-python
    [?25l  Downloading https://files.pythonhosted.org/packages/5e/7e/bd5425f4dacb73367fddc71388a47c1ea570839197c2bcad86478e565186/opencv_python-4.1.1.26-cp36-cp36m-manylinux1_x86_64.whl (28.7MB)
    [K     |████████████████████████████████| 28.7MB 31.7MB/s eta 0:00:01   |███▋                            | 3.2MB 5.3MB/s eta 0:00:05
    [?25hRequirement already satisfied: numpy>=1.11.3 in /srv/conda/envs/notebook/lib/python3.6/site-packages (from opencv-python) (1.17.0)
    Installing collected packages: opencv-python
    Successfully installed opencv-python-4.1.1.26
    Note: you may need to restart the kernel to use updated packages.



```python
pip install opencv-contrib-python
```

    Collecting opencv-contrib-python
    [?25l  Downloading https://files.pythonhosted.org/packages/33/9b/1f9ef069206002d0bbca80598193904ce1ae2a990e7465bc351b1264c7d8/opencv_contrib_python-4.1.1.26-cp36-cp36m-manylinux1_x86_64.whl (34.7MB)
    [K     |████████████████████████████████| 34.7MB 22.8MB/s eta 0:00:01     |██████████████████████████▏     | 28.4MB 22.8MB/s eta 0:00:01
    [?25hRequirement already satisfied: numpy>=1.11.3 in /srv/conda/envs/notebook/lib/python3.6/site-packages (from opencv-contrib-python) (1.17.0)
    Installing collected packages: opencv-contrib-python
    Successfully installed opencv-contrib-python-4.1.1.26
    Note: you may need to restart the kernel to use updated packages.



```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

!wget "https://raw.githubusercontent.com/satyamuralidhar/opencv/master/images/tiger.jpg"



```

    --2019-09-25 06:38:08--  https://raw.githubusercontent.com/satyamuralidhar/opencv/master/images/tiger.jpg
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.36.133
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.36.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 6803 (6.6K) [image/jpeg]
    Saving to: ‘tiger.jpg’
    
    tiger.jpg           100%[===================>]   6.64K  --.-KB/s    in 0s      
    
    2019-09-25 06:38:09 (39.2 MB/s) - ‘tiger.jpg’ saved [6803/6803]
    



    <Figure size 640x480 with 6 Axes>



```python
img = cv2.imread('tiger.jpg')

import cv2
img = cv2.imread('tiger.jpg')
ret,thresh1 = cv2.threshold(img , 100 , 255 , cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img , 100 , 255 , cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img , 100 , 255 , cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img , 100 , 255 , cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img , 100 , 255 , cv2.THRESH_TOZERO_INV)

titles = ['oringinal' , 'binary' ,'binary_inv' ,'trunc' ,'tozero' ,'tozero_inv']
images = [img , thresh1 , thresh2 , thresh3 , thresh4 , thresh5]
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i] ,'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()

```
