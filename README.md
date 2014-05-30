# Julia Set renderer

Julia set renderer in Python using PIL.

<div style="float: right">
    <img src="https://raw.githubusercontent.com/TimonKnigge/julia-set-renderer/master/samples/sample1.png" alt="Julia Set of a quadratic polynomial" title="Julia Set of a quadratic polynomial"/>
</div>

### Usage

#### Command line

This module is intended to be used using the commandline. For example, the command used to generate the above image is:
`
python julia.py z**2 - 0.7 + 0.27015j
`
(actually, I specified a few extra flags as not to generate an image that fills the entire screen, but the above command will give you the same image, just at a higher resolution)

There are a lot of flags that allow you to customize the image, use `python julia.py -h` to find out more.

#### As a module

The renderer can also be used as a module. You will only need the `renderer.py` file to do this, `julia.py` acts as a cmd-wrapper for this module. **Note:** Python's built-in `eval()` function is used to evaluate the equation. Letting users specify the equation without filtering it yourself is therefore **unsafe**.

### More samples

(working on it)