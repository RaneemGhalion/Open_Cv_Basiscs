# import the necessary packages
import argparse
import cv2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--Image_Path", required=True,
	help="path of the image")
ap.add_argument("-n", "--name", required=True,
	help="name of the new image")

args = vars(ap.parse_args())
image=cv2.imread(args["Image_Path"])
(h,w,c)=image.shape[:3]
print("hight ,width , channels",h,w,c)
# cv2.imshow("Original",image)
# cv2.waitKey(0)
# cv2.imwrite(args["name"],image)
# print("----------",args,"---------------")
# display a friendly message to the user
# print("Hi there {}, it's nice to meet you!".format(args["Image_Path"]))sd

# images are simply NumPy arrays -- with the origin (0, 0) located at
# the top-left of the image
(b,g,r)=image[0,0]
print("BGR",b,"  ",g," ",r)

hw=w//2
hh=h//2
(b1,g1,r1)=image[hw,hh]

# print(b1," ",g1," ",r1)


# access the pixel located at x=50, y=20
(b2,g2,r2)=image[20,50]
# print("b2 ,g2 ,r2",b2,g2,r2)

# update the pixel at (50, 20) and set it to red
image[20,50]=(0,0,255)
# print(image[20,50])

# since we are using NumPy arrays, we can apply array slicing to grab
# large chunks/regions of interest from the image -- here we grab the

# top-left corner of the image

top_left_corner=image[0:hh,0:hw]
cv2.imshow("top_left_corner",top_left_corner)
# cv2.waitKey(0)
# in a similar fashion, we can crop the top-right, bottom-right, and
# bottom-left corners of the image and then display them to our
# screen
#  top-right
top_right_corner = image[0:hh, hw:w]
cv2.imshow("top_right_corner", top_right_corner)
# cv2.waitKey(0)

# bottom-right
bottom_right_corner=image[hh:,hw:]
cv2.imshow("bottom_right_corner", bottom_right_corner)
# cv2.waitKey(0)

# bottom-left corners 
bottom_left_corner=image[hh:,0:hw]
cv2.imshow("bottom_left_corner", bottom_left_corner)
cv2.waitKey(0)
