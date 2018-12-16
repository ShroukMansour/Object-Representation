import numpy as np
import cv2
from Point import Point
from MPPVertices import MPPVertices
import  matplotlib.pyplot as plt
class MPP:
    def __init__(self):
        pass

    def get_boundary_points(self, path):
        im = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        ret, thresh = cv2.threshold(im, 127, 255, 0)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #print(contours)
        boundary = np.reshape(contours[0], [contours[0].shape[0], contours[0].shape[2]])
        # cv2.drawContours(im, contours, -1, (0, 255, 0), 3)
        # cv2.imshow("window", im)
        # cv2.waitKey()
        return boundary

    def get_BW_points(self, path, w, h):
        boundary = self.get_boundary_points(path)
        bw_points = [Point(boundary[0])]
        for i in range(1, boundary.shape[0]-1, w):
            p = Point(boundary[i])
            type = p.calc_type(boundary[i-1], boundary[i+1])
            if type != 0:
                bw_points.append(p)
        return np.array(bw_points)

    def DrawMPP(self,path,mppPoints):
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        contour=np.array(mppPoints)
        mask = np.zeros(img.shape)
        v=len(contour)
        contour = np.array(contour)
        contour = np.expand_dims(contour, 1)
        pts = contour.reshape((-1, 1, 2))
        cv2.polylines(mask, [pts], True, (255, 255, 255))
        # plt.figure(figsize=(13, 13))
        # plt.imshow(mask, cmap='gray'), plt.title(str(v))
        # plt.xticks([]), plt.yticks([])
        # plt.show()
        return mask, v



def mpp(path, block_size):
    mpp = MPP()
    mppVert = MPPVertices()
    # returns an array of points, make sure it's clockwise or anticlock wise as you need
    BW_points = mpp.get_BW_points(path, block_size, block_size)
    mppPoints = mppVert.Is_vertix(BW_points)
    mask, v = mpp.DrawMPP(path, mppPoints)
    return np.array(mask), np.array(v)


img_2, v_2 = mpp('leaf.png', 2)
img_5, v_5 = mpp('leaf.png', 5)
img_10, v_10 = mpp('leaf.png', 10)
img_20, v_20 = mpp('leaf.png', 20)
img_32, v_32 = mpp('leaf.png', 32)
img_64, v_64= mpp('leaf.png', 64)

plt.figure(figsize=(13, 13))
plt.subplot(231), plt.imshow(img_2, cmap='gray'), plt.title(str(v_2))
plt.xticks([]), plt.yticks([])
plt.subplot(232), plt.imshow(img_5, cmap='gray'), plt.title(str(v_5))
plt.xticks([]), plt.yticks([])
plt.subplot(233), plt.imshow(img_10, cmap='gray'), plt.title(str(v_10))
plt.xticks([]), plt.yticks([])
plt.subplot(234), plt.imshow(img_20, cmap='gray'), plt.title(str(v_20))
plt.xticks([]), plt.yticks([])
plt.subplot(235), plt.imshow(img_32, cmap='gray'), plt.title(str(v_32))
plt.xticks([]), plt.yticks([])
plt.subplot(236), plt.imshow(img_64, cmap='gray'), plt.title(str(v_64))
plt.xticks([]), plt.yticks([])
plt.show()