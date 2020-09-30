# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class CcmCtrl(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/roland-sipos/ccm-ctrl"
    url      = "https://github.com/roland-sipos/ccm-ctrl/archive/v0.0.0.tar.gz"
    git      = "https://github.com/roland-sipos/ccm-ctrl.git"

    maintainers = ['brettviren']

    version('master', branch='master')

    # normally, don't depend on a speciffic version but for now this
    # package requires this branch.
    depends_on('appfwk@bv-config-proto')

    depends_on('pistache')

    patch("fix-cmakelists.patch")
