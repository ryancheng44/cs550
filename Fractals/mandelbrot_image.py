'''
Ryan Cheng
11/10/23
Sources: ChatGPT for color functions for third image (burning ship fractal)
Reflection: I really enjoyed this project. I've always been fascinated by fractals, so it was great to be
			able to make some myself. I was especially fond of my burning ship fractal; I think it looks so
			cool. It's quite simple as well. Instead of squaring z like in the Mandelbrot set, we square
			the absolute value of z. It's mindblowing how such a small change can make such a big visual
			difference. Furthermore, I was quite surprised that ChatGPT was able to create such interesting
			color fuctions. The color choices for the other two images were a bit more deliberate. I really
			love the colors mint green, orange-red, and light blue, hence why I chose to use them in my
			first and second images. One thing that confused me a bit that I still haven't resolved is how
			my Mandelbrot function interacts with negative xmin/xmax/ymin/ymax values. I was trying to find
			Seahorse Valley for my second image, which is in the negatives, and for some reason, the y
			coordinates seemed to act in reverse. Regardless, I was able to find it eventually. In the
			future, I'd like to make an interactive fractal viewer, where the user can zoom in infinitely,
			or at least close to it.
Feedback:
    Sebastian Plunkett: I think you could dry up your code by creating a function that creates these images.
    You repeated your code for fractal image generation three times.
    Addressed: I created a function that creates the images.
    Leon Gopaul: I really like your burning ship fractal. The color scheme is really cool. However, I think
    you should explain how you got the color functions for the first two images.
    Addressed: I explained how I got the color functions for the first two images.
On my honor, I have neither given nor received unauthorized aid: Ryan Cheng
'''

from PIL import Image
import numpy as np


def mandelbrot(c, z=complex(0, 0), count=0):
    count += 1
    znew = z ** 2 + c

    if abs(znew) >= 2 or count >= 255:
        return count
    return mandelbrot(c, znew, count)

# burning ship fractal


def burning_ship(c, z=complex(0, 0), count=0):
    count += 1
    # instead of squaring z, we square the absolute value of z
    znew = (abs(z.real) + abs(z.imag) * 1j) ** 2 + c

    if abs(znew) >= 2 or count >= 255:
        return count
    return burning_ship(c, znew, count)

# color functions for first image; meant to be shades of mint
# essentially, (69, 186, 147) is the RGB value of the mint
# and based on numescape which gets passed in as x, I subtract a proportional amount from each value
# so that lower values of numescape are closer to the mint color
# and higher values of numescape are closer to black


def r_1(x):
    return 69 - int(69 * x / 255)


def g_1(x):
    return 186 - int(186 * x / 255)


def b_1(x):
    return 147 - int(147 * x / 255)

# color functions for second image; meant to have shades of red and blue based on even/odd
# the code for the shades is the same as the code for the shades of mint


def r_2(x):
    if x % 2 == 0:
        return 189 - int(189 * x / 255)
    return 254 - int(254 * x / 255)


def g_2(x):
    if x % 2 == 0:
        return 213 - int(213 * x / 255)
    return 95 - int(95 * x / 255)


def b_2(x):
    if x % 2 == 0:
        return 234 - int(234 * x / 255)
    return 85 - int(85 * x / 255)

# color functions for third image; I got this from ChatGPT and I thought it looked too cool to pass up
# np.exp(x) is e^x


def r_3(x):
    return int(255 * (1 - np.exp(-x / 50)))


def g_3(x):
    return int(255 * (1 - np.exp(-x / 30)))


def b_3(x):
    return int(255 * (1 - np.exp(-x / 20)))

# r, g, and b are functions that I pass into this function to determine the color of each pixel
# fractal is a function that I pass into this function to determine the fractal to be drawn


def make_image_with(dimx, dimy, xmin, xmax, ymin, ymax, r, g, b, fractal=mandelbrot):
    image = Image.new("RGB", (dimx, dimy))

    # determine relationship between x and y coordinates of image and real and imaginary parts of complex number
    xm = (xmax - xmin) / (dimx - 1)
    xb = xmin

    ym = (ymax - ymin) / (dimy - 1)
    yb = ymin

    for i in range(0, dimy):
        for j in range(0, dimx):
            numescape = fractal(complex(xm * j + xb, ym * i + yb))
            color = (r(numescape), g(numescape), b(numescape))
            image.putpixel((j, i), color)

    image.show()


make_image_with(1000, 1000, 0.35, 0.4, 0.35, 0.4, r_1, g_1, b_1)
make_image_with(1000, 1000, -0.875, -0.625, -0.25, 0, r_2, g_2, b_2)
make_image_with(1000, 1000, -1.8, -1.7, -0.08,
                0.01, r_3, g_3, b_3, burning_ship)
