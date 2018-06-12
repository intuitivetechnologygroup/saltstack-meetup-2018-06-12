# vi /srv/runners/get_api_token.py

from __future__ import absolute_import
import socket

__virtualname__ = 'get_api_token'


def call(config, outputter=None, display_progress=False):
    response = {
        'path': config['path'],
        'minion_id': config['id'],
        'master_hostname': socket.gethostname(),
        'token': 'foo',
    }
    __salt__['event.send']('salt/beacon/response/cark/session', response)
    return response
