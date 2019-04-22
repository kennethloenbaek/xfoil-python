# -*- coding: utf-8 -*-
#   Copyright (c) 2019 D. de Vries
#
#   This file is part of XFoil.
#
#   XFoil is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   XFoil is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with XFoil.  If not, see <https://www.gnu.org/licenses/>.
import os
from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration

version = '0.0.17'


# Adding source extension
config = Configuration('xfoil')
sources = [
    "i_pindex.f90",
    "i_xfoil.f90",
    "i_blpar.f90",
    "i_circle.f90",
    "i_xbl.f90",
    # Main modules
    "m_userio.f90",
    "m_aread.f90",
    "m_iopol.f90",
    "m_naca.f90",
    "m_sort.f90",
    "m_spline.f90",
    "m_xsolve.f90",
    "m_xutils.f90",
    "s_xbl.f90",
    "m_xpanel.f90",
    "m_xblsys.f90",
    "s_xfoil.f90",
    "m_xbl.f90",
    "m_xgeom.f90",
    "m_xgdes.f90",
    "s_xoper.f90",
    "m_xpol.f90",
    "m_xoper.f90",
    "m_xqdes.f90",
    "m_xmdes.f90",
    "m_xfoil.f90",
    # API
    "api.f90",
]
# Setting source path location
sources = [os.path.join("src",source) for source in sources]
# Compiler flags
extra_compile_args = [
    "-O",
    "-fbounds-check",
    "-finit-real=inf",
    "-ffpe-trap=invalid,zero",
    "-fdefault-real-8"
]
# Adding sorces to config and giving name
config.add_extension('libxfoil', sources= sources, extra_compile_args=extra_compile_args)

def readme():
    with open('README.md') as f:
        return f.read()

kwds = dict(
    name='xfoil',
    version=version,
    description='Stripped down version of XFOIL as compiled python module ',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Fortran',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
    ],
    keywords='xfoil airfoil aerodynamic analysis',
    url='https://github.com/daniel-de-vries/xfoil-python',
    download_url='https://github.com/daniel-de-vries/xfoil-python/tarball/' + version,
    author='Daniël de Vries',
    author_email='contact@daniel-de-vries.com',
    license='GNU General Public License v3 or later (GPLv3+)',
    packages=['xfoil'],
    install_requires=['numpy'],
    zip_save=False,
)

kwds.update(config.todict())

setup(**kwds)