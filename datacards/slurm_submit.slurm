#!/bin/bash

#SBATCH --mail-type=ALL
#SBATCH --mail-user=reixesreis@gmail.com

#SBATCH --qos=cu_htc
#SBATCH --partition=cpu
#SBATCH --job-name=Limits
#SBATCH --output=sbatch.log
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=50
#SBATCH --mem=100G

# Source the CMS environment
source /work/app/cms/cmsset_default.sh
function cmsset() {
  cd ~/binary/CMSSW_14_1_0_pre5/src && source /work/app/share_env/hepsw.sh && cmsenv && cd -
}
cmsset

python3 -u run_limits.py --threads 50
