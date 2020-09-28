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
#     spack install appfwk
#
# You can edit this file again by typing:
#
#     spack edit appfwk
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Appfwk(CMakePackage):
    """DUNE DAQ application framework."""

    homepage = "https://github.com/DUNE-DAQ/appfwk"
    url      = "https://github.com/DUNE-DAQ/appfwk/archive/v1.1.0.tar.gz"
    git      = "https://github.com/DUNE-DAQ/appfwk.git"

    version('spack-build', branch='spack-build')
    version('develop', branch='develop')
    version('1.1.1', sha256='0359717ed285d9ac1e2bcfdb5da23e02f3315c5be38ee49080265832558e8ede')
    version('1.1.0', sha256='3a88d45b5251748d0041fb7ad3df07c086d5acf3c27b1ca213887c3ad15bee98')
    version('1.0.0', sha256='2d61dd2d9b685351f840cf085606935960ab2e437ff10be14be1d67adeea0255')

    # probably needed earlier than 1.1.0
    patch("fix-find-dqt.patch", when="@1.1.0")
    patch("fix-find-dqt.patch", when="@develop")

    # FIXME: Add dependencies if required.
    depends_on('daq-buildtools')
    depends_on('boost')
    depends_on('folly')
    depends_on('trace@stable')
    depends_on('cetlib')
    depends_on('ers')
    depends_on('nlohmann-json')
