from sympy import fourier_series, pi, plot
from sympy.abc import x

f = x**2  #Defined f(x) = x^2


def show_fourier(range1: float, range2: float, plot_range1: float, plot_range2: float):
    s = fourier_series(f, (x, range1, range2))

    s1 = s.truncate(n = 3)

    s2 = s.truncate(n = 5)

    s3 = s.truncate(n = 100)

    p = plot(f, s1, s2, s3, (x, plot_range1, plot_range2), show=False, legend=True)

    p[0].line_color = (0, 0, 0)

    p[0].label = 'x'

    p[1].line_color = (1, 0.7, 0.7)

    p[1].label = 'n=3'

    p[2].line_color = (0.5, 1, 0.5)

    p[2].label = 'n=5'

    p[3].line_color = (0.3, 0.3, 1)

    p[3].label = 'n=100'

    p.show()


show_fourier(0, 2, -20, 20)