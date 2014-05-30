from PIL import Image, ImageDraw
from cmath import *


def rendertoimage(equation, blowup, _xinterval, _yinterval, _iterations, _resolution, filename):
    # save globally so they can be used by renderer.pixeltocomplex and renderer.iterationstopixel
    global xinterval, yinterval, resolution, iterations
    xinterval = _xinterval
    yinterval = _yinterval
    resolution = _resolution
    iterations = _iterations

    image = Image.new("RGB", resolution)

    for x in range(resolution[0]):
        for y in range(resolution[1]):
            z = pixeltocomplex(x, y)
            i = 0
            while (i < iterations) and (abs(z) < blowup):
                z = eval(equation)
                i += 1

            image.putpixel((x, y), iterationstopixel(i))

    image.save(filename, "PNG")


def pixeltocomplex(xpos, ypos):
    """ Uses linear interpolation to convert an image coordinate to its complex value. """
    re = (xpos / resolution[0]) * (xinterval[1] - xinterval[0]) + xinterval[0]
    im = (ypos / resolution[1]) * (yinterval[1] - yinterval[0]) + yinterval[0]
    return complex(re, im)


def iterationstopixel(i):
    delta = i / iterations
    r = min(3 * delta, 1) * 256
    g = max(min(3 * delta - 1, 1), 0) * 256
    b = max(min(3 * delta - 2, 1), 0) * 256
    return int(r), int(g), int(b)