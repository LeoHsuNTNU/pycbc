#!/usr/bin/python
# Copyright (C) 2011 Karsten Wiesner
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


#
# =============================================================================
#
#                                   Preamble
#
# =============================================================================
#

"""
setup.py file for PyCBC package
"""

import os
from distutils.core import setup
from distutils.core import Extension
from distutils.command.clean import clean as _clean

ver = '0.1'
pycbc_extensions = []
pycbc_clean_files = []

# extension modules for the top-level package
pycbc_extensions.append(Extension( 'pycbc.clayer._cpu', 
    sources = ['pycbc/clayer/cpu/pycbccpu.i',
               'pycbc/clayer/cpu/pycbccpu.c'],
    depends = ['pycbc/clayer/cpu/pycbccpu_types.h',
               'pycbc/clayer/cpu/pycbccpu_prototypes.h'],
    swig_opts = ['-outdir','pycbc/clayer'],
    extra_compile_args = ['-Wall','-fPIC']
    ))

pycbc_clean_files.append('pycbc/clayer/cpu.py')
pycbc_clean_files.append('pycbc/clayer/cpu/pycbccpu_wrap.c')


pycbc_extensions.append(Extension( 'pycbc.datavector.clayer._cpu', 
    sources = ['pycbc/datavector/clayer/cpu/datavectorcpu.i',
               'pycbc/datavector/clayer/cpu/datavectorcpu.c'],
    depends = ['pycbc/datavector/clayer/cpu/datavectorcpu.h',
               'pycbc/datavector/clayer/cpu/datavectorcpu_private.h'],
    swig_opts = ['-outdir','pycbc/datavector/clayer'],
    extra_compile_args = ['-Wall','-fPIC']
    ))

pycbc_clean_files.append('pycbc/datavector/clayer/cpu.py')
pycbc_clean_files.append('pycbc/datavector/clayer/cpu/datavectorcpu_wrap.c')


pycbc_extensions.append(Extension( 'pycbc.straindata.clayer._cpu', 
    sources = ['pycbc/straindata/clayer/cpu/straindatacpu.i',
               'pycbc/straindata/clayer/cpu/straindatacpu.c'],
    depends = ['pycbc/straindata/clayer/cpu/straindatacpu_types.h',
               'pycbc/straindata/clayer/cpu/straindatacpu_prototypes.h'],
    include_dirs = ['pycbc/datavector/clayer/cpu'],
    swig_opts = ['-outdir','pycbc/straindata/clayer'],
    extra_compile_args = ['-Wall','-fPIC']
    ))

pycbc_clean_files.append('pycbc/straindata/clayer/cpu.py')
pycbc_clean_files.append('pycbc/straindata/clayer/cpu/straindatacpu_wrap.c')


pycbc_extensions.append(Extension( 'pycbc.templatebank.clayer._cpu', 
    sources = ['pycbc/templatebank/clayer/cpu/templatebankcpu.i',
               'pycbc/templatebank/clayer/cpu/templatebankcpu.c'],
    depends = ['pycbc/templatebank/clayer/cpu/templatebankcpu_prototypes.h'],
    include_dirs = ['pycbc/clayer/cpu',
               'pycbc/datavector/clayer/cpu'],
    swig_opts = ['-outdir','pycbc/templatebank/clayer'],
    extra_compile_args = ['-Wall','-fPIC']
    ))

pycbc_clean_files.append('pycbc/templatebank/clayer/cpu.py')
pycbc_clean_files.append('pycbc/templatebank/clayer/cpu/templatebankcpu_wrap.c')


pycbc_extensions.append(Extension( 'pycbc.matchedfilter.clayer._cpu', 
    sources = ['pycbc/matchedfilter/clayer/cpu/matchedfiltercpu.i',
               'pycbc/matchedfilter/clayer/cpu/matchedfiltercpu.c'],
    depends = ['pycbc/matchedfilter/clayer/cpu/matchedfiltercpu_types.h',
               'pycbc/matchedfilter/clayer/cpu/matchedfiltercpu_prototypes.h'],
    include_dirs = ['pycbc/clayer/cpu',
               'pycbc/datavector/clayer/cpu'],
    swig_opts = ['-outdir','pycbc/matchedfilter/clayer'],
    extra_compile_args = ['-Wall','-fPIC']
    ))

pycbc_clean_files.append('pycbc/matchedfilter/clayer/cpu.py')
pycbc_clean_files.append('pycbc/matchedfilter/clayer/cpu/matchedfiltercpu_wrap.c')


# class to clean up the files automatically generated by swig
class clean(_clean):
    def finalize_options (self):
        _clean.finalize_options(self)
        self.clean_files = pycbc_clean_files

    def run(self):
        _clean.run(self)
        for f in self.clean_files:
            try:
                os.unlink(f)
                print 'removed {0}'.format(f)
            except:
                pass


# do the actual work of building the package
setup (
    name = 'pycbc',
    version = ver,
    description = 'Gravitational wave CBC analysis toolkit',
    author = 'Ligo Virgo Collaboration - pyCBC team',
    author_email = 'https://sugwg-git.phy.syr.edu/dokuwiki/doku.php?id=pycbc:home',
    cmdclass = { 'clean' : clean },
    ext_modules = pycbc_extensions,
    packages = ['pycbc','pycbc.clayer',
                'pycbc.datavector','pycbc.datavector.clayer',
                'pycbc.bandpass',
                'pycbc.chisqveto',
                'pycbc.injection',
                'pycbc.overwhiteningfilter',
                'pycbc.resample',
                'pycbc.singledetectorevent',
                'pycbc.straindata','pycbc.straindata.clayer',
                'pycbc.templatebank','pycbc.templatebank.clayer',
                'pycbc.matchedfilter','pycbc.matchedfilter.clayer',
                'pycbc.waveform'],
    scripts = ['bin/pycbc_min_pipeline',
               'bin/pycbc_cpu_syr_pipeline']

)
