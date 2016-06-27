#!/usr/bin/env python

import argparse
import logging
import signal

import serial, sys

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib


def hw_pomodoro_started():
    if not args.noserial:
        ser.write("P") # we are on a pomodoro

def hw_pomodoro_ended():
    if not args.noserial:
        ser.write("R") # we are on a recess

def catchall_pomodoro_signals_handler(*args, **kwargs):
    # Get the 1st PropertiesChanged signal of the pomodoro and read its `State`
    if args > 0:
        dict = args[1]
        if "State" in dict:
            if dict['State'] == "pomodoro":
                logging.debug('Pomodoro started')
                hw_pomodoro_started()
            # if dict['State'] == "null" or "pause":
            #     logging.debug('Pomodoro ended')
            #     hw_pomodoro_ended()
            if dict['State'] == "null":
                logging.debug('Pomodoro ended')
                hw_pomodoro_ended()
            if dict['State'] == "pause":
                logging.debug('Pomodoro ended')
                hw_pomodoro_ended()
        if logger.isEnabledFor(logging.DEBUG):
            if "Elapsed" in dict:
                logging.debug('Elapsed time %.2s', dict['Elapsed'])

def signal_handler(signal, frame):
    print('Gomoduino received SIGINT, exiting gracefully')
    # Close serial port
    if not args.noserial:
        ser.close()
        logging.debug('Closed serial port')
    # Close d-bus loop
    if not loop is None:
        loop.quit()
        logging.debug('Closed d-bus loop')
    sys.exit(0)


# Setup argpase
parser = argparse.ArgumentParser(
    description='A script for inputting gnome-pomodoro\'s state to serial port')
parser.add_argument("-d", "--debug", help="show debug messages",
                    action="store_true")
parser.add_argument("-ns", "--noserial", help="don't try to connect serial port",
                    action="store_true")
parser.add_argument("-a", "--arduino",
                    help="use /dev/ttyACM0, Arduino Uno's default serial port",
                    action="store_true")
args = parser.parse_args()
if args.debug:
    logging.basicConfig(level=logging.DEBUG)

# Setup logging
logger = logging.getLogger(__name__)

# Set up serial port
if args.arduino:
    SERIALPORT = "/dev/ttyACM0"
else:
    SERIALPORT = "/dev/ttyUSB0"
if not args.noserial:
    try:
        ser = serial.Serial(SERIALPORT, 9600, timeout=0)
    except serial.SerialException:
        print('Cannot connect to serial port')
        sys.exit()

# Setup main event loop to receive asynchronous calls
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

# Connect to the session bus
bus = dbus.SessionBus()
logging.debug('Connected to D-bus')

# Catch all PropertiesChanged signals from Pomodoro
bus.add_signal_receiver(catchall_pomodoro_signals_handler,
                        dbus_interface = "org.freedesktop.DBus.Properties",
                        path="/org/gnome/Pomodoro",
                        signal_name = "PropertiesChanged")

# Run main loop for asynchronous callbacks and receiving signals
loop = GLib.MainLoop()
logging.debug('Starting d-bus loop to catch signals')
signal.signal(signal.SIGINT, signal_handler)
loop.run()

