# Jorge Nocedal · 代表作候选摘要

> 来自OpenAlex，仅供筛选精读对象。引用前请回到原文核对。

## Updating quasi-Newton matrices with limited storage

1980 · Mathematics of Computation · 被引2760 · https://doi.org/10.1090/s0025-5718-1980-0572855-7

We study how to use the BFGS quasi-Newton matrices to precondition minimization methods for problems where the storage is critical. We give an update formula which generates matrices using information from the last m iterations, where m is any number supplied by the user. The quasi-Newton matrix is updated at every iteration by dropping the oldest information and replacing it by the newest information. It is shown that the matrices generated have some desirable properties. The resulting algorithms are tested numerically and compared with several well-known methods.

## Global Convergence Properties of Conjugate Gradient Methods for Optimization

1992 · SIAM Journal on Optimization · 被引1072 · https://doi.org/10.1137/0802003

This paper explores the convergence of nonlinear conjugate gradient methods without restarts, and with practical line searches. The analysis covers two classes of methods that are globally convergent on smooth, nonconvex functions. Some properties of the Fletcher–Reeves method play an important role in the first family, whereas the second family shares an important property with the Polak–Ribière method. Numerical experiments are presented.

## Remark on “algorithm 778: L-BFGS-B: Fortran subroutines for large-scale bound constrained optimization”

2011 · ACM Transactions on Mathematical Software · 被引464 · https://doi.org/10.1145/2049662.2049669

This remark describes an improvement and a correction to Algorithm 778. It is shown that the performance of the algorithm can be improved significantly by making a relatively simple modification to the subspace minimization phase. The correction concerns an error caused by the use of routine dpmeps to estimate machine precision.

## Optimization Methods for Large-Scale Machine Learning

2018 · SIAM Review · 被引3255 · https://doi.org/10.1137/16m1080173

Abstract. This paper provides a review and commentary on the past, present, and future of numerical optimization algorithms in the context of machine learning applications. Through case studies on text classification and the training of deep neural networks, we discuss how optimization problems arise in machine learning and what makes them challenging. A major theme of our study is that large-scale machine learning represents a distinctive setting in which the stochastic gradient (SG) method has traditionally played a central role while conventional gradient-based nonlinear optimization techniques typically falter. Based on this viewpoint, we present a comprehensive theory of a straightforward, yet versatile SG algorithm, discuss its practical behavior, and highlight opportunities for designing algorithms with improved performance. This leads to a discussion about the next generation of optimization methods for large-scale machine learning, including an investigation of two main streams of research on techniques that diminish noise in the stochastic directions and methods that make use of second-order derivative approximations.

## An investigation of Newton-Sketch and subsampled Newton methods

2020 · Optimization methods & software · 被引98 · https://doi.org/10.1080/10556788.2020.1725751

Sketching, a dimensionality reduction technique, has received much attention in the statistics community. In this paper, we study sketching in the context of Newton's method for solving finite-sum optimization problems in which the number of variables and data points are both large. We study two forms of sketching that perform dimensionality reduction in data space: Hessian subsampling and randomized Hadamard transformations. Each has its own advantages, and their relative tradeoffs have not been investigated in the optimization literature. Our study focuses on practical versions of the two methods in which the resulting linear systems of equations are solved approximately, at every iteration, using an iterative solver. The advantages of using the conjugate gradient method vs. a stochastic gradient iteration are revealed through a set of numerical experiments, and a complexity analysis of the Hessian subsampling method is presented.
