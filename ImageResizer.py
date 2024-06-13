import cv2

inimage="lotus.jpg"                  # take a image which we have to change as a input
opimage="LotusNewImage1.png"         # Generated image name which we want at output
scale_per=750    


img=cv2.imread(inimage,cv2.IMREAD_UNCHANGED)
print("--------")
#print(img)
print("--------")



w = int(img.shape[1] * scale_per / 2000) 
h = int(img.shape[0] * scale_per / 1000)

dsize=(w,h) # tuple with width and height

op=cv2.resize(img,dsize)   # resize() function is used here to resize the input image with new dimensions

cv2.imwrite('LotusNewImage1.png',op)   # New modified generated image at output side

cv2.waitKey(0)  # pauses the script until a key is pressed (0 means waiting indefinitely)  Wait for the user to press a key