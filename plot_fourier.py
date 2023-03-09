from sympy import fourier_series, pi, plot
from sympy.abc import x

f = x**2

s = fourier_series(f, (x, -pi, pi))

s1 = s.truncate(n = 3)

s2 = s.truncate(n = 5)

s3 = s.truncate(n = 7)

p = plot(f, s1, s2, s3, (x, -3*pi, 3*pi), show=False, legend=True)

p[0].line_color = (0, 0, 0)

p[0].label = 'x'

p[1].line_color = (0.7, 0.7, 0.7)
