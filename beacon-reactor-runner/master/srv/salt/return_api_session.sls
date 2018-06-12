# File: /srv/salt/return_api_session.sls

set-cark-minion-session:
  file.managed:
    - name: {{ pillar['path'] }}
    - contents: |
        {{ pillar['master_hostname'] }}
