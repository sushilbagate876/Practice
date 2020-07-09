#!/usr/bin/python3

import os
import platform
import site
from subprocess import call
import multiprocessing

print(os.name)
print(platform.system())
print(platform.release())
print(site.getsitepackages())
call(["ls","-l"])
print("practice.py",os.path.realpath(__file__))
print(multiprocessing.cpu_count())

