import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'httpie'
PACKAGE_BINARY = '/usr/bin/http'


def test_httpie_package_installed(host):
    """
    Tests if httpie package is in installed state.
    """
    assert host.package(PACKAGE).is_installed


def test_httpie_binary_exists(host):
    """
    Tests if httpie binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_httpie_binary_file(host):
    """
    Tests if httpie binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_httpie_binary_which(host):
    """
    Tests the output to confirm httpie's binary location.
    """
    assert host.check_output('which http') == PACKAGE_BINARY
