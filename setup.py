# to generate an exe file, run
# $ python setup.py py2exe

from distutils.core import setup
import os

if os.name == 'nt':
    import py2exe

    setup(console=['OSCkeylogger.py'])
    setup(windows=['OSCkeyloggerGUI.py'])
