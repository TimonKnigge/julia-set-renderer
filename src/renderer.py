from PIL import Image, ImageDraw
from cmath import *


def rendertoimage(equation, blowup, xinterval, yinterval, iterations, resolution, filename):
    """ Renders the Julia set. For more info on parameters, use python julia.py -h """

    image = Image.new("RGB", resolution)

    for x in range(resolution[0]):
        for y in range(resolution[1]):
            z = pixeltocomplex(x, y, xinterval, yinterval, resolution)
            i = 0
            while (i < iterations) and (abs(z) < blowup):
                try:
                    z = eval(equation)
                except (ArithmeticError, SyntaxError, NameError, ValueError):
                    break
                i += 1
            image.putpixel((x, y), iterationstopixel(i, iterations))

    image.save(filename, "PNG")


def pixeltocomplex(xpos, ypos, xinterval, yinterval, resolution):
    """ Uses linear interpolation to convert an image coordinate to its complex value. """
    re = (xpos / resolution[0]) * (xinterval[1] - xinterval[0]) + xinterval[0]
    im = (ypos / resolution[1]) * (yinterval[1] - yinterval[0]) + yinterval[0]
    return complex(re, -im)


def iterationstopixel(i, iterations):
    """ Assigns a color based on iteration count. You can implement your own color function here. """
    d = int(i / iterations * 255)
    return d, d, d