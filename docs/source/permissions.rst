=======================
Permissions Class Usage
=======================

Library to work with RecordsKeeper permissions.

You can grant and revoke permissions like connect, send, receive, create, issue, mine, activate, admin by using Assets class. You just have to pass parameters to invoke the pre-defined functions.

Libraries
---------

Import these python libraries first to get started with the functionality.

.. code-block:: python

    import requests
    import json
    from requests.auth import HTTPBasicAuth
    import yaml
    import sys
    import binascii


Creating Connection
-------------------

Entry point for accessing Address class resources.

Config file to import config parameters:

```bash
    
    with open("config.yaml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
```
   
Importing chain url and chain name from config file:

* URL: Url to connect to the chain ([RPC Host]:[RPC Port])
* Chain-name: chain name

```bash

    url = network['url']
    chain = network['chain']

```   

Node Authentication
-------------------

Import values from config file.

* User name: The rpc user is used to call the APIs.
* Password: The rpc password is used to authenticate the APIs.

.. code-block:: python
    
    user = cfg['testnet']['rkuser']
    password = cfg['testnet']['passwd']

Now we have node authentication credentials.

Permissions Class
-----------------

.. class:: Permissions

Permissions class is used to call permissions related functions like grant and revoke permissions for an address functions which are used on the RecordsKeeeper Blockchain. 


**1. Grant Permissions to an address on the RecordsKeeper Blockchain**

You have to pass these two arguments to the grantPermission function call:

* Permissions: list of comma-seperated permissions passed as a string 
* Address: to which you have to grant permission 

grantPermission() function is used to grant permissions like connect, send, receive, create, issue, mine, activate, admin to an address on RecordsKeeper Blockchain.

.. code-block:: python

    grantPermission(address, permissions)  

    result = grantPermission(address, permissions)          #grantPermission() function call   

    print txid                  # prints response of the grant permision transaction

It will return the transaction id of the permission transaction.


**2. Revoke Permissions to an address on the RecordsKeeper Blockchain**

You have to pass these two arguments to the revokePermission function call:

* Permissions: list of comma-seperated permissions passed as a string 
* Address: to which you have to grant permission 

revokePermission() function is used to revoke permissions like connect, send, receive, create, issue, mine, activate, admin to an address on RecordsKeeper Blockchain.

.. code-block:: python

    revokePermission(address, permissions)  
    result = revokePermission(address, permissions)       #revokePermission() function call
  
    print result                # prints response of the revoke permision transaction

It will return the transaction id of the permission transaction.
