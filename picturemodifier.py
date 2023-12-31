import cv2
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors

from matplotlib.colors import hsv_to_rgb

import PIL.Image as Image

print("done")


racinglinepic1 = cv2.imread("./data2/f045b193-736a-11ee-8402-001a7dda7115.png",cv2.COLOR_BGR2RGB)
racinglinepic1 = cv2.cvtColor(racinglinepic1, cv2.COLOR_BGR2RGB)
plt.imshow(racinglinepic1)
#plt.show()

#r, g, b = cv2.split(racinglinepic1)
#fig = plt.figure()
#axis = fig.add_subplot(1, 1, 1, projection="3d")

pixel_colors = racinglinepic1.reshape((np.shape(racinglinepic1)[0]*np.shape(racinglinepic1)[1], 3))
norm = colors.Normalize(vmin=-1.,vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()

#axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
#axis.set_xlabel("Red")
#axis.set_ylabel("Green")
#axis.set_zlabel("Blue")
#plt.show()


hsv_racing = cv2.cvtColor(racinglinepic1, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv_racing)
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")

axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Hue")
axis.set_ylabel("Saturation")
axis.set_zlabel("Value")
plt.show()

dark_green = (45, 25, 130)
light_green = (85, 200, 222)

lg_square = np.full((10, 10, 3), light_green, dtype=np.uint8) / 225.0
dg_square = np.full((10, 10, 3), dark_green, dtype=np.uint8) / 225.0

plt.subplot(1, 2, 1)
plt.imshow(hsv_to_rgb(dg_square))
plt.subplot(1, 2, 2)
plt.imshow(hsv_to_rgb(lg_square))
plt.show()

dark_orange = (0, 25, 130)
light_orange = (15, 255, 222)

lo_square = np.full((10, 10, 3), light_orange, dtype=np.uint8) / 225.0
do_square = np.full((10, 10, 3), dark_orange, dtype=np.uint8) / 225.0

plt.subplot(1, 2, 1)
plt.imshow(hsv_to_rgb(do_square))
plt.subplot(1, 2, 2)
plt.imshow(hsv_to_rgb(lo_square))
plt.show()

mask = cv2.inRange(hsv_racing, dark_green, light_green)
result = cv2.bitwise_and(racinglinepic1, racinglinepic1, mask=mask)
plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(result)
plt.show()

mask2 = cv2.inRange(hsv_racing, dark_orange, light_orange)
result2 = cv2.bitwise_and(racinglinepic1, racinglinepic1, mask=mask2)
plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(result2)
plt.show()

final_mask = mask + mask2
final_result = cv2.bitwise_and(racinglinepic1, racinglinepic1, mask=final_mask)
plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(final_result)
plt.show()

def changeimage():
    picture = cv2.imread("./data2/ff6a9713-736a-11ee-9a06-001a7dda7115.png",cv2.COLOR_BGR2RGB)
    picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)