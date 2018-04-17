#!/bin/bash
#SBATCH -p general
#SBATCH -J Rtestjob
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -t 0-1:00
#SBATCH --mem 50000
#SBATCH -o %j_%N.out
#SBATCH -e %j_%N.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=dsong@hsph.harvard.edu

cd /n/home08/songdongyuan/practice

source new-modules.sh

module load R/3.4.2-fasrc01

R CMD BATCH --vanila --slave CV_simu.R
