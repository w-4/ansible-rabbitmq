# import testinfra.utils.ansible_runner

# testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
#    '.molecule/ansible_inventory').get_hosts('group2')


def test_rabbitmq_erlang_cookie_is_present(File, Sudo):
    with Sudo():
        erlang_cookie = File("/var/lib/rabbitmq/.erlang.cookie")
        assert erlang_cookie.exists
        assert erlang_cookie.is_file
        assert erlang_cookie.user == 'rabbitmq'
        assert erlang_cookie.group == 'rabbitmq'
        assert erlang_cookie.mode == 0400


def test_rabbitmq_erlang_cookie_not_empty(File, Sudo):
    with Sudo():
        erlang_cookie = File("/var/lib/rabbitmq/.erlang.cookie")
        assert erlang_cookie.content_string != ""
        assert len(erlang_cookie.content_string) != 0


def test_rabbitmq_erlang_cookie_contains_cookie(File, Sudo):
    with Sudo():
        erlang_cookie = File("/var/lib/rabbitmq/.erlang.cookie")
        assert erlang_cookie.content_string == "QDRDOLMCHSLSZMCRBQYV"
        assert len(erlang_cookie.content_string) == 20
