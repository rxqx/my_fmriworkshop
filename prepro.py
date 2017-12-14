#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:15 2017

@author: rx
"""
import glob
import os
#import shutil
import pdb


#Set the path to the data
def prepro(basedir):
    for item in glob.glob(os.path.join(basedir,'sub-*','func','sub-*_task-bart_bold.nii.gz')):
        input=item
        output_path=item.split('.')[0]
        output=output_path+('_brain')
        os.system("/usr/local/fsl/bin/bet %s %s -F"%(input, output))
        #pdb.set_trace()
def main():
    basedir='/Users/rx/Documents/Research/my_fmriworkshop/fmri_workshop/data'
    prepro(basedir)
main()

#Use wildcards to pull all the subjects' data from a BIDS-formatted project 
input=glob.glob('/Users/rx/Documents/Research/my_fmriworkshop/fmri_workshop/data/sub-*/func/sub-*_task-bart_bold*.nii.gz')
print(input)
#Check that it is pulling the data from the correct number of subjects
len(input)
#Use the split function to parse the data by the '/' character, then reference 
#the newly created list in the appropriate cell to generate the subj number.
sub=input[0].split('/')[8]
print(sub)

subtask=input[1].split('/')[10].split('.')[0]
print(subtask)
output=subtask+'_brain'
print(output)


os.system('bet %s $s -F'%(sub, output))

# Can use the os.path.join function to use the above code to produce single
# participants' variables, instead to bulk spit them out for all of the data.
basedir='/Users/rx/Documents/Research/my_fmriworkshop/fmri_workshop/data'
path=os.path.join(basedir,'sub-*','func','sub-*.nii.gz')
print(path)
input=glob.glob(path)
len(input[1:5])
print(input[0:2])