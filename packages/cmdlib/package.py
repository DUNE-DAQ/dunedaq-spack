# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Cmdlib(CMakePackage):
    """Interfaces for DUNE DAQ command objects."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/dune-daq/cmdlib"
    url      = "https://github.com/dune-daq/cmdlib/archive/v0.0.0.tar.gz"
    git      = "https://github.com/dune-daq/cmdlib.git"

    maintainers = ['brettviren']

    version('master', branch='master')

    depends_on('daq-buildtools')
    depends_on('nlohmann-json')
    depends_on('cetlib')
    depends_on('ers')

    # note: https://github.com/DUNE-DAQ/cmdlib/issues/2
    depends_on('intel-tbb')
    patch("add-tbb.patch")

