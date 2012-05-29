#!/usr/bin/env python
# vim: set fileencoding=UTF-8 :

"""keylogger that send events via OSC.
each keypress generates an event like:
  /keylogger/window/<window>/<keyname>/key <bool:down>
"""

import sys
import hooklib, osc

class OSCkeylogger:
    host="localhost"
    port=6666
    callback=None

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

    def sendevent(self, event, down):
        bundle=osc.createBundle()
        osc.appendToBundle(bundle, "/keylogger/window/"+str(event.Window)+"/key", [event.Key, down])
        osc.appendToBundle(bundle, "/keylogger/WindowName/"+event.WindowName+"/key", [event.Key, down])
        osc.sendBundle(bundle, self.host, self.port)
        if(self.callback):
            self.callback(str(event.Window), str(event.Key))
	
 
    def OnKeyboardEvent(self, event):
        if("key down"==event.MessageName):
            self.sendevent(event, 1)
        elif("key up"==event.MessageName):
            self.sendevent(event, 0)
        #printevent(event)
        return True

    def __init__(self, host="localhost", port=6666):
        osc.init()
        self.host=host
        self.port=int(port)
        print "reporting to %s:%d" % (self.host, self.port)
        self.hm=hooklib.HookManager()
        self.hm.KeyDown = self.OnKeyboardEvent
        self.hm.KeyUp = self.OnKeyboardEvent
        self.hm.HookKeyboard()

    def start(self):
        self.hm.start()

    def stop(self):
        self.hm.cancel()

    def setHostPort(self, host, port):
        self.host=host
        self.port=port

    def setCallback(self, callback):
        self.callback=callback

def main(script, port=6666, host="localhost"):
    okl = OSCkeylogger(host, port)
    okl.start()


if __name__ == '__main__':
	main(*sys.argv)
