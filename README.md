RabbitMQ
=========

Ansible role to install and configure RabbitMQ server.

#### Requirements
------------

This role requires the previous installation of the EPEL repositories. Alternatively you can use our role to install EPEL (ansible-buy4.repo-epel)

#### Role Variables
--------------

```yaml

rabbitmq_install_enabled: true

rabbitmq_install_major: 3
rabbitmq_install_minor: 3
rabbitmq_install_patch: 5
rabbitmq_install_release: 1
rabbitmq_install_path: "{{ rabbitmq_install_major }}.{{ rabbitmq_install_minor }}.{{ rabbitmq_install_patch }}"
rabbitmq_install_version: "{{ rabbitmq_install_major }}.{{ rabbitmq_install_minor }}.{{ rabbitmq_install_patch }}-{{ rabbitmq_install_release }}"
rabbitmq_package_url: http://www.rabbitmq.com/releases/rabbitmq-server/v{{ rabbitmq_install_path }}/rabbitmq-server-{{ rabbitmq_install_version }}.noarch.rpm

```

#### Dependencies
------------

None yet.

#### Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
        - buy4.repo-epel
        - buy4.rabbitmq
```

#### License
-------

BSD
