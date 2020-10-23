# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class DaqBuildtools(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/dune-daq/daq-buildtools"
    url      = "https://github.com/dune-daq/daq-buildtools/archive/v1.1.1.tar.gz"
    git      = "https://github.com/dune-daq/daq-buildtools.git"

    maintainers = ['philiprodrigues', 'brettviren']

    version('1.2.1', sha256='cc671faa5a646a5e217b744ea3b5acb11b367d76bd173a82a9a9681bc02cc021')
    version('1.1.1', sha256='d9476e12c4727b0069e37382529d126c01d3d1e1cd2cab474247c16736ea03b4')
    version('develop', branch='develop')

    patch("fix-broken-cetlib.patch")
    
