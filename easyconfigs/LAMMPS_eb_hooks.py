# Hooks to customize how EasyBuild installs software in EESSI
# see https://docs.easybuild.io/en/latest/Hooks.html
import glob
import os
import re

import easybuild.tools.environment as env
from easybuild.easyblocks.generic.configuremake import obtain_config_guess
from easybuild.framework.easyconfig.constants import EASYCONFIG_CONSTANTS
from easybuild.tools.build_log import EasyBuildError, print_msg
from easybuild.tools.config import build_option, update_build_option
from easybuild.tools.filetools import apply_regex_substitutions, copy_file, remove_file, symlink, which
from easybuild.tools.run import run_cmd
from easybuild.tools.systemtools import AARCH64, POWER, X86_64, get_cpu_architecture, get_cpu_features
from easybuild.tools.toolchain.compiler import OPTARCH_GENERIC

# prefer importing LooseVersion from easybuild.tools, but fall back to distuils in case EasyBuild <= 4.7.0 is used
try:
    from easybuild.tools import LooseVersion
except ImportError:
    from distutils.version import LooseVersion


CPU_TARGET_NEOVERSE_N1 = 'aarch64/neoverse_n1'
CPU_TARGET_NEOVERSE_V1 = 'aarch64/neoverse_v1'
CPU_TARGET_AARCH64_GENERIC = 'aarch64/generic'
CPU_TARGET_A64FX = 'aarch64/a64fx'

CPU_TARGET_ZEN4 = 'x86_64/amd/zen4'

EESSI_RPATH_OVERRIDE_ATTR = 'orig_rpath_override_dirs'

SYSTEM = EASYCONFIG_CONSTANTS['SYSTEM'][0]

EESSI_INSTALLATION_REGEX = r"^/cvmfs/[^/]*.eessi.io/versions/"
HOST_INJECTIONS_LOCATION = "/cvmfs/software.eessi.io/host_injections/"

def pre_configure_hook(self, *args, **kwargs):
    """
    pre-configure hook for LAMMPS:
    - set kokkos_arch on x86_64/amd/zen4
    """

    print_msg("Using custom hook for %s %s", self.name, self.version)
    cpu_target = get_eessi_envvar('EESSI_SOFTWARE_SUBDIR')
    if self.name == 'LAMMPS':
        if self.version in ('2Aug2023_update4'):
            if get_cpu_architecture() == X86_64:
                if cpu_target == CPU_TARGET_ZEN4:
                    # There is no support for ZEN4 in LAMMPS yet so falling back to ZEN3
                    self.cfg['kokkos_arch'] = 'ZEN3'
    else:
        raise EasyBuildError("LAMMPS-specific hook triggered for non-LAMMPS easyconfig?!")

