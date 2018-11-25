import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_config(host):
    f = host.file("/etc/shorewall/shorewall.conf")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o640


def test_zones(host):
    f = host.file("/etc/shorewall/zones")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o640
    assert f.content_string.split("\n")[-1] == "pub   ipv4"


def test_interfaces(host):
    f = host.file("/etc/shorewall/interfaces")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o640


def test_policy(host):
    f = host.file("/etc/shorewall/policy")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o640
    assert f.content_string.split("\n")[-2] == "local   pub   ACCEPT"
    assert f.content_string.split("\n")[-1] == "all   all   REJECT   info"


def test_rules(host):
    f = host.file("/etc/shorewall/rules")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o640

    lines = f.content_string.split("\n")

    assert "ACCEPT all local tcp ssh,rsync" in [e.strip() for e in lines]
