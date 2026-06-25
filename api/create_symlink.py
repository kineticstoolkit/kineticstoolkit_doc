#!/usr/bin/env python3
import os
import kineticstoolkit

os.symlink(os.path.dirname(os.path.realpath(kineticstoolkit.__file__)), "ktk")
