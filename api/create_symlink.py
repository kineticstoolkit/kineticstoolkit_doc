#!/usr/bin/env python3
import os
import kineticstoolkit

os.chdir(os.path.dirname(os.path.dirname(os.path.realpath(kineticstoolkit.__file__))))
os.symlink("kineticstoolkit", "ktk")
