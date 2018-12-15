import numpy as np

import cv2
import matplotlib.pyplot as plt


def is_inf(n):
    return n == np.float("Inf") or n == np.float("-Inf")


def mpp_2(img_path, T):
    im = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    ret, thresh = cv2.threshold(im, 127, 255, 0)
    edges = np.zeros(im.shape)
    _, contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    mpp_ls = []
    p1 = contours[0][0, 0, :]
    p2 = contours[0][1, 0, :]
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    slope = dy / dx
    intercept = p1[1] - slope * p1[0]
    error = 0
    prev = p2
    x_const = p2[0]
    for i in range(2, contours[0].shape[0]):
        p = contours[0][i, 0, :]
        if not is_inf(slope) or slope == 0:
            yp = slope * p[0] + intercept
            error = error + abs(yp - p[1])
        else:
            if is_inf(slope):
                xp = x_const
            else:
                xp = (1 / slope) * (p[1] - intercept)
            error = error + abs(xp - p[0])

        if error > T:
            mpp_ls.append(p)
            error = 0
            dx = p[0] - prev[0]
            dy = p[1] - prev[1]
            x_const = p[0]
            slope = np.float(dy) / dx
            intercept = p[1] - slope * p[0]

        prev = p

    vertices = len(mpp_ls)
    mpp_np = np.array(mpp_ls)
    mpp_np = np.expand_dims(mpp_np, 1)
    pts = mpp_np.reshape((-1, 1, 2))
    cv2.polylines(edges, [pts], True, (255, 255, 255))
    return edges, vertices


img_0, v_0 = mpp_2("img2.png", -1)
img_5, v_5 = mpp_2("img2.png", 5)
img_10, v_10 = mpp_2("img2.png", 10)
img_20, v_20 = mpp_2("img2.png", 20)
img_40, v_40 = mpp_2("img2.png", 40)
img_80, v_80 = mpp_2("img2.png", 80)
img_160, v_160 = mpp_2("img2.png", 160)

plt.figure(figsize=(13, 13))
plt.subplot(231), plt.imshow(img_0, cmap='gray'), plt.title(str(v_0))
plt.xticks([]), plt.yticks([])
plt.subplot(232), plt.imshow(img_5, cmap='gray'), plt.title(str(v_5))
plt.xticks([]), plt.yticks([])
plt.subplot(233), plt.imshow(img_10, cmap='gray'), plt.title(str(v_10))
plt.xticks([]), plt.yticks([])
plt.subplot(234), plt.imshow(img_20, cmap='gray'), plt.title(str(v_20))
plt.xticks([]), plt.yticks([])
plt.subplot(235), plt.imshow(img_40, cmap='gray'), plt.title(str(v_40))
plt.xticks([]), plt.yticks([])
plt.subplot(236), plt.imshow(img_80, cmap='gray'), plt.title(str(v_80))
plt.xticks([]), plt.yticks([])

plt.show()
