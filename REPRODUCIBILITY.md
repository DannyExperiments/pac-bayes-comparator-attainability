# Reproduce the checks

Use an existing Python 3.11 or compatible interpreter. The replay has no external dependencies.

    python3 -B -I scripts/verify_repository.py
    python3 -B -I verification/src/replay.py

Use Lean 4.30.0 with its bundled standard library for the partial certificate.

    lean -DwarningAsError=true formal/Q949Certificate.lean

The seven declarations check the two-term polynomial, sample counts, example thresholds, rational contradiction, discriminant and rational gap estimates. They do not formalize the real-valued comparator argument or the distribution-free estimate. [Paper build](paper/BUILD.md) · [Visualization guide](visualization/README.md)
