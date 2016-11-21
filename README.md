Ansible *Audiokitt server* role
========================================

A minimal Ansible role that installs and configureas a minimal [Audiokitt](http://audiokitt.org/) server.


Requirements
------------

 - Debian 8.x
   + Debian < 8.x: We don't have any reasons to support older versions. Most things actually should work fine, but `wheezy`does not include `nodejs`/`npm`
   + ubuntu: Should/could work as well, but has never been tested.

 - The instance used to deploy to should have at least **5GB** of free disk space.


Role Variables
--------------

- `audiokitt_hostname`: my.local.proxy.example.com
- `audiokitt_include_nginx`: install local nginx instance


Example Playbook
----------------

Minimal usage example:

    - hosts: audiokitt
      roles:
        - {
            role: hzlf.audiokitt-server,
            audiokitt_hostname: "my.local.proxy.example.com",
          }


License
-------

BSD
