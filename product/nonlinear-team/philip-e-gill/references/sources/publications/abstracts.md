# Philip E. Gill · 代表作候选摘要

> 来自OpenAlex，仅供筛选精读对象。引用前请回到原文核对。

## SNOPT: An SQP Algorithm for Large-Scale Constrained Optimization

2005 · SIAM Review · 被引2886 · https://doi.org/10.1137/s0036144504446096

Sequential quadratic programming (SQP) methods have proved highly effective for solving constrained optimization problems with smooth nonlinear functions in the objective and constraints. Here we consider problems with general inequality constraints (linear and nonlinear). We assume that first derivatives are available and that the constraint gradients are sparse. Second derivatives are assumed to be unavailable or too expensive to calculate. We discuss an SQP algorithm that uses a smooth augmented Lagrangian merit function and makes explicit provision for infeasibility in the original problem and the QP subproblems. The Hessian of the Lagrangian is approximated using a limited-memory quasi-Newton method. SNOPT is a particular implementation that uses a reduced-Hessian semidefinite QP solver (SQOPT) for the QP subproblems. It is designed for problems with many thousands of constraints and variables but is best suited for problems with a moderate number of degrees of freedom (say, up to 2000). Numerical results are given for most of the CUTEr and COPS test collections (about 1020 examples of all sizes up to 40000 constraints and variables, and up to 20000 degrees of freedom).

## SNOPT: An SQP Algorithm for Large-Scale Constrained Optimization

2002 · SIAM Journal on Optimization · 被引1605 · https://doi.org/10.1137/s1052623499350013

Sequential quadratic programming (SQP) methods have proved highly effective for solving constrained optimization problems with smooth nonlinear functions in the objective and constraints. Here we consider problems with general inequality constraints (linear and nonlinear). We assume that first derivatives are available and that the constraint gradients are sparse. We discuss an SQP algorithm that uses a smooth augmented Lagrangian merit function and makes explicit provision for infeasibility in the original problem and the QP subproblems. SNOPT is a particular implementation that makes use of a semidefinite QP solver. It is based on a limited-memory quasi-Newton approximation to the Hessian of the Lagrangian and uses a reduced-Hessian algorithm (SQOPT) for solving the QP subproblems. It is designed for problems with many thousands of constraints and variables but a moderate number of degrees of freedom (say, up to 2000). An important application is to trajectory optimization in the aerospace industry. Numerical results are given for most problems in the CUTE and COPS test collections (about 900 examples).

## Quasi-Newton Methods for Unconstrained Optimization

1972 · IMA Journal of Applied Mathematics · 被引363 · https://doi.org/10.1093/imamat/9.1.91

A revised algorithm is given for unconstrained optimization using quasi-Newton methods. The method is based on recurring the factorization of an approximation to the Hessian matrix. Knowledge of this factorization allows greater flexibility when choosing the direction of search while minimizing the adverse effects of rounding error. The control of rounding error is particularly important when analytical derivatives are unavailable, and a modification of the algorithm to accept finite-difference approximations to the derivatives is given.

## Dictionary of civil defense

1953 · Journal of Chemical Education · 被引0 · https://doi.org/10.1021/ed030p163.3

ADVERTISEMENT RETURN TO ISSUEPREVBook and Media Revie...Book and Media ReviewNEXTDictionary of civil defensePhilip Gill Cite this: J. Chem. Educ. 1953, 30, 3, 163Publication Date (Print):March 1, 1953Publication History Received3 August 2009Published online1 March 1953Published inissue 1 March 1953https://doi.org/10.1021/ed030p163.3RIGHTS & PERMISSIONSArticle Views92Altmetric-Citations-LEARN ABOUT THESE METRICSArticle Views are the COUNTER-compliant sum of full text article downloads since November 2008 (both PDF and HTML) across all institutions and individuals. These metrics are regularly updated to reflect usage leading up to the last few days.Citations are the number of other articles citing this article, calculated by Crossref and updated daily. Find more information about Crossref citation counts.The Altmetric Attention Score is a quantitative measure of the attention that a research article has received online. Clicking on the donut icon will load a page at altmetric.com with additional details about the score and the social media presence for the given article. Find more information on the Altmetric Attention Score and how the score is calculated. Share Add toView InAdd Full Text with ReferenceAdd Description ExportRISCitationCitation and abstractCitation and referencesMore Options Share onFacebookTwitterWechatLinked InReddit PDF (947 KB) Get e-Alerts Get e-Alerts

## Methods for modifying matrix factorizations

1974 · Mathematics of Computation · 被引586 · https://doi.org/10.1090/s0025-5718-1974-0343558-6

