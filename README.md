# recordskeeper-python-sdk


RecordsKeeper-python-lib3 
=========================


It is an infrastructure to build RecordsKeeper blockchain-based applications and products and to work around applications that are built on top of this blockchain.

**Note:** If you're looking for the RecordsKeeper Python Library please see: https://github.com/RecordsKeeper/recordskeeper-python-sdk/tree/python-3.0


## Getting Started

Before you begin you'll need to have python v3 installed. There are several options for installation for python depending on the operating system you are using.


```bash
pip install -g recordskeeper-python-lib3
```

Import these python libraries first to get started with the library classes and functions.

.. code-block:: python

    import requests
    import json
    from requests.auth import HTTPBasicAuth
    import yaml
    import sys
    import binascii

Create Connection
-----------------

Entry point for accessing Address class resources.

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


## Libraries

- [Addresses] Library to work with RecordsKeeper addresses. You can generate new address, check all addresses, check address validity, check address permissions, check address balance by using Address class. You just have to pass parameters to invoke the pre-defined functions.

- [Assets] Library to work with RecordsKeeper assets. You can create new assets and list all assets by using Assets class. You just have to pass parameters to invoke the pre-defined functions.

- [Block] Library to work with RecordsKeeper block informaion. You can collect block information by using block class. You just have to pass parameters to invoke the pre-defined functions.

- [Blockchain]Library to work with RecordsKeeper block informaion. You can collect block information by using block class. You just have to pass parameters to invoke the pre-defined functions.

- [Permissions]Library to work with RecordsKeeper permissions. You can grant and revoke permissions like connect, send, receive, create, issue, mine, activate, admin by using Assets class. You just have to pass parameters to invoke the pre-defined functions.

- [Stream]Library to work with RecordsKeeper streams. You can publish, retrieve and verify stream data by using stream class. You just have to pass parameters to invoke the pre-defined functions.

- [Transaction]Library to work with RecordsKeeper transactions. You can send transaction, create raw transaction, sign raw transaction, send raw transaction, send signed transaction, retrieve transaction information and calculate transaction's fees by using transaction class. You just have to pass parameters to invoke the pre-defined functions.

- [Wallet]Library to work with RecordsKeeper wallet functionalities. You can create wallet, dump wallet into a file, backup wallet into a file, import wallet from a file, lock wallet, unlock wallet, change wallet's password, retrieve private key, retrieve wallet's information, sign and verify message by using wallet class. You just have to pass parameters to invoke the pre-defined functions.


##Tests

- To run all the test cases:

```bash
pip install -g recordskeeper-python-lib3
```

- To run a particular test case:

```bash
pip install -g recordskeeper-python-lib3
```

- To run test cases with **green**:

```bash
pip install -g recordskeeper-python-lib3
```


## Documentation

The complete docs are here: [RecordsKeeper python library documentation](https://github.com/RecordsKeeper/recordskeeper-python-sdk/tree/python-3.0/docs/source).

- [Read for python version 3 or greater](https://github.com/RecordsKeeper/recordskeeper-python-sdk/tree/python-3.0/docs/source)
- [Read for python version 2](https://github.com/RecordsKeeper/recordskeeper-python-sdk/tree/master/docs)


## License

Copyright (c) 2016-2018 Recordskeeper 
License: GNU General Public License version 3, see COPYING

Portions copyright (c) 2014-2017 Coin Sciences Ltd
Portions copyright (c) 2009-2016 The Bitcoin Core developers
Portions copyright many others - see individual files