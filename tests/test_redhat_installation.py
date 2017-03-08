import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_libselinux_python_is_installed(Package):
    libselinux_python = Package("libselinux-python")
    assert libselinux_python.is_installed
