# Julia Set renderer

Julia set renderer in Python using PIL.

![Sample image](https://raw.githubusercontent.com/TimonKnigge/julia-set-renderer/master/samples/sample1.png)

(more samples can be found [here](/samples/))

### Usage

#### Command line

This module is intended to be used using the commandline. For example, the command used to generate the above image is: `python julia.py z**2 - 0.7 + 0.27015j` (actually, I specified a few extra flags as not to generate an image that fills the entire screen, but the above command will give you the same image, just at a higher resolution).

There are a lot of flags that allow you to customize the image, use `python julia.py -h` to find out more.

The only thing you can't specify using flags is how colors are picked based on iterations, since this process is to complex to capture in a flag. By default, a grayscale color will be picked using linear interpolation. However, you can define your own function in `renderer.py`, for example, the second sample uses this function:
```Python
def iterationstopixel(i):
    delta = i / iterations
    r = min(3 * delta, 1) * 256
    g = max(min(3 * delta - 1, 1), 0) * 256
    b = max(min(3 * delta - 2, 1), 0) * 256
    return int(r), int(g), int(b)
```

#### As a module

The renderer can also be used as a module. You will only need the `renderer.py` file to do this, `julia.py` acts as a cmd-wrapper for this module. **Note:** Python's built-in `eval()` function is used to evaluate the equation. Letting users specify the equation without filtering it yourself is therefore **unsafe**.