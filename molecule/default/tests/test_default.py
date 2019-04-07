import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service(host):
    assert host.service('mysql').is_running
    assert host.socket('tcp://127.0.0.1:3306').is_listening


def test_configuration(host):
    my_cnf = host.file('/etc/mysql/my.cnf')
    assert my_cnf.contains(r'^socket = /var/run/mysqld/mysqld.sock$')
    assert my_cnf.contains(r'^pid-file = /var/run/mysqld/mysqld.pid$')
    assert my_cnf.contains(r'^\[mysqld_safe\]$')
    assert my_cnf.contains(r'^\[mysqld\]$')
    assert my_cnf.contains(r'^port = 3306$')
    user_my_cnf = host.file('/root/.my.cnf')
    assert user_my_cnf.mode == 0o400
    assert user_my_cnf.contains(r'^\[client\]$')
    assert user_my_cnf.contains(r'^user = root$')
    assert user_my_cnf.contains(r'^password = qwe$')


def test_accounts(host):
    assert host.run(
        'mysql -u db1_owner -pdb1_password -h 127.0.0.1 db1 -e ""'
    ).rc == 0
    assert host.run(
        'mysql -u db1_owner -pdb1_password -h 127.0.0.1 db2 -e ""'
    ).rc == 1
    assert host.run(
        'mysql -u dbs_owner -pdbs_password -h 127.0.0.1 db1 -e ""'
    ).rc == 0
    assert host.run(
        'mysql -u dbs_owner -pdbs_password -h 127.0.0.1 db2 -e ""'
    ).rc == 0
    assert host.run('mysql -e ""').rc == 0
