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
print(h,w,c)
cv2.imshow("Cute catty",image)
cv2.waitKey(0)
cv2.imwrite(args["name"],image)
# print("----------",args,"---------------")
# display a friendly message to the user
# print("Hi there {}, it's nice to meet you!".format(args["Image_Path"]))sd