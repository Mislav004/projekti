import cv2
import numpy as np

img = cv2.imread("cat.jpg")

# filter2D
blur_filter = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
]
)
blur_filter = blur_filter/9
#img = cv2.filter2D(img,ddepth=-1,kernel=blur_filter)

# no filter / bright image
no_filter = np.array([
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
)
no_filter = no_filter*2
#img = cv2.filter2D(img,ddepth=-1,kernel=no_filter)

# blur
#img = cv2.blur(img,ksize=(111,111))

# gaussian blur
#img = cv2.GaussianBlur(img,ksize=(11,11),sigmaX=30,sigmaY=300)

# filter2D
sharpen_filter = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
]
)
#img = cv2.filter2D(img,ddepth=-1,kernel=sharpen_filter)

# edge detection // laplacian
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gray_img = cv2.GaussianBlur(gray_img, ksize=(3,3),sigmaX=1,sigmaY=1)
#edges = cv2.Laplacian(gray_img,ddepth=-1)

# sobel
sobelhd_filter = np.array([
    [-1,-2,-1],
    [0,0,0],
    [1,2,1]
])
sobelhu_filter = np.array([
    [1,2,1],
    [0,0,0],
    [-1,-2,-1]

])
sobelvr_filter = np.array([
    [-1,0,1],
    [-2,0,2],
    [-1,0,1]

])
sobelvl_filter = np.array([
    [1,0,-1],
    [2,0,-2],
    [1,0,-1]

])
downedge = cv2.filter2D(gray_img,ddepth=-1,kernel=sobelvl_filter)
cv2.namedWindow("Cat!", cv2.WINDOW_NORMAL) 
cv2.resizeWindow("Cat!", 700, 700) 
cv2.imshow("Cat!",downedge)
cv2.waitKey(0)
cv2.destroyAllWindows()