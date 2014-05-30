import argparse
import renderer
from math import *  # has to be loaded this way for user input parsing


def main():
    parser = argparse.ArgumentParser(description="Generates a Julia set for the given equation.")
    parser.add_argument("equation", action="store", nargs='+',
                        help="The equation to generate the Julia set from. Use z as complex variable name.")
    parser.add_argument("-s", "--size", dest="size", action="store", nargs=2, metavar=('h', 'v'),
                        help="Specify the size of the image to be generated.\nThe default size is 320x320.")

    args = parser.parse_args()
    equation = " ".join(args.equation)
    size = (args.size[0], args.size[1]) if args.size else (320, 320)

    try:
        z = 1
        eval(equation)
    except (ArithmeticError, SyntaxError, NameError, ValueError):
        print("Error: not a valid equation.")
        return

    renderer.rendertoimage(equation, size)

if __name__ == "__main__":
    main()