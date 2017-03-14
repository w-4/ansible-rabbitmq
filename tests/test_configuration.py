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


def test_rabbitmq_guest_user_not_present(User):
    guest_user = User("guest")
    assert not guest_user.exists


def test_rabbitmq_rabbit_user_present(User):
    rabbitmq_user = User("rabbitmq")
    assert rabbitmq_user.exists
