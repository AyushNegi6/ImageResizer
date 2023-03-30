import cv2

source = "image.jpg"
destination = "newImage.jpg"
#Percent by which the image is resizeed
scale_percent = 50


src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",src)

#calculate the 50% of orignal dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

#desize
dsize  = (width,height)

#resize image 
output = cv2.resize(src, dsize)

cv2.imwrite(destination,output)
cv2.waitKey(0)