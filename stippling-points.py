import cv2
import random
import sys
import numpy as np

#
#       GETS CLOSEST COLOR
#
def get_closest_color(self, chosen_pixel):
    available_pixel = self.available_pixel
    distances = []

   for key, value in available_pixel.items():
        a1 = value
        c1 = chosen_pixel
        curr_dist = a1 - c1
        distances.append(curr_dist)
        if(curr_dist == min(distances)):
            curr_key = key

    return curr_key


#image is expected to be a grayscale cv2 image
def stippling_points(image):
    points = []


   for i, row in enumerate(image):
        for j, col in enumerate(image[i]):
            r = random.randint(0,255)
            if (r > image[i][j]):
                points.append([(i,j)])

    return points

#
#returns a dictionary of colors black to white
#the number of colors in between is determined by n
#len(colors) = n+2
#colors[0] = black
#colors[1] = white
#
def color_generator(n):
    n += 1
    color = {}
    for i in range(n+1):
        color[i] = int((i/n)*255)
    return color

im = cv2.imread("./chimp.jpeg", cv2.IMREAD_GRAYSCALE)
#print(im)
points = stippling_points(im)
#print(points)
print(color_generator(5))

white = [[[255,255,255] for x in range(len(im[0]))] for x in range(len(im))]

white = np.asarray(white)

for point in points:
    white[point[0][0]][point[0][1]] = [0,0,0]

cv2.imwrite("output.png", white)
