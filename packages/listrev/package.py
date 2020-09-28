# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install listrev
#
# You can edit this file again by typing:
#
#     spack edit listrev
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Listrev(CMakePackage):
    """A DUNE DAQ appfwk demo package."""

    homepage = "https://github.com/dune-daq/listrev"
    url      = "https://github.com/DUNE-DAQ/listrev/archive/v1.1.0.tar.gz"
    git      = "https://github.com/DUNE-DAQ/listrev.git"

    maintainers = ['philiprodrigues', 'brettviren']

    version('master', branch='master')
    version('1.1.0', sha256='7aafd55b2f076ed1aa2ea301f0d40db14ca7cb3de4f2ba1a5ee9b826ea9dbcad')
    version('1.0.0', sha256='f0cbdb680a09fef8ba382c6c60c9bb8d85359132366c69fdeeef19b75dbf733c')

    depends_on('appfwk')

    patch("fix-find-dqt.patch")
