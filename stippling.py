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

#
# image is expected to be a grayscale cv2 image
# 
def stippling_points(image):
    points = []

    for i, row in enumerate(image):
        for j, col in enumerate(image[i]):
            r = random.randint(0, 255)
            if r > image[i][j]:
                points.append([(j, i)])
    return points
#
# image is expected to be a grayscale cv2 image
# 
def stippling_points_jitter(image):
    points = []

    for i, row in enumerate(image):
        for j, col in enumerate(image[i]):
            r = random.randint(0, 255)
            if r > image[i][j]:
                points.append([(j + np.random.normal(0,.3,None), i + np.random.uniform(0,.3,None))])

    return points


#
# runs edgepoints, goes to the designated edgepoints and darkens them by a 
# parameterized value
#
# for some reason the image is some combination or rotations and transposes and 
# I don't know why
#

def darken_edges(image, darken):
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    sys.path.append('..')
    from EdgePoints import edgepoints as ep

    edges = cv2.Canny(image, 50, 100)

    edge_points = ep.generate_edgepoints(edges)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


    for line in edge_points:
        for point in line:
            print(point)
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
# colors[-1] = white
#
def color_generator(n):
    n += 1
    color = {}
    for i in range(n + 1):
        color[i] = int((i / n) * 255)
    return color


#
# saves a digital stippling image to ./outputs
# 
# @param fn: string filename of an image you would like to generate digital 
# stippling of
#
def main(fn):
    im = cv2.imread(fn, cv2.IMREAD_GRAYSCALE)
    im = np.transpose(im)
    im = darken_edges(im, 200)

    jpoints = stippling_points_jitter(im)
    points = stippling_points(im)
    print("saving darkened-edge image")
    cv2.imwrite("./outputs/darkened.png",im)

    #print(jpoints)
    #print(color_generator(5))

    white = [[[255, 255, 255] for x in range(len(im[0]))] for x in range(len(im))]

    white = np.asarray(white)

    for point in points:
        white[point[0][0]][point[0][1]] = [0, 0, 0]

    cv2.imwrite("./outputs/output.png", white)
    print("saving output image")

if __name__ == "__main__":
    FILENAME = "./davidlynchportrait.png"
    main(FILENAME)


