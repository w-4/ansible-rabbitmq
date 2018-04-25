import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rabbitmq_bin_is_link(host):
    rabbitmq_bin = host.file("/usr/lib/rabbitmq/bin")
    assert rabbitmq_bin.exists
    assert rabbitmq_bin.is_directory


def test_rabbitmq_sbin_is_present(host):
    rabbitmq_sbin = host.file("/usr/lib/rabbitmq/sbin")
    assert rabbitmq_sbin.is_symlink


def test_rabbitmq_management_plugin_is_enable(host):
    list_plugins_command = host.run("sudo rabbitmq-plugins list -E -m")
    assert 'rabbitmq_management' in list_plugins_command.stdout
