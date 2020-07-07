import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rabbitmq_config_file_permissions_must_be_644(host):
    rabbitmq_config = host.file("/etc/rabbitmq/rabbitmq.config")
    assert rabbitmq_config.exists
    assert rabbitmq_config.is_file
    assert rabbitmq_config.user == 'rabbitmq'
    assert rabbitmq_config.group == 'rabbitmq'
    assert rabbitmq_config.mode == 0o644


def test_rabbitmq_guest_user_not_present(host):
    rabbitmq_users = host.run("rabbitmqctl list_users")
    assert "guest" not in rabbitmq_users.stdout


def test_rabbitmq_rabbit_user_present(host):
    rabbitmq_users = host.run("rabbitmqctl list_users")
    assert "admin" in rabbitmq_users.stdout


def test_rabbitmq_rabbit_local_user_present(host):
    rabbitmq_user = host.user("rabbitmq")
    assert rabbitmq_user.exists
