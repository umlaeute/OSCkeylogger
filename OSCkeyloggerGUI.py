#!/usr/bin/env python
# vim: set fileencoding=UTF-8 :
# (c) 2012, IOhannes m zmölnig

"""keylogger that send events via OSC.
each keypress generates an event like:
  /keylogger/window/<window>/<keyname>/key <bool:down>
"""

from Tkinter import *
import string, os
from threading import Thread

from OSCkeylogger import OSCkeylogger

import tkSimpleDialog
import tkMessageBox


def idleProxy(self):
    self.idleTask()

class OklConfigDialog(tkSimpleDialog.Dialog):
    host="localhost"
    port=6666
    parent=None

    def __init__(self, root, parent, host="localhost", port=6666):
        self.hostport=parent
        tkSimpleDialog.Dialog.__init__(self, root)
        self.host=host
        self.port=port

    def setentries(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)

        if(self.hostport):
            self.host=self.hostport.host
            self.port=self.hostport.port

        self.e1.insert(0, str(self.host))
        self.e2.insert(0, str(self.port))

    def body(self, master):
        Label(master, text="Host:").grid(row=0)
        Label(master, text="Port:").grid(row=1)

        self.e1 = Entry(master)
        self.e2 = Entry(master)

        self.setentries()

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1 # initial focus

    def validate(self):
        try:
            first= str(self.e1.get())
            second = int(self.e2.get())
            if(second<1 or second>65535):
                raise ValueError
            self.host=first
            self.port=second
            return 1
        except ValueError:
            self.setentries()
            tkMessageBox.showwarning(
                "Bad input",
                "Illegal values, please try again"
            )

            return 0

    def apply(self):
        if(self.hostport):
            self.hostport.setHostPort(self.host, self.port)
        else:
            print "no target for setting %s:%d" % (self.host, self.port)

class OklAppWindow():
    top = 0
    host="localhust"
    port=7777
    okl=None

    hostName=None
    portName=None

    windowName=None
    keyName=None
    window_name="???"
    key_name="???"

    def __init__(self, host, port, okl):
        self.top=Tk()
        self.top.title("OSCkeylogger")
        self.top.protocol("WM_DELETE_WINDOW", self.cancel)

        self.host=host
        self.port=port
        self.okl=okl

        self.hostName=StringVar()
        self.hostName.set(self.host)
        self.portName=StringVar()
        self.portName.set(str(self.port))

        self.windowName=StringVar()
        self.windowName.set("???")
        self.keyName=StringVar()
        self.keyName.set("???")

        self.l1 = Label(self.top, text="OSCHost:").grid(row=0)
        self.l2 = Label(self.top, text="OSCPort:").grid(row=1)

        self.e1 = Label(self.top, width=30, textvariable=self.hostName).grid(row=0, column=1)
        self.e2 = Label(self.top, width=30, textvariable=self.portName).grid(row=1, column=1)

        Button(self.top, text="configure", command=self.configure).grid(row=0, column=2)

        self.l3 = Label(self.top, text="Window:").grid(row=3)
        self.e3 = Label(self.top, width=30, textvariable=self.windowName).grid(row=3, column=1)
        self.l4 = Label(self.top, text="Key:").grid(row=4)
        self.e4 = Label(self.top, width=30, textvariable=self.keyName).grid(row=4, column=1)

        self.top.update()
        self.pushHostPort()
        self.idleTask()


    def start(self):
        self.top.mainloop()

    def configure(self):
        d = OklConfigDialog(self.top, self, self.host, self.port)

    def setHostPort(self, host, port):
        self.host=host
        self.port=port
        self.hostName.set(self.host)
        self.portName.set(str(self.port))

        self.pushHostPort()

    def pushHostPort(self):
        self.okl.setHostPort(self.host, self.port)
        self.dump()

    def dump(self):
        print "connecting to %s:%d" % (self.host, self.port)

    def idleTask(self):
        self.updateLabels()
        #self.top.after_idle(idleProxy, self)
        self.top.after(100, idleProxy, self)

    def updateLabels(self):
        if(self.windowName):
            self.windowName.set(self.window_name)
        if(self.keyName):
            self.keyName.set(self.key_name)

    def eventCallback(self, windowname, keyname):
        self.window_name=windowname
        self.key_name=keyname

    def cancel(self):
        self.top.destroy()

class OKLThread(Thread):
    okl=None

    def __init__(self, okl) :
        Thread.__init__(self)
        self.okl=okl

    def run(self):
        if self.okl:
            self.okl.start(False)

    def stop(self) :
        if self.okl:
            self.okl.stop()

def main(script, port=6666, host="localhost"):
    _port=int(port)
    okl = OSCkeylogger(host, _port)
    oklthread=OKLThread(okl)
    oklthread.run()
    app = OklAppWindow(host, _port, okl)
    okl.setCallback(app.eventCallback)
    try:
        app.start()
    except KeyboardInterrupt:
         print 'KeyBoardInterrupt'
    oklthread.stop()

if __name__ == '__main__':
	main(*sys.argv)
