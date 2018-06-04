==================
Assets Class Usage
==================

Library to work with RecordsKeeper assets.

You can create new assets and list all assets by using Assets class. You just have to pass parameters to invoke the pre-defined functions.

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

Entry point for accessing Assets class resources.

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

Default value of network is **Test-net**, you can change its value to select mainnet or testnet

.. code-block:: python
    
    network = cfg['testnet']                    #network variable to store the network that you want to access

    if (network==cfg['testnet']):

        user = cfg['testnet']['rkuser']
        password = cfg['testnet']['passwd']
        
    else:

        user = cfg['mainnet']['rkuser']
        password = cfg['mainnet']['passwd']

Now we have node authentication credentials.

Assets Class
------------

.. class:: Assets

Assets class is used to call assets related functions like create assets and list assets functions which are used on the RecordsKeeeper Blockchain. 


**1. Create Assets on the RecordsKeeper Blockchain**

createAsset() function is used to create or issue an asset.

.. code-block:: python

    createAsset(address, asset_name, asset_qty)  

    txid = createAsset(address, asset_name, asset_qty)          #createAsset() function call   

    print txid                  # prints tx id of the issued asset

It will return the transaction id of the issued asset.


**2. List all assets on the RecordsKeeper Blockchain**

retrieveAssets() function is used to list all assets, no of assets, issued quantity and issued transaction id of all the assets on RecordsKeeper Blockchain.

.. code-block:: python

    retrieveAssets()  
    asset_name, issue_id, issue_qty, asset_count = retrieveAssets()       #retrieveAssets() function call
  
    print asset_name       # prints all the addresses of the wallet
    print asset_count      # prints the address count
    print issue_qty        # prints assets issued quantity
    print issue_id         # prints assets issued transaction id

It will return all the assets, the count of the assets, issued quantity of assets and issued transaction id of the asset on the RecordsKeeper Blockchain.


