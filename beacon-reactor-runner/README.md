# beacon-reactor-runner

## Setup

#### Start master container:

```bash
docker run --rm -d \
    -v $(pwd)/master/etc:/root/etc \
    -v $(pwd)/master/srv:/srv \
    -h dev-salt-master \
    --name dev-salt-master \
    simplyadrian/allsalt:debian_master_2017.7.2
docker exec -it dev-salt-master bash
```

#### Start minion container:

```bash
docker run --rm -d \
    -v $(pwd)/minion/etc:/root/etc \
    -h dev-ubuntu-minion \
    --name dev-ubuntu-minion \
    simplyadrian/allsalt:ubuntu_minion_2017.7.2
docker exec -it dev-ubuntu-minion bash
```


## Do things on the master

#### Accept the keys:

```bash
salt-key
salt-key -A -y
salt dev-ubuntu-minion test.ping
```

#### Install vim:

```bash
salt '*' pkg.install vim refresh=True
salt dev-ubuntu-minion pkg.install python-pyinotify
```


#### Reactor config:

```bash
cp /root/etc/salt/master.d/reactor.conf /etc/salt/master.d/reactor.conf
```

#### Runner config:

```bash
cp /root/etc/salt/master.d/runners.conf /etc/salt/master.d/runners.conf
```


## Do things on the minion

#### Beacon config:

```bash
mkdir -p /srv/.cark-logs
cp /root/etc/salt/minion.d/beacons.conf /etc/salt/minion.d/beacons.conf
```


## Restart master and minion containers

```bash
docker restart dev-salt-master
docker restart dev-ubuntu-minion
```


## Run it

### View events on the master

```bash
salt-run state.event pretty=true
```


### Trigger the beacon from the minion

```bash
touch /srv/.cark-logs/.cyberark_api_call.log
```

#### Watch the event log

When it's done cat the file:

```bash
cat /srv/.cark-logs/.cyberark_api_call.log
```
