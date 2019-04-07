ansible-role-mysql
******************

Role to setup MySQL


Variables
=========

mysql_package_release

   Package default release

mysql_root_password

   Password for root user on every login host. Latest MySQL packages
   usually come with UNIX socket authentication enabled by default for
   root. In such case root password won't have any effect. You may
   revert to old behaviour by altering *plugin* column in *mysql.user*
   entry for root.

mysql_package

   Package with MySQL

mysql_python_package

   Package with Python MySQL driver

mysql_service

   MySQL service name

mysql_state

   MySQL service desired state. This value is passed directly to
   *service* module.

   Restart or privilege/access management won't happen, if it's set to
   'stopped'.

mysql_restart

   Restart service when necessary

mysql_enable

   Enable MySQL service

mysql_config_file

   Server configuration file

mysql_client_config_file

   Client configuration file

mysql_client_config

   Client configuration

   By default it will contain access credentials for root

mysql_config

   Server configuration

mysql_users

mysql_databases


Examples
========

   ---
   - hosts: instance
     tasks:
       - import_role:
           name: mysql
         vars:
           mysql_python_package: python3-pymysql
           mysql_root_password: qwe
           mysql_databases:
             db1:
               collation: latin1_swedish_ci
               encoding: latin1
             db2:
           mysql_users:
             - name: db1_owner
               host: 127.0.0.1
               privileges:
                 - "db1.*:ALL"
               password: db1_password
             - name: dbs_owner
               host: 127.0.0.1
               privileges:
                 - "db1.*:ALL"
                 - "db2.*:ALL"
               password: dbs_password


Documentation
=============

Compile:

   $ pip3 install -r requirements.txt
   $ make man

View:

   $ man ./docs/man/ansible-role-mysql.1
