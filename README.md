# SaltStack Meetup Demo (06/12/2018)


## <a name='problem'></a> The Problem

Understanding the beacon system and how they can be useful...

The beacon system continually monitors system processes and will send an event to the event bus when triggered. Beacons leverage the Salt reactor system to make 
changes when beacon events occur. Some examples of processes that can be monitored are...

* file system changes
* system load
* service status
* shell activity, such as user login
* network and disk usage

for a full listing of beacon modules check here: [beacon modules](https://docs.saltstack.com/en/2015.8/ref/beacons/all/index.html#all-salt-beacons)

## <a name='configuration'></a> Configuring Beacons

Salt beacons do not require any changes to the system process that is being monitored, everything is configured using Salt.

Beacons are typically enabled by placing a beacons: top level block in the minion configuration file:

```bash
beacons:
  inotify:
    /etc/httpd/conf.d: {}
    /opt: {}
```
The beacon system, like many others in Salt, can also be configured via the minion pillar, grains, or local config file.

  * The inotify beacon only works on OSes that have inotify kernel support. Currently this excludes FreeBSD, Mac OS X, and Windows.

## <a name='interval'></a> Beacon Monitoring Interval

Beacons monitor on a 1-second interval by default. To set a different interval, provide an interval argument to a beacon.
Here is an example of a beacon that runs on 5- and 10-second intervals:

```YAML
beacons:
  inotify:
    /etc/httpd/conf.d: {}
    /opt: {}
    interval: 5
  load:
    1m:
      - 0.0
      - 2.0
    5m:
      - 0.0
      - 1.5
    15m:
      - 0.1
      - 1.0
    interval: 10
```

## <a name='event loops'></a> Avoiding Event Loops

It is important to carefully consider the possibility of creating a loop between a reactor and a beacon. For example, one might set up a beacon 
which monitors whether a file is read which in turn fires a reactor to run a state which in turn reads the file and re-fires the beacon.

To avoid these types of scenarios, the `disable_during_state_run` argument may be set. If a state run is in progress, the beacon will not be run 
on its regular interval until the minion detects that the state run has completed, at which point the normal beacon interval will resume.

```YAML
beacons:
  inotify:
    - files:
        /etc/important_file: {}
    - disable_during_state_run: True
```

## <a name='solution'></a> A Solution


## <a name='dojo'></a> DOJO

Dig into it...

* write a custom beacon plugin ?
* your ideas?
