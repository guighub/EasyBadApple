import os.path
import time
import PIL.Image as Image
import numpy as np
import matplotlib.pyplot as plt

file_name = 'badapple.dat' # File to read from
res = (64, 32) # Resolution of video (x, y)
frame_rate = 0.1 # FPS in milliseconds
color_black = (0, 0, 0) # Black color
color_white = (255, 255, 255) # White color

def divmod(a, b):
    return (a % b, a // b)

if os.path.isfile(file_name) == False:
    print("Unable to find badapple.dat!")
    print("The file must be in the same directory as main.py\n")
    time.sleep(1.5)
else:
    ba_data = open(file_name, 'rb').read()
    frames = len(ba_data * 8) // (res[0] * res[1])
    print("Video resolution: " + str(res[0]) + "x" + str(res[1]))
    print("Frames: " + str(frames))
    img = np.asarray(Image.new('RGB', res, color_black))
    imgplot = plt.imshow(img)

    for frame in range(frames):
        image = Image.new('RGB', res, color_black)
        bit = 0
        byte_offset = ((res[0] * res[1]) // 8) * frame
        for x in range(res[0]):
                for y in range(res[1]):
                    if (ba_data[byte_offset + (bit // 8)] >> (7 - bit) % 8) & 1:
                        image.putpixel((x, y), color_white)
                    bit += 1
        
        img = np.asarray(image)
        imgplot.set_data(img)
        print('frame ' + str(frame))
        plt.pause(frame_rate)
        image.close()