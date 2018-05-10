==================
Stream Class Usage
==================

Library to work with RecordsKeeper streams.

You can publish, retrieve and verify stream data by using stream class.
You just have to pass parameters to invoke the pre-defined functions.

Libraries
---------

Import these python libraries first to get started with the functionality.

.. code-block:: python

    import requests
    import json
    from requests.auth import HTTPBasicAuth
    import yaml
    import binascii
    import sys


Create Connection
-----------------

Entry point for accessing Stream class resources.

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

Stream Class
------------

.. class:: Stream

Stream class to call stream related functions like publish, retrievewithtxid, retrieveWithAddress, retrieveWithKey and verify data functions which are used to publish data into the stream, retrieve data from the stream and verify data from the stream. 

**1. Publish**

You have to pass these four arguments to the publish function call:

* Data Hex of the data to be published
* Address of the publihser
* Stream to which you want your data to be published
* key Value for the data to be published


The **data.hex()** will convert the data into a hex value

.. code-block:: python

    publish(address, stream, key, dataHex)   

    txid = publish(address, stream, key, dataHex)    

    print txid  # prints the transaction id of the data published

It will return a transaction id of the published data, use this information to retrieve the particular data from the stream.


**2. Retrieve an existing item from a particular stream against a transaction id**

You have to pass these two arguments to the retrieve function call:

* Stream name: which you want to access
* Transaction id: id of the data you want to retrieve

.. code-block:: python

    retrieve(stream, txid)  # call retrieve function with stream and txid as the required parameters
    result = retrieve(stream, txid) 
  
    print result    #prints info of the transaction 

It will return the item's details like publisher address, key value, confirmations, hexdata and transaction id.


**3. Retrieve an item against a particular publisher address**

You have to pass these two arguments to the verifyWithAddress function call:

* Stream name: which you want to access
* Publisher address: address of the data publisher you want to verify

.. code-block:: python

    verifyWithKey(stream, address)
    key,data, txid = verifyWithKey(stream, address)

    raw_data = binascii.unhexlify(data).decode('utf-8')         # convert hex data into raw data

    print key       # prints key value of the data
    print data      # prints hex data 
    print txid      # prints transaction id of the data
    print raw_data  # prints raw data 

It will return the key value, hexdata, raw data and transaction id of the published item.

**4. Retrieve an item against a particular key value**

You have to pass these two arguments to the verifyWithKey function call:

* Stream name: which you want to access
* Key: key value of the published data you want to verify

.. code-block:: python

    verifyWithKey(stream, address)
    publisher,data, txid = verifyWithKey(stream, address)

    raw_data = binascii.unhexlify(data).decode('utf-8')         # convert hex data into raw data

    print publisher     # prints publisher's address of the published data
    print data          # prints hex data 
    print txid          # prints transaction id of the data
    print raw_data      # prints raw data 

It will return the key value, hexdata, raw data and transaction id of the published item.

**5. Verify an data item on a particular stream of RecordsKeeper Blockchain**

You have to pass these three arguments to the verifyWithKey function call:

* Stream name: which you want to access
* Data: against which you want to make a query
* Count: count of items which will be queried

.. code-block:: python

    verifyData(stream, data, count)
    result = verifyData(stream, data, count)

    print result     #prints if verification is successful or not

It will return the result if verification is successful or not.


**6. Retrieve data items on a particular stream of RecordsKeeper Blockchain**

You have to pass these two arguments to the verifyWithKey function call:

* Stream name: which you want to access
* Count: count of items which will be queried

.. code-block:: python

    retrieveItems(stream, count)
    address, key_value, raw_data, txid = retrieveItems(stream, count)

    print address     #prints address of the publisher of the item
    print key_value   #prints key value of the stream itme
    print raw_data    #prints raw data published
    print txid        #prints tx id of the item published 

It will return the address, key value, data and transaction id of the stream item published.