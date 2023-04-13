# generate_file.py
# Used to generate an easily readable, compact bad apple video file.
# Generated files are 1bpp frames, similar to the .RAW image format
# Resolution is dependant on the input sequence's resolution
# Do not mix image resolutions in the same sequence, it will break
# the images in 'frames/' will be sorted alphabetically/numerically

import PIL.Image
import os

def bitsToBytes(a):
    s = i = 0
    for x in a:
        s += s + x
        i += 1
        if i == 8:
            yield s
            s = i = 0
    if i > 0:
        yield s << (8 - i)

frames_dir = 'frames/' # Keep / at the end!
output_file = 'badapple.dat'

out_file = open(output_file, 'wb')
bits = []
percent_counter = 0

for dirpath, dirnames, filenames in os.walk(frames_dir, True):
    for file in filenames:
        image = PIL.Image.open(frames_dir + file)
        bit_counter = 0
        for x in range(image.width):
            for y in range(image.height):
                if bit_counter > 7:
                    out_file.write(bytes(bitsToBytes(bits)))
                    bit_counter = 0
                    bits = []
                bits.append(image.getpixel((x, y)) > (128, 128, 128))
                bit_counter += 1
        if percent_counter % 100 == 0:
            print(str(round(percent_counter / len(filenames) * 100)) + '%')
        percent_counter += 1
if bit_counter != 0:
    out_file.write(bytes(bitsToBytes(bits)))

print('frames: ' + str(len(filenames)))
print('Done')