In recent years, several algorithms have appeared for modifying the factors of a matrix following a rank-one change. These methods have always been given in the context of specific applications and this has probably inhibited their use over a wider field. In this report, several methods are described for modifying Cholesky factors. Some of these have been published previously while others appear for the first time. In addition, a new algorithm is presented for modifying the complete orthogonal factorization of a general matrix, from which the conventional QR factors are obtained as a special case. A uniform notation has been used and emphasis has been placed on illustrating the similarity between different methods.

## Algorithms for the Solution of the Nonlinear Least-Squares Problem

1978 · SIAM Journal on Numerical Analysis · 被引556 · https://doi.org/10.1137/0715063

This paper describes a modification to the Gauss–Newton method for the solution of nonlinear least-squares problems. The new method seeks to avoid the deficiencies in the Gauss–Newton method by improving, when necessary, the Hessian approximation by specifically including or approximating some of the neglected terms. The method seeks to compute the search direction without the need to form explicitly either the Hessian approximation or a factorization of this matrix. The benefits of this are similar to that of avoiding the formation of the normal equations in the Gauss-Newton method. Three algorithms based on this method are described; one which assumes that second derivative information is available and two which only assume first derivatives can be computed.

## Aquifer Reclamation Design: The Use of Contaminant Transport Simulation Combined With Nonlinear Programing

1984 · Water Resources Research · 被引271 · https://doi.org/10.1029/wr020i004p00415

A simulation‐management methodology is demonstrated for the rehabilitation of aquifers that have been subjected to chemical contamination. Finite element groundwater flow and contaminant transport simulation are combined with nonlinear optimization. The model is capable of determining well locations plus pumping and injection rates for groundwater quality control. Examples demonstrate linear or nonlinear objective functions subject to linear and nonlinear simulation and water management constraints. Restrictions can be placed on hydraulic heads, stresses, and gradients, in addition to contaminant concentrations and fluxes. These restrictions can be distributed over space and time. Three design strategies are demonstrated for an aquifer that is polluted by a constant contaminant source: they are pumping for contaminant removal, water injection for in‐ground dilution, and a pumping, treatment, and injection cycle. A transient model designs either contaminant plume interception or in‐ground dilution so that water quality standards are met. The method is not limited to these cases. It is generally applicable to the optimization of many types of distributed parameter systems.

## User's Guide for NPSOL (Version 4.0): A Fortran Package for Nonlinear Programming.

1986 · — · 被引525 · https://doi.org/10.21236/ada169115

Abstract : This report forms the user's guide for Version 4.0 of NPSOL, a set of Fortran subroutines designed to minimize a smooth function subject to constraints, which may include simple bounds on the variables, linear constraints and smooth nonlinear constraints. (NPSOL may also be used for unconstrained, bound-constrained and linearly constrained optimization.) The user must provide subroutines that define the objective and constraint functions and (optionally) their gradients. All matrices are treated as dense, and hence NPSOL is not intended for large sparse problems. NPSOL uses a sequential quadratic programming (SQP) algorithm, in which the search directions is the solution of a quadratic programming (QP) subproblem. The algorithm treats bounds, linear constraints and nonlinear constraints separately. The Hessian of each QP subproblem is a positive-definite quasi-Newton approximation to the Hessian of the Lagrangian function. The steplength at each iteration is required to produce a sufficient decrease an augmented Lagrangian merit function. Each QP subproblem is solved using a quadratic programming package with several features that improve the efficiency of an SQP algorithm. (Author)

## Preconditioners for Indefinite Systems Arising in Optimization

1992 · SIAM Journal on Matrix Analysis and Applications · 被引147 · https://doi.org/10.1137/0613022

Methods are discussed for the solution of sparse linear equations $Ky = z$, where K is symmetric and indefinite. Since exact solutions are not always required, direct and iterative methods are both of interest. An important direct method is the Bunch–Parlett factorization $K = U^T DU$, where U is triangular and D is block-diagonal. A sparse implementation exists in the form of the Harwell code MA27. An appropriate iterative method is the conjugate-gradient–like algorithm SYMMLQ, which solves indefinite systems with the aid of a positive-definite preconditioner. For any indefinite matrix K, it is shown that the $U^T DU$ factorization can be modified at nominal cost to provide an “exact” preconditioner for SYMMLQ. Code is given for overwriting the block-diagonal matrix D produced by MA27. The KKT systems arising in barrier methods for linear and nonlinear programming are studied, and preconditioners for use with SYMMLQ are derived. For nonlinear programs a preconditioner is derived from the “smaller” KKT system associated with variables that are not near a bound. For linear programs several preconditioners are proposed, based on a square nonsingular matrix B that is analogous to the basis matrix in the simplex method. The aim is to facilitate solution of full KKT systems rather than equations of the form $AD^2 A^T \Delta \pi = r$ when the latter become excessively ill conditioned.
