"""Exact rational checks accompanying the analytic proof."""
from fractions import Fraction as F
from itertools import product

hist = [0, 0, 0]
for sample in product((0, 1), repeat=2):
    hist[sum(sample)] += 1
assert [F(x, 4) for x in hist] == [F(1, 4), F(1, 2), F(1, 4)]
r, p = F(4, 5), F(3, 4)
a0 = F(12) / F(3, 4)
a1 = 1 / F(3, 4)
assert 1 / (1-p)**2 == a0 == 16
assert F(1, 4) / (p*(1-p)) == a1 == F(4, 3)
assert a0*(1-r)**2 + a1*2*r*(1-r) == F(16, 15) > 1
assert (r-p) / 4 == F(1, 80)
# Polynomial 3*[a0*(1-r)^2 + a1*2*r*(1-r)-1].
assert 3*(a0*(1-r)**2 + a1*2*r*(1-r)-1) == 40*r*r-88*r+45
assert 88**2-4*40*45 == 16*34
assert 34 < 6**2  # stronger lower gap > 1/80
catoni_p = (1 - F(1, 4)) / (1 - F(1, 12))
assert catoni_p == F(9, 11)
assert F(3, 4)*(catoni_p-p) == F(9, 176)
print("PASS: all four sample outcomes, rational obstruction and gap, stronger-root algebra, Catoni upper bound.")
