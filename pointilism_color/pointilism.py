import numpy as np
import cv2
#
# goal is to generate pointilism paintings
# https://en.wikipedia.org/wiki/Pointillism
#
# Uses a similar algorithm as the stippling_color but incorporates multiple 
# colors instead of lightness
#

# the maximum distance between two colors
# np.linalg.norm([255,255,255] - [0,0,0])
THE_MAGIC_CONSTANT = 441.6729559300637

#
# Creates a list of differences, normalizes that list and then returns
#
# @param pixel_color: RGB color value of a given pixel
# @param color_list: list of RGB color values
# @param ratio_squish: optional parameter that is added to each 
#    difference before they are normalized
#
def get_ratio_of_colors(pixel_color, color_list, ratio_squish):
    #print("pixel_color", pixel_color)
    #print("color_list", color_list)
    #TODO: make the differences more similar to how the human eye percieves them

    #compute differences
    differences = [np.linalg.norm(pixel_color - b) + ratio_squish for b in color_list]


    #pivot them around THE_MAGIC_CONSTANT/2
    flip_differences = np.array(list(map(flip_function, differences)))

    # ruins mathematical purity but eh?
    # filter out negative by just making them zero and then normalizing again
    flip_differences = [x if x > 0 else 0 for x in flip_differences ]

    #normalize to create a probability vector
    ratios = flip_differences/sum(flip_differences)
    # print(ratios)

    return ratios

#
# Flips values around THE_MAGIC_CONSTANT/2
# y = -x + THE_MAGIC_CONSTANT
#
# @param value: value you want to flip
#
def flip_function(value):
    return -1*value + THE_MAGIC_CONSTANT


#
# returns the key of the color to be used
#
# @param ratio: a ratio made by comparing the similarity of a pixel's color 
#     with the color of all colors in the color_dict
#
def get_color(ratio, color_dict):
    #print("color_dict",color_dict)
    keys = color_dict.keys()

    return np.random.choice(list(keys), p=ratio)


#
# Simply goes to each pixel and randomly selects a color from get_color using
# a distribution generated from get_ratio_of_colors and color_dict. Places
# that color at [0] of each element of the points list.
#   
# @param image: (M,N,3) matrix
# @param color_dict: dictionary of name:triple pairs that define RGB colors and their names
# @param ratio_squish: the more negative this number is the flatter the distribution will be
#      and thus the more random the colors will be, positive numbers will 
#      heighten the distribution
# 
# @return: list of tuples where:
#      [0] = key into color_dict
#      [1] = coordinate value of the point
#
def generate(image, color_dict, ratio_squish=0):
    #print("image",image)
    #print("color_dict",color_dict)
    points = [[]]
    color_values = np.array(list(color_dict.values()))
    for i, row in enumerate(image):
        for j, element in enumerate(row):
            ratio = get_ratio_of_colors(element, color_values, ratio_squish)
            color = get_color(ratio, color_dict)
            points[-1].append(color)
            points[-1].append( (i,j) )

            points.append([])

    del points[-1]
    print(points)
    return points


#TODO: shuffle function that shuffles a points list from generate() in order to 
# layer the points more interestingly


#
# generates points from an image and then constructs a new image using those 
# colors and points
#
def main(colors, image):
    #print(get_ratio_of_colors((0,140,214),np.array(list(colors.values())), 50))

    points = generate(image, colors, ratio_squish=200)
    #print(points)
    for point in points:
        image[point[1][0]][point[1][1]] = colors[point[0]]

    cv2.imwrite("./outputs/output.png", image)

if __name__ == "__main__":
    colors = {
        'red':(255,39,18),
        'yellow':(255,255,51),
        'white':(255,255,255),
        'blue':(0,69,252),
        'magenta':(255,51,230),
        'violet':(122,51,255),
        'orange':(255,151,51),
        'green':(20,140,30)
        }
    image = cv2.imread("./images/colorful-flowers.jpg")
    main(colors, image)
