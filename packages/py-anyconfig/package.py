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
#     spack install py-anyconfig
#
# You can edit this file again by typing:
#
#     spack edit py-anyconfig
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyAnyconfig(PythonPackage):
    """Common APIs to load and dump configuration files in various formats."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/ssato/python-anyconfig"
    url      = "https://pypi.io/packages/source/a/anyconfig/anyconfig-0.9.11.tar.gz"

    maintainers = ['brettviren']

    version('0.9.11', sha256='8888130cde5461cb39379afdd1d09b1b1342356210f0a6743a4b60f9973226f8')

    depends_on('py-setuptools', type='build')
