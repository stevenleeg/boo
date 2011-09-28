import os
import sys
from setuptools import setup

if sys.platform.startswith('win32'):
        requires = ['pywin32']
else:
        requires = []

setup(
	name = 'boom',
	version = '0.1',
	py_modules = ['boom'],
	scripts = ['boo'],
        requires = requires,
)
