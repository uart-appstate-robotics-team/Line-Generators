import cv2
import numpy as np

def get_closest_color(available_pixel, chosen_pixel):
    distances = []
    
    for key, value in available_pixel.items():
        a1 = np.asarray(value)
        c1 = np.asarray(chosen_pixel)
        curr_dist = np.linalg.norm(a1 - c1)
        distances += [curr_dist]
        if(curr_dist <= min(distances)):
            curr_key = key

    return curr_key

#
# generates lines that draws diagnol lines to fill adjacent spaces with their closest color
#
def generate_diagnol_fill(image, color_dict):
    print(color_dict)

    diag_list = list(range(len(image),0,-1))
    #print(diag_list)
    
    x_list = list(range(len(image[0])))
    #print(x_list)
    diag_list.extend(x_list)
    #print(diag_list)
    #print('starting_diags', diag_list)

    y_decrement = True  #initialize
    prev_closest = None
    lines = []
    for i in diag_list:
        if i == 0:
            y_decrement = False
        if y_decrement:
            y = i
            x = 0
        else:
            y = 0
            x = i


        while x < len(image[0]) and y < len(image):
            closest_color = get_closest_color(color_dict, image[y][x])
            if closest_color is not prev_closest:
                lines.append([closest_color])
            xy = (x,y)
            lines[-1].append(xy)
            x += 1
            y += 1
            prev_closest = closest_color

    return lines

colors = {'red':[255,0,0], 'green':[0,255,0], 'blue':[0,0,255],'magenta':[255,0,255], 'tomato':[255,99,71], 'lawn green':[124,252,0], 'yellow':[255,217,41]}
img = cv2.imread("./flower.jpg")
lines = generate_diagnol_fill(img,colors)
#print(lines)
