#!/usr/bin/env python
# vim: set fileencoding=UTF-8 :

"""keylogger that send events via OSC.
each keypress generates an event like:
  /keylogger/window/<window>/<keyname>/key <bool:down>
"""

import sys
import hooklib, osc

osc.init()
Host="localhost"
Port=6666

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

def sendevent(event, down):
	bundle=osc.createBundle()
	osc.appendToBundle(bundle, "/keylogger/window/"+str(event.Window)+"/key", [event.Key, down])
	osc.appendToBundle(bundle, "/keylogger/WindowName/"+event.WindowName+"/key", [event.Key, down])
	osc.sendBundle(bundle, Host, Port)
	
 
def OnKeyboardEvent(event):
	#printevent(event)
	if("key down"==event.MessageName):
		sendevent(event, 1)
	elif("key up"==event.MessageName):
		sendevent(event, 0)
	return True

def main(script, port=6666, host="localhost"):
	Host=host
        Port=int(port)
	hm=hooklib.HookManager()
	hm.KeyDown = OnKeyboardEvent
	hm.KeyUp = OnKeyboardEvent
	hm.HookKeyboard()
	hm.start()


if __name__ == '__main__':
	main(*sys.argv)
