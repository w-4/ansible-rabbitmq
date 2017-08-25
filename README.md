RabbitMQ
=========

Ansible role to install and configure RabbitMQ server.

## Note

A good practice is to have, before using this, clear knowledge of what are the plugins you're going to need. By
default, this role enables the management plugin, here is a example of a playbook that enables more plugins.

```yaml
---
- name: queue service
  hosts: your_hosts
  become: true
  roles:
    - role: stone-payments.rabbitmq
      rabbitmq_plugins:
        - rabbitmq_management
        - rabbitmq_shovel
        - rabbitmq_shovel_management
```

## Requirements
------------
Before using this role make sure that the machines that will compose the cluster connect to each other - via ping or
name resolution. Also make sure that they can connect to the Internet to download RabbitMQ package.

For RedHat machines make sure the machines are subscribed. Also, this role requires the previous installation of the
EPEL repositories. Alternatively, you can use our role
[stone-payments.epel](https://github.com/stone-payments/ansible-epel) to install EPEL.

## Role Variables
--------------

```yaml

# Take the package given by the OS/distrib
rabbitmq_os_package: false

# Allways install RabbitMQ, unless it's already installed and you don't want it to be replaced
rabbitmq_install_enabled: true

# Install specific RabbitMQ version, unless it's redefined
rabbitmq_install_major: 3
rabbitmq_install_minor: 3
rabbitmq_install_patch: 5
rabbitmq_install_release: "*"
rabbitmq_install_version: "{{ rabbitmq_install_major }}.{{ rabbitmq_install_minor }}.{{ rabbitmq_install_patch }}-{{ rabbitmq_install_release }}"

# TCP configuration
rabbitmq_conf_tcp_listeners_address: ''
rabbitmq_conf_tcp_listeners_port: 5672

# RabbitMQ configuration
rabbitmq_config_file_path: "/etc/rabbitmq/rabbitmq.config"
rabbitmq_env_variables_file_path: "/etc/rabbitmq/rabbitmq-env.config"
rabbitmq_config_file_owner: root
rabbitmq_config_file_group: rabbitmq
rabbitmq_config_file_mode: 0644

rabbitmq_users_remove:
  - guest

rabbitmq_users:
  - rabbitmq

# RabbitMQ plugins
rabbitmq_bin_path: "/usr/lib/rabbitmq/bin"
rabbitmq_sbin_path: "/usr/lib/rabbitmq/sbin"
rabbitmq_plugins_prefix_path: "/usr/lib/rabbitmq"
rabbitmq_plugins:
  - rabbitmq_management

# RabbitMQ cluster
rabbitmq_clustering_enabled: false
rabbitmq_erlang_cookie_file_path: "/var/lib/rabbitmq/.erlang.cookie"

```

## Dependencies
------------

None yet.

## Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
        - stone-payments.rabbitmq
```

The specific RabbitMQ environment variables can also be given.

```yaml
    vars:
      rabbitmq_conf_env:
        RABBITMQ_NODE_IP_ADDRESS: "127.0.0.2"
        RABBITMQ_NODENAME: "nodename"
```

## Testing
-------------

This role was developed using [Molecule](https://molecule.readthedocs.io). The `molecule.yml` and the `playbook.yml`
for testing are on the root of this role.

## License
-------

MIT

## To Do
-------------
  - Set specific permissions and priviledges to specific users
  - Install latest version when a version number is not given
  - Add tests for the conection/read/write of rabbit's queues
  - Test removing flush_handlers from clustering step
  - Bug: when the master is down and the clustering step is run all the other nodes will go down.
  - App start with service start
