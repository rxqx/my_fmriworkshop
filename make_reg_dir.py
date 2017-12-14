#!/usr/bin/python


import os
import glob

# This is the path to the directory that contains all the subject directories
basedir = '/Users/rx/Documents/Research/my_fmriworkshop/fmri_workshop/data/derivatives/task'

# Grab all the paths to the bart.feat directories

barts = glob.glob("%s/sub*/bart.feat"%(basedir))

# Now we'll march through each bart.feat and create a reg directory and the files it needs based on my tutorial here: http://mumfordbrainstats.tumblr.com/post/166054797696/feat-registration-workaround

for dir in barts:
    os.system("mkdir %s/reg"%(dir))
    os.system("cp $FSLDIR/etc/flirtsch/ident.mat %s/reg/example_func2standard.mat"%(dir))
    os.system("cp %s/mean_func.nii.gz %s/reg/standard.nii.gz"%(dir, dir))
    
