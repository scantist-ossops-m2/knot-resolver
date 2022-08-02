#!/usr/bin/python3

import importlib
import importlib.util
import sys
from types import ModuleType

import pkg_resources

# replace imports with mocks
dummy = ModuleType("dummy")
dummy.__dict__["setup"] = lambda *args, **kwargs: None
dummy.__dict__["build"] = lambda *args, **kwargs: None
sys.modules["setuptools"] = dummy
sys.modules["build"] = dummy

# load install_requires array from setup.py
spec = importlib.util.spec_from_file_location("setup", "manager/setup.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
install_requires = mod.install_requires

# stip version codes
deps = set((x[: x.index(">")].lower() for x in install_requires))

# find out which packages are missing
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = deps - installed

# fail if there are some missing
if len(missing) > 0:
    print(f"Some required packages are missing: {missing}", file=sys.stderr)
    exit(1)
