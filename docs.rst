ansible-role-mysql
================================================================================

Role to setup MySQL

Variables
--------------------------------------------------------------------------------

mysql_package_release

   Package default release

mysql_root_password

   Password for root user on every login host. Latest MySQL packages usually
   come with UNIX socket authentication enabled by default for root. In such
   case root password won't have any effect. You may revert to old behaviour
   by altering `plugin` column in `mysql.user` entry for root.

.. autoyaml:: defaults/main.yml

Examples
--------------------------------------------------------------------------------

.. literalinclude:: molecule/default/playbook.yml
   :language: yaml

Documentation
--------------------------------------------------------------------------------

Compile::

   $ pip3 install -r requirements.txt
   $ make man

View::

   $ man ./docs/man/ansible-role-mysql.1
