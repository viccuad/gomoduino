Gomoduino
======

Gomoduino: notify your colleagues when you are on a pomodoro


# But what is it?
Gomoduino provides a traffic light-like sign showcasing when you are on available
and on a break, and when you are on a [pomodoro](http://pomodorotechnique.com).
It was made on a couple of afternoons as an excuse to learn how D-Bus works.

Potato photo:
![gomoduino](https://github.com/viccuad/gomoduino/raw/master/assets/web/gomoduino.jpg)

# How it works
It works in conjunction with [Gnome Pomodoro](http://gnomepomodoro.org),
a Gnome-Shell application for managing your Pomodoros, with presence awareness,
notifications, messaging status changes and more.

![dbus_diagram](https://github.com/viccuad/gomoduino/raw/master/assets/web/bustle_pomodoro_log.png)

Gomoduino is comprised of 2 parts, a Python script, and an Arduino firmware.
Gnome Pomodoro showcases its state by [D-Bus](https://freedesktop.org/wiki/IntroductionToDBus/)
signals. Gomoduino's Python script connects to D-Bus, parses the signals and relays
information about state changes to the Arduino counterpart via serial comm. Then,
the simple Arduino firmware changes the LED output so your folks can leave you be
on your pomodoros.

Here is the Arduino layout:

![arduino_sketch](https://github.com/viccuad/gomoduino/raw/master/assets/web/Sketch_schem.png)

Here is the Python script usage:

```terminal
$ ./gomoduino.py -h
usage: gomoduino.py [-h] [-d] [-ns]

A script for inputting gnome-pomodoro's state to serial port

optional arguments:
  -h, --help       show this help message and exit
  -d, --debug      show debug messages
  -ns, --noserial  don't try to connect serial port

```

See `docs/` for more info on all of it.


# Dependencies
## For the Arduino part

Do it with Arduino IDE

(1). `apt install arduino`

or go console style:

(2). Install [inotool](http://inotool.org/)

  a. For Debian based systems: ```sudo apt-get install python-pip```
  b. Install inotool: ```pip install --user inotool``` (never ever use pip with sudo!)
  c. Add ~/.local/bin to your PATH

## For the Python script:

`apt install python-dbus python-serial`


# Building
## Arduino part
Do it with Arduino IDE or go console style:

(2). `cd firmware`, `ino build`, `ino upload`.

## Python part
You might need to change the serial device you are going to connect to.


# License
![gplv3](https://github.com/viccuad/gomoduino/raw/master/assets/web/gplv3.png)

This work is released under the terms of GPLv3 license. You can find a copy of
the GPLv3 license in LICENSE file.
