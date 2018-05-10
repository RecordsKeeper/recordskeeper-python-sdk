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
    import sys


Create Connection
-----------------

Entry point for accessing Block class resources.

* URL: Url to connect to the chain ([RPC Host]:[RPC Port])
* Chain-name: chain name

.. code-block:: python
    
    with open("config.yaml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

Default value of network is **Test-net**, you can change its value to select mainnet or testnet

.. code-block:: python

    network = cfg['testnet']                    #network variable to store the network that you want to access

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


Block Class
-----------

.. class:: Block

**1. Block info to retrieve block information**

Block class is used to call block related function like blockinfo which is used to retrieve block details like block's hash value, size, nonce, transaction ids, transaction count, miner address, previous block hash, next block hash, merkleroot, blocktime and difficulty of the block for which you have made the query.

You have to pass these block height as the argument to the blockinfo function call:

* Block height: height of the block of which you want to collect info

.. code-block:: python

    blockinfo(block_height)
    tx_count, tx, miner, size, nonce, blockHash, prevblock, nextblock, merkleroot, blocktime, difficulty = blockinfo(block_height)

    print tx_count      # prints transaction count of the block
    print tx            # prints transaction ids of the block
    print size          # prints size of the block
    print blockHash     # prints hash value of the block
    print nonce         # prints nonce of the block
    print miner         # prints miner's address of the block
    print nextblock     # prints next block's hash
    print prevblock     # prints previous block's hash
    print merkleroot    # prints merkle root of the block
    print blocktime     # prints time at which block is mined
    print difficulty    # prints difficulty of the block

It will return transaction ids, transaction count, nonce, size, hash value, previous block's hash value, next block hash value, merkle root, difficulty, blocktime and miner address of the block.


**2. Retrieve a range of blocks on RecordsKeeper chain**

You have to pass these block height as the argument to the retrieveBlocks function call:

* Block range: range of the block of which you want to collect info

. code-block:: python

    . code-block:: python

    retrieveBlocks(block_range)
    block_hash, miner_add, block_time, txcount = retrieveBlocks(block_range)

    print block_hash    # prints hash of the blocks
    print miner_add     # prints miner of the blocks
    print block_time    # prints block time of the blocks
    print txcount       # prints transaction count of the blocks

It will return blockhash, miner address, blocktime and transaction count of the blocks.
