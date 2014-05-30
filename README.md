## Julia Set renderer

Julia set renderer in Python using PIL.

![Sample image](https://raw.githubusercontent.com/TimonKnigge/julia-set-renderer/master/samples/sample1.png)

#### Usage

Example:
`
python julia.py z**2 - 0.4
`

#### Warning: unsafe

Python's built-in `eval()` function is used to evaluate the equation. Letting users specify the equation without filtering it yourself is therefore **unsafe**.