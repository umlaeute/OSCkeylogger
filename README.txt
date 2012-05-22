OSCkeylogger

this little program logs all keypresses on your computer and sends them via OSC
to a (potentially remote) OSC-receiver.

USAGE:
start with 
$ ./OSCkeylogger.py <port> <host>
this will send all data to <host>:<port> using UDP.
the defaults are:
 host: localhost
 port: 6666

INTERPRETING THE DATA:
key-actions are either key-down or key-up events.
when running in a windowing environment (X, w32), the receiver will receive 
a bundle of two (2) messages for each key-action.
<bundle>
"/keylogger/window/<windowID>/key" <keyname> <keystate>
"/keylogger/WindowName/<windowName>/key" <keyname> <keystate>
</bundle>

<windowID> uniquely identifies a given window, and is something like "0x042000ee"
<windowName> is the title associated with a window, e.g. "Terminal" and might not be unique
<keyname> is the name of the key, e.g. "a"
<keystate> indicates whether the key is pressed down (1) or released (0)


STATUS:
- currently tested on linux/X
- should run on w32 using pyHook
- TODO: OSX support
- TODO: user-interface that allows to change host:port at runtime and to
  shut-down the application
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
