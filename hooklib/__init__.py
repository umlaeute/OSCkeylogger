
__version__ = "0"
__author__ = "IOhannes m zmölnig @ IEM"
__license__ = "GNU General Public License"
__all__ = ["oscAPI", "OSC"]

import os

if os.name == 'posix':
    import pyxhook as hooklib
elif os.name == 'nt':
    import pyHook as hooklib
    import pythoncom
else:
    print "OS is not recognised as windows or linux."
    exit()

