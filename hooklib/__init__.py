#!/usr/bin/python
# -*- coding: UTF-8 -*-

__version__ = "0"
__author__ = "IOhannes m zmölnig @ IEM"
__license__ = "GNU General Public License"
__all__ = ["HookManager", ]

import os

if os.name == 'posix':
    import pyxhook
    class HookManager(pyxhook.HookManager):
	def start(self, needPump=True):
		pyxhook.HookManager.start(self)

elif os.name == 'nt':
    import pyHook
    import pythoncom

    class HookManager(pyHook.HookManager):
	def start(self, needPump=True):
            if(needPump):
                pythoncom.PumpMessages()
            else:
                print "not starting to pump messages"

        def cancel(self):
            print "ignoring HookManager.stop"
else:
    print "OS is not recognised as windows or linux."
    exit()


