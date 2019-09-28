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
        if curr_dist == min(distances):
            curr_key = key

    return curr_key


# image is expected to be a grayscale cv2 image
def stippling_points(image):
    points = []

    for i, row in enumerate(image):
        for j, col in enumerate(image[i]):
            r = random.randint(0, 255)
            if r > image[i][j]:
                points.append([(j, i)])

    return points


#
# runs edgepoints, goes to the designated edgepoints and darkens them by a parameterized value
#

def darken_edges(image, darken):
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    sys.path.append('..')
    from EdgePoints import edgepoints as ep

    edges = cv2.Canny(image, 100, 200)

    edge_points = ep.generate_edgepoints(edges)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    for line in edge_points:
        for point in line:
            print(point)
            print(image[point[0]][point[1]])
            if image[point[0]][point[1]] < darken:
                image[point[0]][point[1]] = 0
            else:
                image[point[0]][point[1]] -= darken

    return image


#
# returns a dictionary of colors black to white
# the number of colors in between is determined by n
# len(colors) = n+2
# colors[0] = black
# colors[1] = white
#
def color_generator(n):
    n += 1
    color = {}
    for i in range(n + 1):
        color[i] = int((i / n) * 255)
    return color



im = cv2.imread("./mug.jpg", cv2.IMREAD_GRAYSCALE)
# print(im)
im = darken_edges(im, 100)
points = stippling_points(im)
cv2.imwrite("darkened.png",im)
# print(points)
print(color_generator(5))

white = [[[255, 255, 255] for x in range(len(im[0]))] for x in range(len(im))]

white = np.asarray(white)

for point in points:
    white[point[0][1]][point[0][0]] = [0, 0, 0]

cv2.imwrite("output.png", white)



