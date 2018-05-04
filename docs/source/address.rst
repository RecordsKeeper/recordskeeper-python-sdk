====================
Address Class Usage
====================

Library to work with RecordsKeeper addresses.

You can generate new address, check all addresses, check address validity, check address permissions, check address balance
by using Address class. You just have to pass parameters to invoke the pre-defined functions.

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

Address Class
-----------------

.. class:: Address

Address class is used to call address related functions like generate new address, list all addresses and no of addresses on the node's wallet, check if given address is valid or not, check if given address has mining permission or not and check a particular address balance on the node functions which are used on the RecordsKeeeper Blockchain. 


**1. Generate new address on the node's wallet**

getAddress() function is used to generate a new wallet address.

.. code-block:: python

    getAddress()  

    newAddress = getAddress()          #getAddress() function call   

    print newAddress                  # prints a new address

It will return a new address of the wallet.


**2. List all addresses and no of addresses on the node's wallet**

retrieveAddresses() function is used to list all addresses and no of addresses on the node's wallet.

.. code-block:: python

    retrieveAddresses()  
    allAddresses, address_count = retrieveAddresses()       #retrieveAddresses() function call
  
    print allAddresses       # prints all the addresses of the wallet
    print address_count      # prints the address count

It will return all the addresses and the count of the addresses on the wallet.

**3. Check validity of the address**

You have to pass address as argument to the checkifValid function call:

* Address: to check the validity

checkifValid() function is used to check validity of a particular address. 

.. code-block:: python

    checkifValid()  
    addressC = checkifValid(address)                #checkifValid() function call 
  
    print addressC      # prints validity

It will return if an address is valid or not.


**4. Check if given address has mining permission or not**

You have to pass address as argument to the checkifMineAllowed function call:

* Address: to check the permission status

checkifMineAllowed() function is used to sign raw transaction by passing transaction hex of the raw transaction and the private key to sign the raw transaction. 

.. code-block:: python

    checkifMineAllowed(address) 
    permissionCheck = checkifMineAllowed(address)   #checkifMineAllowed() function call
    
    print permissionCheck      # prints permission status of the given address

It will return if mining permission is allowed or not.


**5. Check address balance on a particular node**

You have to pass address as argument to the checkifMineAllowed function call:

* Address: to check the balance

checkBalance() function is used to check the balance of the address. 

.. code-block:: python

    checkBalance(address)
    address_balance = checkBalance(address)     #checkBalance() function call
  
    print address_balance    # prints balance of the address

It will return the balance of the address on RecordsKeeper Blockchain.

