# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMoo(PythonPackage):
    """Model oriented objects, tools for code generation."""

    homepage = "https://brettviren.github.io/moo"
    url      = "https://github.com/brettviren/moo/archive/0.0.0.tar.gz"
    git      = "https://github.com/brettviren/moo.git"

    maintainers = ['brettviren']

    version('master', branch='master')
    version('0.0.1', sha256='e1b4b7f70b321737fb512ae40293bb4c5b937462d0e65b7b1ed5428ac5e2892e')

    # from spack:
    depends_on('py-click', type=('build', 'run'))
    depends_on('py-jinja2', type=('build', 'run'))
    depends_on('py-jsonschema', type=('build', 'run'))        
    depends_on('py-jsonpointer', type=('build', 'run'))        

    # from dundaq:
    depends_on('py-jsonnet', type=('build', 'run'))
    depends_on('py-anyconfig', type=('build', 'run'))

