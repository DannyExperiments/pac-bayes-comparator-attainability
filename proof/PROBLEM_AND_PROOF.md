# Problem and proof

The generic PAC-Bayes theorem uses a prechosen convex comparator. Its binomial exponential moment factor shifts the level of the samplewise upper inversion. The optimistic KL benchmark drops this factor. The source asks if one comparator always attains that benchmark in expectation. [Open Problem 1](https://proceedings.neurips.cc/paper_files/paper/2021/file/214cfbe603b7f9f9bc005d5f53f7a1d3-Paper.pdf#page=10)

Use two iid fair labels and hypotheses that always make the same prediction on the supported input. Give one hypothesis prior mass $1/12$. When both labels are zero choose its point mass as the posterior, and otherwise keep the prior. For $\delta=3/4$ the data law gives the following values.

| Empirical risk | Posterior-prior KL | Probability | Optimistic upper inversion |
| --- | --- | --- | --- |
| 0 | $\log 12$ | $1/4$ | $3/4$ |
| $1/2$ | 0 | $1/2$ | $3/4$ |
| 1 | 0 | $1/4$ | 1 |

Normalize each comparator to have binomial exponential moment at most 1. Convexity and change of measure show it lies pointwise below Bernoulli KL in the interior of the second argument. Its inversion is therefore at least the optimistic inversion in each branch.

If both first-row and second-row inversions are below an interior probe $r$, their two binomial moment terms at $r$ have sum strictly greater than $L(r)=16(1-r)^2+(8/3)r(1-r)$. At $L(r)=1$ this is impossible. The smaller root is $(22-\sqrt{34})/20$. At least one of two branches of probability at least $1/4$ exceeds its ideal by at least $r-3/4$. This forces an expected gap of at least $(7-\sqrt{34})/80$.

The fixed Catoni comparator with $\beta=\log12$ gives both first-row inversions $9/11$, hence the concrete upper bound $9/176$. The paper also derives a distribution-free upper estimate using the ordinary KL comparator. [Full proof](../paper/manuscript.pdf)
