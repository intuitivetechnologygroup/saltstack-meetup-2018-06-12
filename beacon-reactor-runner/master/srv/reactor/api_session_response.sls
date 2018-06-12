return-session:
  local.state.apply:
    - tgt: "{{ data['minion_id']}}"
    - arg:
      - return_api_session
    - kwarg:
        pillar:
          master_hostname: "{{ data['master_hostname'] }}"
          minion_id: "{{ data['minion_id'] }}"
          path: "{{ data['path'] }}"
