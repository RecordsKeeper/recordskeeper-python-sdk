======================
Blockchain Class Usage
======================

Library to work with Blockchain in RecordsKeeper Blockchain.

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

Entry point for accessing Blockchain class resources.

* URL: Url to connect to the chain ([RPC Host]:[RPC Port])
* Chain-name: chain name

.. code-block:: python
    
    with open("config.yaml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

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
    

Node Authentication
-------------------

Import values from config file.

* User name: The rpc user is used to call the APIs.
* Password: The rpc password is used to authenticate the APIs.

Default value of network is **Test network**, you can change its value to select mainnet or testnet

.. code-block:: python
    
    network = cfg['testnet']                    #network variable to store the network that you want to access

    if (network==cfg['testnet']):

        url = cfg['testnet']['url']
        chain = cfg['testnet']['chain']
        
    else:

        url = cfg['mainnet']['url']
        chain = cfg['mainnet']['chain']


Now we have node authentication credentials.

Blockchain Class
----------------

.. class:: Blockchain

Blockchain class is used to call blockchain related functions like retrieving blockchain parameters, retrieving node's information, retrieving mempool's information, retrieving node's permissions and check node's balance functions which are used on the RecordsKeeeper Blockchain. 


**1. Retrieve Blockchain parameters of RecordsKeeper Blockchain**

getChainInfo() function is used to retrieve Blockchain parameters.

.. code-block:: python

    getChainInfo()  

    chain_protocol, chain_description, root_stream, max_blocksize, default_networkport, default_rpcport, mining_diversity, chain_name = getChainInfo()             #getChainInfo() function call   

    print chain_protocol                  #prints blockchain's protocol
    print chain_description               #prints blockchain's description
    print root_stream                     #prints blockchain's root stream
    print max_blocksize                   #prints blockchain's maximum block size
    print default_networkport             #prints blockchain's default network port
    print default_rpcport                 #prints blockchain's default rpc port
    print mining_diversity                #prints blockchain's mining diversity
    print chain_name                      #prints blockchain's name

It will return the information about RecordsKeeper blockchain's parameters.


**2. Retrieve node's information on RecordsKeeper Blockchain**

getNodeInfo() function is used to retrieve node's information on RecordsKeeper Blockchain.

.. code-block:: python

    getNodeInfo()  
    node_balance, synced_blocks, node_address, difficulty = getNodeInfo()       #getNodeInfo() function call
  
    print node_balance       #prints balance of the node
    print synced_blocks      #prints no of synced blocks
    print node_address       #prints node's address
    print difficulty         #prints node's difficulty 

It will return node's balance, no of synced blocks, node's address and node's difficulty.


**3. Retrieve permissions given to the node on RecordsKeeper Blockchain**

permissions() function is used to retrieve node's permissions. 

.. code-block:: python

    permissions()  
    allowed_permissions = permissions()                #permissions() function call 
  
    print allowed_permissions      # prints permissions available to the node

It will return the permissions available to the node.


**4. Retrieve pending transaction's information on RecordsKeeper Blockchain**

getpendingTransactions() function is used to retrieve pending transaction's information like no of pending transactions and the pending transactions. 

.. code-block:: python

    getpendingTransactions() 
    pendingtx, pendingtxcount = getpendingTransactions(address)   #getpendingTransactions() function call
    
    print pendingtx             # prints pending transactions
    print pendingtxcount        #prints pending transaction count

It will return the information of pending transactions on Recordskeeper Blockchain.


**5. Check node's total balance**

checkNodeBalance() function is used to check the total balance of the node. 

.. code-block:: python

    checkNodeBalance()
    node_balance = checkNodeBalance()     #checkNodeBalance() function call
  
    print node_balance    # prints total balance of the node

It will return the total balance of the node on RecordsKeeper Blockchain.

