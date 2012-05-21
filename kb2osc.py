#!/usr/bin/env python
# vim: set fileencoding=UTF-8 :

import sys
import hooklib, osc

def printevent(event):
    print 'MessageName:',event.MessageName
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    print 'Key:', event.Key
    print 'KeyID:', event.KeyID
    print 'ScanCode:', event.ScanCode
    print '---'

    return True
 
def OnKeyboardEvent(event):
	printevent(event)
	return True

def main(script, port=6666, host="localhost"):
        port_=int(port)
	osc.init()
	hm=hooklib.HookManager()
	hm.KeyDown = OnKeyboardEvent
	hm.HookKeyboard()
	hm.start()


if __name__ == '__main__':
	main(*sys.argv)
