# import testinfra.utils.ansible_runner

# testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
#    '.molecule/ansible_inventory').get_hosts('all')


def test_rabbitmq_bin_is_link(File):
    rabbitmq_bin = File("/usr/lib/rabbitmq/bin")
    assert rabbitmq_bin.exists
    assert rabbitmq_bin.is_directory


def test_rabbitmq_sbin_is_present(File):
    rabbitmq_sbin = File("/usr/lib/rabbitmq/sbin")
    assert rabbitmq_sbin.is_symlink


def test_rabbitmq_management_plugin_is_enable(Command):
    list_plugins_command = Command("sudo rabbitmq-plugins list -E -m")
    assert list_plugins_command.stdout == 'rabbitmq_management'
