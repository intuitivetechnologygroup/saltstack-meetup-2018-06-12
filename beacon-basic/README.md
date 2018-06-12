# beacon-basic

## Setup

#### Start master container:

```bash
docker run --rm -d \
    -v $(pwd)/master.d:/etc/salt/master.d \
    -h dev-salt-master \
    --name dev-salt-master \
    simplyadrian/allsalt:debian_master_2017.7.2
docker exec -it dev-salt-master bash
```

#### Start minion container:

```bash
docker run --rm -d \
    -v $(pwd)/minion.d:/etc/salt/minion.d \
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
salt \* test.ping
```

#### Install vim:

```bash
salt dev-ubuntu-minion pkg.install vim refresh=True
salt dev-ubuntu-minion pkg.install python-pyinotify
```


#### Setup beacon watch file

From the minion, create a file named `/etc/important_file` and add some simple content:

```bash
echo "important_config: True" > /etc/important_file
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

**Edit /etc/important_file:**

```bash
vi /etc/important_file
# edit it and save
```

#### Watch the event log

You should see an event like this:

```bash
salt/beacon/dev-ubuntu-minion/inotify//etc/important_file    {
    "_stamp": "2017-11-26T18:55:06.015431",
    "change": "IN_IGNORED",
    "id": "dev-ubuntu-minion",
    "path": "/etc/important_file"
}
```
