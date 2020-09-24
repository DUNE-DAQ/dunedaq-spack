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
#     spack install daq-buildtools
#
# You can edit this file again by typing:
#
#     spack edit daq-buildtools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *

class DaqBuildtools(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/dune-daq/daq-buildtools"
    url      = "https://github.com/dune-daq/daq-buildtools/archive/v1.1.1.tar.gz"
    git      = "https://github.com/dune-daq/daq-buildtools.git"

    maintainers = ['philiprodrigues', 'brettviren']

    version('1.1.1', sha256='d9476e12c4727b0069e37382529d126c01d3d1e1cd2cab474247c16736ea03b4')
    version('develop', branch='develop')
