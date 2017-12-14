#!/usr/bin/python

# This script will generate each subjects design.fsf, but does not run it.
# It depends on your system how will launch feat

import os
import glob

# Set this to the directory all of the sub### directories live in
studydir = '/Users/rx/Documents/Research/my_fmriworkshop/fmri_workshop/FSL_tutorial_data'

# Set this to the directory where you'll dump all the fsf files
# May want to make it a separate directory, because you can delete them all o
#   once Feat runs
fsfdir="%s/fsfs"%(studydir)

# Get all the paths!  Note, this won't do anything special to omit bad subjects
subdirs=glob.glob("%s/sub[0-9][0-9][0-9]"%(studydir))

for dir in subdirs:
  subnum=dir[-3:]
  print(subnum)
  #os.popen runs fslnvols and reports back how many volumes there are 
  #ntime = os.popen('fslnvols %s/bold.nii.gz'%(dir)).read().rstrip()
  replacements = {'SUBNUM':subnum}
  with open("%s/template.fsf"%(fsfdir)) as infile: 
    with open("%s/design_sub%s.fsf"%(fsfdir, subnum), 'w') as outfile:
        for line in infile:
          # Note, since the video, I've changed "iteritems" to "items"
          # to make the following work on more versions of python
          #  (python 3 no longer has iteritems())  
          for src, target in replacements.items():
            line = line.replace(src, target)
          outfile.write(line)
  
