import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_rabbitmq_is_installed(Package):
    nginx = Package("rabbitmq-server")
    assert nginx.is_installed
    assert nginx.version.startswith("3.3.5")


def test_rabbitmq_running_and_enabled(Service):
    nginx = Service("rabbitmq-server")
    assert nginx.is_enabled
    assert nginx.is_running
