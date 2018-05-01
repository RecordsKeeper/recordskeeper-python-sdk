=================
Block Class Usage
=================

Library to work with RecordsKeeper block informaion.

You can collect block information by using block class.
You just have to pass parameters to invoke the pre-defined functions.

Libraries
---------

Import these python libraries first to get started with the functionality.

.. code-block:: python

    import requests
    import json
    from requests.auth import HTTPBasicAuth
    import yaml


Create Connection
-----------------

Entry point for accessing Stream class resources.

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

Block Class
-----------

.. class:: Block

Block class is used to call block related functions like blockinfo which is used to collect block details like block's hash value, size, nonce, transaction ids, transaction count, and miner address of the block for which you have made the query.

**1. Block info to retrieve block's information**

You have to pass these block height as the argument to the blockinfo function call:

* Block height: height of the block of which you want to collect info

blockinfo() function is used to collect block's information by passing blockheight to the blockinfo function call

.. code-block:: python

    blockinfo(block_height)
    tx_count, tx, miner, size, nonce, blockHash = blockinfo(block_height)       

    print tx_count      # prints transaction count of the block
    print tx            # prints transaction ids of the block
    print size          # prints size of the block
    print blockHash     # prints hash value of the block
    print nonce         # prints nonce of the block
    print miner         # prints miner's address of the block

It will return transaction ids, transaction count, nonce, size, hash value and miner address of the block.


