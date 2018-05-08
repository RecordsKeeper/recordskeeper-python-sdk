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


Create Connection
-----------------

Entry point for accessing Transaction class resources.

* URL: Url to connect to the chain ([RPC Host]:[RPC Port])
* Chain-name: chain name

.. code-block:: python

    with open("config.yaml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    url = cfg['testnet']['url']
    chain = cfg['testnet']['chain']

Node we have an entry point to get started.


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

grantPermission() function is used to grant permissions like connect, send, receive, create, issue, mine, activate, admin to an address on RecordsKeeper Blockchain.

.. code-block:: python

    grantPermission(address, permissions)  

    txid = grantPermission(address, permissions)          #grantPermission() function call   

    print txid                  # prints tx id of the permision transaction

It will return the transaction id of the permission transaction.


**2. Revoke Permissions to an address on the RecordsKeeper Blockchain**

revokePermission() function is used to revoke permissions like connect, send, receive, create, issue, mine, activate, admin to an address on RecordsKeeper Blockchain.

.. code-block:: python

    revokePermission(address, permissions)  
    txid = revokePermission(address, permissions)       #revokePermission() function call
  
    print txid                  # prints tx id of the permision transaction

It will return the transaction id of the permission transaction.
