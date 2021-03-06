# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Dunedaqapps(BundlePackage):
    """Bundle all the DUNE DAQ Applications."""

    homepage = "https://github.com/DUNE-DAQ"
    # There is no URL since there is no code to download.

    maintainers = ['philiprodrigues', 'brettviren']

    # First fixed bundle release
    version('0.0.2')

    # The "develop" version maps to "develop" versions for all other
    # packages which themselves tend to be chasing "develop" branches
    version('develop')


    # Add sets of dependencies to specific top-level packages to
    # construct a "matrix" that maps each specific version of this
    # bundle to a vector of specifically versioned packages.  Any
    # packages not listed we leave for Spack to concretize as desired.

    # first "release"
    depends_on('daq-buildtools@1.1.1', when='@0.0.1')
    depends_on('appfwk@1.1.1', when='@0.0.1')
    depends_on('listrev@1.1.0', when='@0.0.1')


    # for now we must take daq-buildtools 1.1.1 to have fixes needed
    # for standard building.  It is expect that develop and post 1.1.1
    # tags will eventually work like 1.1.1.
    depends_on('daq-buildtools@1.1.1', when='@develop')
    depends_on('appfwk@develop', when='@develop')
    depends_on('listrev@master', when='@develop')
    depends_on('py-moo@master', when='@develop')

