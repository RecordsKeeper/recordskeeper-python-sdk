#stream class

#variables
data: a variable that stores the data to be uploaded
address: a variable to store address of the publisher
stream: a variable to store stream to which data is published
key: a variable to store key value of the data
dataHex: a variable to store hex value of the data
txid : a variable to store txid of the published data


#functions

publish: a function used to publish data into the stream by passing address, stream, key and hex value of the data as the required parameters
retrieve: a function used to retrieve stream data by passing stream name and txid as the required parameters
verify: a function used to verify data against key value or publisher's address
verifyWithKey: a function to verify data against key value
verifyWithAddress: a function to verify data against publisher's address


