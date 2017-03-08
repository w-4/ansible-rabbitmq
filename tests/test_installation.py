import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_rabbitmq_is_installed(Package):
    rabbitmq = Package("rabbitmq-server")
    assert rabbitmq.is_installed
    assert rabbitmq.version.startswith("3.3.5")


def test_earlang_is_installed(Package):
    erlang = Package("erlang")
    assert erlang.is_installed


def test_rabbitmq_running_and_enabled(Service):
    rabbitmq = Service("rabbitmq-server")
    assert rabbitmq.is_enabled
    assert rabbitmq.is_running
