import cv2
import matplotlib.pyplot as plt
img = cv2.imread('robot.jpg')
img2 = cv2.imread('robot2.jpg')
img = img[0:142, 0:194,:]
img2 = img2[0:142,  0:106,:]
print(img.shape) 
print(img2.shape)
def showing(im):
    plt.imshow(im[:,:,::-1])
    plt.show()

def imshow(im):
    cv2.imshow('Preview',im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
showing(img)
showing(img2)
print(img)
print(img2)
imshow(img)
imshow(img2)

added = cv2.add(img, img2)
showing(added)
print(added)