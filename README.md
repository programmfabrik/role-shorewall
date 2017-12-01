# Ansible Role Shorewall

This role installs and configures the Shoreline Firewall
*'Shorewall'*.

## Example Playbook

```yaml
- hosts: all
  vars:
    shorewall_enabled: yes
    
    # enable IP forwarding
    shorewall_ip_forwarding: "YES"
    
    # Shorewall zones
    shorewall_zones:
      - name: local
        in_options: ""
        options: ""
        out_options: ""
        type: firewall
      - name: pub,
        in_options: ""
        options: ""
        out_options: ""
        type: ipv4
        
    # Shorewall primary interfaces
    shorewall_interfaces:
      - name: '{{ hostvars[inventory_hostname].ansible_default_ipv4.interface }}'
        zone: pub
        options: [ nosmurfs, routefilter=2, tcpflags, dhcp, optional ]
    
    # Shorewall policies
    shorewall_policies:
      - source: local
        dest: pub
        policy: ACCEPT
      - source: all
        dest: all
        policy: REJECT
        log_level: info
      
    # Shorewall rules
    shorewall_rules:
      - section: NEW
        rules:
          - name: allow ICMP echo request/response
            src: all
            dest: all
            proto: icmp
            action: Ping(ACCEPT)
          - name: allow important ICMP
            src: all
            dest: all
            proto: icmp
            action: AllowICMPs(ACCEPT)
          - name: allow SSH traffic from all networks
            src: all
            dest: local
            proto: tcp
            dest_ports: [ssh, rsync]
            action: ACCEPT
            
    # Shorewall masquerade
    shorewall_masquerade:
      - interface: tncmng
        sources:
          - '{{ blunix_admin_net }}'
  roles:
     - role: blunix.role-shorewall
```

# License

Apache-2.0

# Author Information

Service and support for orchestrated hosting environments,
continuous integration/deployment/delivery and various Linux
and open-source technology stacks are available from:

```
Blunix GmbH - Consulting for Linux Hosting 24/7
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: service[at]blunix.org
Phone: (+49) 30 / 12 08 39 90
```
