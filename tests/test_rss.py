import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src/rss'))

from line import rss_regression as line_rss_regression
from parabola import rss_regression as parabola_rss_regression

line_test_dataset = [(0, 1), (2, 3), (3, 5)]
line_coeffs = line_rss_regression(1, 0, line_test_dataset, 0.001, 1000)
assert round(line_coeffs[0], 3) == 1.326 \
       and round(line_coeffs[1], 3) == 0.759

line_test_dataset = [(1, 2), (3, 4), (5, 5.5), (7.5, 8)]
line_coeffs = line_rss_regression(1, 0, line_test_dataset, 0.001, 10000)
assert round(line_coeffs[0], 3) == 0.908 \
       and round(line_coeffs[1], 3) == 1.128


parabola_test_dataset = [(1, 2), (3, 0.5), (-1, 0), (7.5, -7)]
parabola_coeffs = parabola_rss_regression(1, 0, 0, parabola_test_dataset, 0.0001, 100000)
assert round(parabola_coeffs[0], 3) == -0.228 \
       and round(parabola_coeffs[1], 3) == 0.627 \
       and round(parabola_coeffs[2], 3) == 1.061

parabola_test_dataset = [(0, 2), (1, 0), (2, 1), (3, 1)]
parabola_coeffs = parabola_rss_regression(1, 0, 0, parabola_test_dataset, 0.008766)
assert round(parabola_coeffs[0], 3) == 0.495 \
       and round(parabola_coeffs[1], 3) == -1.685 \
       and round(parabola_coeffs[2], 3) == 1.792
