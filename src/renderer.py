from PIL import Image, ImageDraw
from cmath import *


def rendertoimage(equation, blowup, _xinterval, _yinterval, iterations, _resolution, filename):
    # save globally so they can be used by renderer.pixeltocomplex
    global xinterval, yinterval, resolution
    xinterval = _xinterval
    yinterval = _yinterval
    resolution = _resolution

    image = Image.new("RGB", resolution)

    for x in range(resolution[0]):
        for y in range(resolution[1]):
            z = pixeltocomplex(x, y)
            i = 0
            while (i < iterations) and (abs(z) < blowup):
                z = eval(equation)
                i += 1
            v = int((i / iterations) * 255)
            image.putpixel((x, y), (v, v, v))

    # z = 2
    # print(eval(equation))
    #image.putpixel((1, 2), (255, 0, 255))

    image.save(filename, "PNG")


def pixeltocomplex(xpos, ypos):
    """ Uses linear interpolation to convert an image coordinate to its complex value. """
    re = (xpos / resolution[0]) * (xinterval[1] - xinterval[0]) + xinterval[0]
    im = (ypos / resolution[1]) * (yinterval[1] - yinterval[0]) + yinterval[0]
    return complex(re, im)