import cv2
import random
import sys
import numpy as np

#image is expected to be a grayscale cv2 image
def stippling_points(image):
    points = []

    for i, row in enumerate(image):
        for j, col in enumerate(image[i]):
            r = random.randint(0,255)
            if (r >= image[i][j]):
                points.append([(i,j)])

    return points


im = cv2.imread("./download.jpeg", cv2.IMREAD_GRAYSCALE)
print(im)
points = stippling_points(im)
print(points)

white = [[[255,255,255] for x in range(len(im[0]))] for x in range(len(im))]

white = np.asarray(white)


for point in points:
    white[point[0][0]][point[0][1]] = [0,0,0]

cv2.imwrite("output.jpeg", white)
