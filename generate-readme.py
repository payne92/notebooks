#!/usr/bin/env python
#
#  Generate the README.md from the *.ipynb file contents of this 
#  directory
#
#  <andy@payne.org>
#  June, 2014

import glob, os, re

viewer = 'http://nbviewer.ipython.org/'
this_repo = 'github/payne92/notebooks/blob/master/'
print """
# Notebooks

This is my collection of IPython Web notebooks on various topics:
"""

for nbpath in sorted(glob.glob("*.ipynb")):
	url = viewer + this_repo + nbpath
	(name, ext) = os.path.splitext(nbpath)
	if re.match("^[0-9]+", name):
		name = re.sub("^[0-9]+ ", "", name)		# Strip leading digits
		print "* [%s](%s)" % (name, url)

print """
<andy@payne.org>
"""
