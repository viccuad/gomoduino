# D-bus Explanation

## Read first: Jargon and overall picture
https://freedesktop.org/wiki/IntroductionToDBus

## Tutorial (WIP)
https://dbus.freedesktop.org/doc/dbus-tutorial.html

## Official dbus-python tutorial
https://dbus.freedesktop.org/doc/dbus-python/doc/tutorial.html

See examples on /usr/share/doc/python-dbus-doc/examples/

## Tutorial using C (kind of meh, with C errors)
http://linoxide.com/how-tos/d-bus-ipc-mechanism-linux


# D-bus logging

## Bustle
A D-Bus activity visualizer.

You can filter visible services on options.


## gbus
```
$ gdbus introspect --session --dest org.gnome.Pomodoro --object-path /org/gnome/Pomodoro
```

```js
node /org/gnome/Pomodoro {
  interface org.freedesktop.DBus.Properties {
    methods:
      Get(in  s interface_name,
          in  s property_name,
          out v value);
      GetAll(in  s interface_name,
             out a{sv} properties);
      Set(in  s interface_name,
          in  s property_name,
          in  v value);
    signals:
      PropertiesChanged(s interface_name,
                        a{sv} changed_properties,
                        as invalidated_properties);
    properties:
  };
  interface org.freedesktop.DBus.Introspectable {
    methods:
      Introspect(out s xml_data);
    signals:
    properties:
  };
  interface org.freedesktop.DBus.Peer {
    methods:
      Ping();
      GetMachineId(out s machine_uuid);
    signals:
    properties:
  };
  interface org.gtk.Actions {
    methods:
      List(out as list);
      Describe(in  s action_name,
               out (bgav) description);
      DescribeAll(out a{s(bgav)} descriptions);
      Activate(in  s action_name,
               in  av parameter,
               in  a{sv} platform_data);
      SetState(in  s action_name,
               in  v value,
               in  a{sv} platform_data);
    signals:
      Changed(as removals,
              a{sb} enable_changes,
              a{sv} state_changes,
              a{s(bgav)} additions);
    properties:
  };
  interface org.freedesktop.Application {
    methods:
      Activate(in  a{sv} platform-data);
      Open(in  as uris,
           in  a{sv} platform-data);
      ActivateAction(in  s action-name,
                     in  av parameter,
                     in  a{sv} platform-data);
    signals:
    properties:
  };
  interface org.gnome.Pomodoro {
    methods:
      ShowPreferences(in  s view,
                      in  u timestamp);
      Start();
      SetState(in  s state,
               in  d state_duration);
      Stop();
      Reset();
    signals:
      NotifyPomodoroEnd(b is_requested);
      NotifyPomodoroStart(b is_completed);
    properties:
      readonly d Elapsed = 1137.2586281299591;
      readonly d StateDuration = 1800.0;
      readonly d Session = 3.7886952405505712;
      readonly d SessionLimit = 4.0;
      readonly s State = 'pomodoro';
      readonly s Version = '0.11.0';
  };
  interface org.gtk.Application {
    methods:
      Activate(in  a{sv} platform-data);
      Open(in  as uris,
           in  s hint,
           in  a{sv} platform-data);
      CommandLine(in  o path,
                  in  aay arguments,
                  in  a{sv} platform-data,
                  out i exit-status);
    signals:
    properties:
      readonly b Busy = false;
  };
  node menus {
  };
};
```

## kdbus
https://liquidat.wordpress.com/2014/03/18/howto-using-dbus-to-query-status-information-from-networkmanager-or-others/


## D-feet



