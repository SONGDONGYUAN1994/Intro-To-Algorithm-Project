# Intro-To-Algorithm-Project
BST234 Intro To Algorithm Final Project  
This project requires using permutation test to calculate SKAT p-value.  
The detailed method of SKAT is in Wu et al's paper.  
Basically, here we calculate <img src="http://latex.codecogs.com/svg.latex?Q%3D+%7B%28Y-%5Chat%7B%5Cmu%7D%29%7D%5ETXX%5ET%28Y-%5Chat%7B%5Cmu%7D%29" /> as the statistics.  
Permutation times are 1000 as the burden test.  
The $Y$ is the binary variable case/control (as 1/0). In data, first 10000th are cases and last 10000th are controls.  
$X$ is a $20000 \times 50$ matrix, which has 50 loci as features.  
Notice the $X$ is very sparse and also binary. So the core of this project is to design fast, stable algorthim for sparse matrix manipulation.  
