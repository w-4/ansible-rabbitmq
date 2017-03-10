import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_rabbitmq_config_file_permissions_must_be_644(File):
    rabbitmq_config = File("/etc/rabbitmq/rabbitmq.config")
    assert rabbitmq_config.exists
    assert rabbitmq_config.is_file
    assert rabbitmq_config.user == 'root'
    assert rabbitmq_config.group == 'rabbitmq'
    assert rabbitmq_config.mode == 0644
