# Explore a shared binomial moment

[Download the offline explorer ZIP](https://raw.githubusercontent.com/DannyExperiments/pac-bayes-comparator-attainability/v1.0.0/visualization/pac-bayes-comparator-attainability-explorer.zip), extract it, and open index.html. Adjust the probe r to see the required subtotal, and rotate the stack to see the two contributions and the budget line.

The lower bound uses the 0-error and 1-error terms of the same normalized two-trial binomial moment. If both samplewise inversions are below r, the respective terms strictly exceed 16(1−r)² and (8/3)r(1−r). At r = 4/5 these subtotal to 16/15. The budget is one. At least one branch must have inversion at least r.

The GIF uses the exact rational probe. The explorer shows rounded values at other probes. The paper proves the sharper algebraic-root bound and the Catoni upper estimate.

To render the GIF, use an existing Python environment with Pillow and Arial or DejaVu Sans available.

    python3 visualization/render.py
