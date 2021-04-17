# Install naoqi

+ Download it from [https://developer.softbankrobotics.com/pepper-naoqi-25-downloads-linux]().
+ Unpack it.
+ Add this directory to the content root of the pycharm project: `pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages`. I have placed a version of the library on dropbox, therefore the following can be added: `/home/dieter/Dropbox/PythonRepos/`

# Start local server

`python3 -m http.server`

# Using signals

```
[Memory]

|
| subscribe to event
v

This creates a signal [Signal] 

| 
| Connect function to signal
|
V
Returns a signal ID that can be used to disconnect


on[event] functions already return a signal to which a function can be connected
```