# EasyBadApple
An easily portable monochrome "Bad Apple!!" video in a compact file.

## How to build
To build your .dat file, run the generate.py file in Python.

If you want to import your own video, save the frames as an RGB PNG sequence and place it in the "frames" folder. The program will automatically determine if a pixel should be black or white.

Playing a file will require you to specify the `frame_rate` value in `main.py`, by default it is set to 10fps (0.1 seconds).
By default, the resolution of the video is 64x32 pixels. You will also need to specify this in `main.py` with the `res` variable.

## File specifics
The file is stored in 1bpp, meaning there is one bit for each pixel (1 is white, 0 is black).
This may be hard to script on some devices, so I may write an option for each pixel to be a byte (`FF` is white, `00` is black)

Also note that the output file may need to be split into smaller chunks for devices with low RAM and no file stream capabilities.

## Example pseudocode
(This code probably has some errors, as it was transferred from Python to C-like syntax)

```c
int[] res = {64, 32};
float fps = 0.1;
bytes[] ba_data = File.Open("badapple.dat", "rb");
int frames = ba_data.length * 8 / (res[0] * res[1]);

for (int frame = 0; frame < frames; frame++)
{
    int[,] frame_data = new int[res[0], res[1]];
    int bit = 0;
    int byte_offset = ((res[0] * res[1]) / 8) * frame;
    for (int x = 0; x < res[0]; x++)
    {
        for (int y = 0; y < res[1]; y++)
        {
            if ((ba_data[byte_offset + (bit / 8)] >> (7 - bit) % 8) & 1)
            {
                frame_data[x, y] = 255;
            } else
            {
                frame_data[x, y] = 0;
            }
            bit++;
        }
                    
    }
    display.clear();
    display.image(frame_data);
    sleep(fps);
}
```
