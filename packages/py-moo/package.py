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
#     spack install py-moo
#
# You can edit this file again by typing:
#
#     spack edit py-moo
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyMoo(PythonPackage):
    """Model oriented objects, tools for code generation."""

    homepage = "https://brettviren.github.io/moo"
    url      = "https://github.com/brettviren/moo/archive/v0.0.0.tar.gz"
    git      = "https://github.com/brettviren/moo.git"

    maintainers = ['brettviren']

    version('master', branch='master')
    # version('1.2.4')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    # depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))

    # from spack:
    depends_on('py-click', type=('build', 'run'))
    depends_on('py-jinja2', type=('build', 'run'))
    depends_on('py-jsonschema', type=('build', 'run'))        
    depends_on('py-jsonpointer', type=('build', 'run'))        

    # from dundaq:
    depends_on('py-jsonnet', type=('build', 'run'))
    depends_on('py-anyconfig', type=('build', 'run'))

