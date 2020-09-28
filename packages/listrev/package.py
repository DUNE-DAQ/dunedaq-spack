# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

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
