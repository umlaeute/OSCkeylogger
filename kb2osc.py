#!/usr/bin/env python
# vim: set fileencoding=UTF-8 :

import sys
import hooklib, osc

def OnKeyboardEvent(event):
    print 'MessageName:',event.MessageName
#    print 'Message:',event.Message
#    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    print 'Key:', event.Key
    print 'KeyID:', event.KeyID
    print 'ScanCode:', event.ScanCode
#    print 'Extended:', event.Extended
#    print 'Injected:', event.Injected
#    print 'Alt', event.Alt
#    print 'Transition', event.Transition
    print '---'

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
