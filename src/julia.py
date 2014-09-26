import argparse
import renderer
from cmath import *  # has to be loaded this way for user input parsing


def main():
    """ Main loop, acts as a command-line wrapper for the renderer. """
    parser = argparse.ArgumentParser(description="Generates a Julia set for the given equation.")
    parser.add_argument("equation", action="store", nargs='+',
                        help="The equation to generate the Julia set from. Use z as complex variable name, and general python syntax.")
    parser.add_argument("-b", dest="blowup", action="store", metavar="int", type=int,
                        help="Specify the blowup value for iterations. Default is 2.")
    parser.add_argument("-x", dest="xinterval", action="store", nargs=2, metavar=('x1', 'x2'), type=float,
                        help="The interval on the real numbers the image should operate on. Default is [-1, 1].")
    parser.add_argument("-y", dest="yinterval", action="store", nargs=2, metavar=('y1', 'y2'), type=float,
                        help="The interval on the imaginary numbers the image should operate on. Default is [-1, 1].")
    parser.add_argument("-i", dest="iterations", action="store", metavar='int', type=int,
                        help="Specify the maximum number of iterations for a point. Default is 255.")
    parser.add_argument("-s", dest="size", action="store", nargs=2, metavar=('h', 'v'), type=int,
                        help="Specify the size of the image to be generated.\nThe default size is 320x320.")
    parser.add_argument("-f", dest="file", action="store", metavar="filename",
                        help="File to save the rendering to. Defaults to julia.png")

    # process user input, set to defaults if not provided
    args = parser.parse_args()
    equation    = " ".join(args.equation)
    blowup      = args.blowup      if args.blowup     else 2
    xinterval   = args.xinterval   if args.xinterval  else (-1, 1)
    yinterval   = args.yinterval   if args.yinterval  else (-1, 1)
    iterations  = args.iterations  if args.iterations else 255
    size        = tuple(args.size) if args.size       else (320, 320)
    file        = args.file        if args.file       else "julia.png"

    # test the equation
    try:
        z = 1.5
        eval(equation)
    except (ArithmeticError, SyntaxError, NameError, ValueError):
        print("Error: not a valid equation.")
        return

    renderer.rendertoimage(equation, blowup, xinterval, yinterval, iterations, size, file)

if __name__ == "__main__":
    main()