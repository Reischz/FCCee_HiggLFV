{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "171be54b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/work/project/escience/ruttho/FCCee_HiggLFV\n"
     ]
    }
   ],
   "source": [
    "%cd /work/project/escience/ruttho/FCCee_HiggLFV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1cb77d13",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total 2319\n",
      "-rwxrwxr-x 1 ruttho   8499 Mar 24 11:19 \u001b[0m\u001b[38;5;34manalyze_eeZH.cpp\u001b[0m*\n",
      "-rw-rw-r-- 1 ruttho   6053 Mar 24 11:19 analyze_pipeline.cpp\n",
      "-rw-r--r-- 1 ruttho      0 Mar 27 11:25 combine_upperlimit.ipynb\n",
      "-rw-r--r-- 1 ruttho   6709 Mar 27 10:42 compare_ETauMuSelection.py\n",
      "-rw-r--r-- 1 ruttho   7155 Mar 27 10:42 compare_MuESelection.py\n",
      "-rw-r--r-- 1 ruttho   5496 Mar 27 11:16 Create_fourSelection.py\n",
      "drwxrwxr-x 2 ruttho   4096 Mar 24 11:19 \u001b[38;5;27mdatacards\u001b[0m/\n",
      "-rwxrwxr-x 1 ruttho   1443 Mar 24 11:19 \u001b[38;5;34mDelphes.C\u001b[0m*\n",
      "-rwxrwxr-x 1 ruttho 246416 Mar 24 11:19 \u001b[38;5;34mDelphes.h\u001b[0m*\n",
      "drwxrwxr-x 4 ruttho   4096 Mar 27 09:24 \u001b[38;5;27mETauMu_Selection\u001b[0m/\n",
      "-rw-r--r-- 1 ruttho 348547 Mar 27 08:19 HLFV_125GeV_81To101Hist.root\n",
      "-rw-rw-r-- 1 ruttho      0 Mar 27 06:20 Hmass125_log.txt\n",
      "drwxrwxr-x 2 ruttho   4096 Mar 27 09:07 \u001b[38;5;27minclude\u001b[0m/\n",
      "-rw-rw-r-- 1 ruttho  21451 Mar 24 11:19 makecard.py\n",
      "drwxrwxr-x 2 ruttho   4096 Mar 27 08:45 \u001b[38;5;27mMasstoPT_Selection\u001b[0m/\n",
      "-rw-rw-r-- 1 ruttho   8579 Mar 24 11:19 merge_twoProdMode.py\n",
      "-rw-r--r-- 1 ruttho   5544 Mar 25 13:19 MuE_run.py\n",
      "-rw-r--r-- 1 ruttho   2721 Mar 27 07:26 MuE_run.sh\n",
      "drwxrwxr-x 4 ruttho   4096 Mar 27 09:24 \u001b[38;5;27mMuE_Selection\u001b[0m/\n",
      "-rw-rw-r-- 1 ruttho  17285 Mar 24 11:19 numpy_hist.py\n",
      "-rw-rw-r-- 1 ruttho  36243 Mar 24 11:19 optimize_results.py\n",
      "-rw-rw-r-- 1 ruttho    796 Mar 24 11:19 pipeline_etaumu_21To81.json\n",
      "-rw-rw-r-- 1 ruttho    805 Mar 27 09:07 pipeline_etaumu_21To81_PTthenMass.json\n",
      "-rw-rw-r-- 1 ruttho    797 Mar 24 11:19 pipeline_etaumu_81To101.json\n",
      "-rw-rw-r-- 1 ruttho    806 Mar 27 09:07 pipeline_etaumu_81To101_PTthenMass.json\n",
      "-rw-rw-r-- 1 ruttho    879 Mar 24 11:19 pipeline_etaumu.json\n",
      "-rw-rw-r-- 1 ruttho    980 Mar 24 11:19 pipeline_etaumu_Zoffshell.json\n",
      "-rw-rw-r-- 1 ruttho    663 Mar 24 18:22 pipeline_mue_21To81.json\n",
      "-rw-rw-r-- 1 ruttho    666 Mar 27 06:15 pipeline_mue_21To81_PTthenMass.json\n",
      "-rw-rw-r-- 1 ruttho    660 Mar 24 18:47 pipeline_mue_81To101.json\n",
      "-rw-rw-r-- 1 ruttho    663 Mar 27 08:17 pipeline_mue_81To101_PTthenMass.json\n",
      "-rw-rw-r-- 1 ruttho    794 Mar 24 11:19 pipeline_mutaue_21To81.json\n",
      "-rw-rw-r-- 1 ruttho    795 Mar 24 11:19 pipeline_mutaue_81To101.json\n",
      "-rw-rw-r-- 1 ruttho    883 Mar 24 11:19 pipeline_mutaue.json\n",
      "-rw-rw-r-- 1 ruttho   1056 Mar 24 11:19 pipeline_mutaue_Zoffshell.json\n",
      "-rw-r--r-- 1 ruttho  10643 Mar 27 10:44 PlotTotalEvents.ipynb\n",
      "-rw-r--r-- 1 ruttho 896292 Mar 25 18:04 PlotYield.ipynb\n",
      "drwxrwxr-x 2 ruttho   4096 Mar 25 12:06 \u001b[38;5;27mprefit_histograms\u001b[0m/\n",
      "drwxrwxr-x 2 ruttho   4096 Mar 27 08:45 \u001b[38;5;27mPTtoMass_Selection\u001b[0m/\n",
      "drwxrwxr-x 2 ruttho   4096 Mar 25 11:51 \u001b[38;5;27m__pycache__\u001b[0m/\n",
      "-rw-rw-r-- 1 ruttho   2325 Mar 24 11:19 README.md\n",
      "-rw-r--r-- 1 ruttho  70388 Mar 25 16:02 ReadROOT.ipynb\n",
      "-rw-rw-r-- 1 ruttho  17755 Mar 24 11:19 runall.py\n",
      "-rw-rw-r-- 1 ruttho  20391 Mar 24 17:54 runall_twoRegion.py\n",
      "-rw-rw-r-- 1 ruttho  19882 Mar 24 11:19 runall_twoRegion_VBF.py\n",
      "-rw-rw-r-- 1 ruttho    134 Mar 27 10:41 sbatch.log\n",
      "drwxrwxr-x 2 ruttho  16384 Mar 25 14:05 \u001b[38;5;27mSelection_Results\u001b[0m/\n",
      "drwxrwxr-x 2 ruttho   4096 Mar 27 09:07 \u001b[38;5;27msrc\u001b[0m/\n",
      "-rw-r--r-- 1 ruttho 336173 Mar 24 18:40 test.root\n",
      "drwxrwxr-x 5 ruttho   4096 Mar 27 11:24 \u001b[38;5;27mUpper_Limits\u001b[0m/\n",
      "-rw-rw-r-- 1 ruttho  36288 Mar 24 11:19 utils.py\n",
      "-rw-rw-r-- 1 ruttho   3292 Mar 24 11:19 xsec_pb.json\n"
     ]
    }
   ],
   "source": [
    "%ll"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "903b488b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a5a35c05",
   "metadata": {},
   "outputs": [],
   "source": [
    "os.copy"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
