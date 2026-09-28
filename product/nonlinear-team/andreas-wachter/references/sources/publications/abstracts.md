# Andreas Wächter · 代表作候选摘要

> 来自OpenAlex，仅供筛选精读对象。引用前请回到原文核对。

## Branching and bounds tighteningtechniques for non-convex MINLP

2009 · Optimization methods & software · 被引607 · https://doi.org/10.1080/10556780903087124

Many industrial problems can be naturally formulated using mixed integer non-linear programming (MINLP) models and can be solved by spatial Branch&Bound (sBB) techniques. We study the impact of two important parts of sBB methods: bounds tightening (BT) and branching strategies. We extend a branching technique originally developed for MILP, reliability branching, to the MINLP case. Motivated by the demand for open-source solvers for real-world MINLP problems, we have developed an sBB software package named couenne (Convex Over- and Under-ENvelopes for Non-linear Estimation) and used it for extensive tests on several combinations of BT and branching techniques on a set of publicly available and real-world MINLP instances. We also compare the performance of couenne with a state-of-the-art MINLP solver.

## An Interior-Point Algorithm for Large-Scale Nonlinear Optimization with Inexact Step Computations

2010 · SIAM Journal on Scientific Computing · 被引57 · https://doi.org/10.1137/090747634

We present a line-search algorithm for large-scale continuous optimization. The algorithm is matrix-free in that it does not require the factorization of derivative matrices. Instead, it uses iterative linear system solvers. Inexact step computations are supported in order to save computational expense during each iteration. The algorithm is an interior-point approach derived from an inexact Newton method for equality constrained optimization proposed by Curtis, Nocedal, and Wächter [SIAM J. Optim., 20 (2009), pp. 1224–1249], with additional functionality for handling inequality constraints. The algorithm is shown to be globally convergent under loose assumptions. Numerical results are presented for nonlinear optimization test set collections and a pair of PDE-constrained model problems.

## A Derivative-Free Trust-Region Algorithm for the Optimization of Functions Smoothed via Gaussian Convolution Using Adaptive Multiple Importance Sampling

2018 · SIAM Journal on Optimization · 被引46 · https://doi.org/10.1137/15m1031679

In this paper we consider the optimization of a functional $F$ defined as the convolution of a function $f$ with a Gaussian kernel. We propose this type of objective function for the optimization of the output of complex computational simulations, which often present some form of deterministic noise and need to be smoothed for the results to be meaningful. We introduce a derivative-free algorithm that computes trial points from the minimization of a regression model of the noisy function $f$ over a trust region. The regression model is constructed from function values at sample points that are chosen randomly around iterates and trial points of the algorithm. The weights given to the individual sample points in the regression problem are obtained according to an adaptive multiple importance sampling strategy. This has two advantages. First, it makes it possible to reuse all noisy function values collected over the course of the optimization. Second, the resulting regression model converges to the second-order Taylor approximation of the convolution functional $F$. We prove that, with probability one, each limit point of the iterates is a stationary point of $F$. Computational experiments on a set of benchmark problems with noisy functions compare the proposed algorithm with the deterministic derivative-free trust-region method the proposed method is based on. It is demonstrated that the proposed algorithm performs similarly efficiently in the early stages of the optimization and is able to overcome convergence problems of the original method, where the algorithm might get trapped in spurious local minima induced by the noise.

## Solving Chance-Constrained Problems via a Smooth Sample-Based Nonlinear Approximation

2020 · SIAM Journal on Optimization · 被引78 · https://doi.org/10.1137/19m1261985

We introduce a new method for solving nonlinear continuous optimization problems with chance constraints. Our method is based on a reformulation of the probabilistic constraint as a quantile function. The quantile function is approximated via a differentiable sample average approximation. We provide theoretical statistical guarantees of the approximation and illustrate empirically that the reformulation can be directly used by standard nonlinear optimization solvers in the case of single chance constraints. Furthermore, we propose an S$\ell_1$QP-type trust-region method to solve instances with joint chance constraints. We demonstrate the performance of the method on several problems and show that it scales well with the sample size and that the smoothing can be used to counteract the bias in the chance constraint approximation induced by the sample approximation.

## Towards Autonomous Wood-Log Grasping with a Forestry Crane: Simulator and Benchmarking

2025 · — · 被引2 · https://doi.org/10.1109/icra55743.2025.11127407

Forestry machines operated in forest production environments face challenges when performing manipulation tasks, especially regarding the complicated dynamics of underactuated crane systems and the heavy weight of logs to be grasped. This study investigates the feasibility of using reinforcement learning for forestry crane manipulators in grasping and lifting heavy wood logs autonomously. We first build a simulator using Mujoco physics engine to create realistic scenarios, including modeling a forestry crane with 8 degrees of freedom from CAD data and wood logs of different sizes. We further implement a velocity controller for autonomous log grasping with deep reinforcement learning using a curriculum strategy. Utilizing our new simulator, the proposed control strategy exhibits a success rate of 96% when grasping logs of different diameters and under random initial configurations of the forestry crane. In addition, reward functions and reinforcement learning baselines are implemented to provide an open-source benchmark for the community in large-scale manipulation tasks. A video with several demonstrations can be seen at https://www.acin.tuwien.ac.at/en/d18a/.
