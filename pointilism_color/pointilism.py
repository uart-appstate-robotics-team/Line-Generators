import numpy as np
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
# @param minimum_difference: optional parameter that is added to each 
#    difference before they are normalized
#
def get_ratio_of_colors(pixel_color, color_list, minimum_difference=0):
    #TODO: make the differences more similar to how the human eye percieves them

    #compute differences
    differences = [np.linalg.norm(pixel_color - b) + minimum_difference for b in color_list]

    #pivot them around THE_MAGIC_CONSTANT/2
    flip_differences = list(map(flip_function, differences))

    #normalize to create a probability vector
    ratios = np.array(flip_differences)/sum(flip_differences)

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
# @param ratio of colors in the 
#
def get_color(ratio, color_dict):
    pass

def generate(image, color_dict):
    pass

def main():
    colors = {'red':(255,39,18),'yellow':(255,255,51),
        'white':(255,255,255),'blue':(0,69,252), 'black':(0,0,0)}
#    pixel_color = np.array([100, 149, 237])

    pixel_color = np.array((0,69,252))

    color_values = np.array(list(colors.values()))

    ratio = get_ratio_of_colors(pixel_color
        , np.array(list(colors.values()))
        , minimum_difference=25)

    ratio = get_ratio_of_colors(pixel_color
        , np.array(list(colors.values()))
        , minimum_difference=0)

if __name__ == "__main__":
    main()
