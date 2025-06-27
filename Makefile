# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= --doctree-dir localTemp/doctrees 
				 
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = sphinxSource
# BUILDDIR      = docBuild
# BUILDDIR      = LCPFDocs/Dev/Api
BUILDDIR      = ../wwwlumensalis/src/content/Projects/LCPF/LCPFDocs/Dev/Api
# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
