OSC keylogger

this little program logs all keypresses on your computer and sends them via OSC
to a (potentially remote) OSC-receiver.

USAGE:
start with 
$ ./kb2osc.py <port> <host>
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



