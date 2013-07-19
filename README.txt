OSCkeylogger

this little program logs all keypresses on your computer and sends them via OSC (over UDP)
to a (potentially remote) OSC-receiver.

USAGE (GUI):
start the OSCkeyloggerGUI (see below), which should pop up a small window,
where you will see which key is currently pressed in which window, 
and where you are sending those events.
If you want to change the destination, click on "configure" and enter the new host/port 
address.


USAGE (cmdline):
start OSCkeylogger.py with the target address.


STARTING on W32:
just click on OSCkeyloggerGUI.exe, which will start the GUI.

STARTING on linux (or w32 when using python directly):
to start the GUI, run 
$ python ./OSCkeyloggerGUI.py [<port> [<host>]]
to start the cmdline application, run
$ python ./OSCkeylogger.py [<port> [<host>]]

this will send all data to <host>:<port> using UDP.
the defaults are:
 host: localhost
 port: 6666


RECEIVING THE DATA:

the receiver  will receive a bundle of two (2) messages for each key-action (key-up or key-down event).
<bundle>
"/keylogger/window/<windowID>/key" <keyname> <keystate>
"/keylogger/WindowName/<windowName>/key" <keyname> <keystate>
</bundle>

<windowID> uniquely identifies a given window, and is something like "0x042000ee"
<windowName> is the title associated with a window, e.g. "Terminal" and might not be unique
<keyname> is the name of the key, e.g. "a"
<keystate> indicates whether the key is pressed down (1) or released (0)


STATUS:
- currently tested on linux/X and w32
- TODO: OSX support
- TODO: windowless (terminal) support

AUTHOR:
IOhannes m zmölnig, Institute of Electronic Music and Acoustics (IEM), KUG, Graz/Austria

LICENSE:
- OSCkeylogger is released under the Gnu GPL-2

Copyright (C) 2012, IOhannes m zmölnig
Copyright (C) 2012, Institute of Electronic Music and Acoustics (IEM), Graz/Austria

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
