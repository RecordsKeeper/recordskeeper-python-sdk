=======================
Permissions Class Usage
=======================

Library to work with RecordsKeeper permissions.

You can grant and revoke permissions like connect, send, receive, create, issue, mine, activate, admin by using Assets class. You just have to pass parameters to invoke the pre-defined functions.

Create Connection
-----------------

Entry point for accessing Stream class resources.

* URL: Url to connect to the chain ([RPC Host]:[RPC Port])
* Chain-name: chain name

.. code-block:: python
    
    with open("config.yaml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

Default value of network is **test-net**, you can change its value to select mainnet or testnet

.. code-block:: python

    network = cfg['testnet']                    #network variable to store the network that you want to access

    if (network==cfg['testnet']):

        user = cfg['testnet']['rkuser']
        password = cfg['testnet']['passwd']
        
    else:

        user = cfg['mainnet']['rkuser']
        password = cfg['mainnet']['passwd']
    

Node Authentication
-------------------

Import values from config file.

* User name: The rpc user is used to call the APIs.
* Password: The rpc password is used to authenticate the APIs.

.. note::
    
    * Set this **network** value to change the network-type
    * Default network is **Test network**, you can change its value to select mainnet or testnet


.. code-block:: python
    
    network = cfg['testnet']                    #network variable to store the network that you want to access

.. code-block:: python 

    if (network==cfg['testnet']):

        url = cfg['testnet']['url']
        chain = cfg['testnet']['chain']
        
    else:

        url = cfg['mainnet']['url']
        chain = cfg['mainnet']['chain']


Now we have node authentication credentials.


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
