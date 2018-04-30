"""Library to work with RecordsKeeper streams.

   You can publish, retrieve and verify stream data by using stream class.
   You just have to pass parameters to invoke the pre-defined functions."""

""" import requests, json and HTTPBasicAuth packages"""
	
import requests
import json
from requests.auth import HTTPBasicAuth
import yaml
import binascii

""" Entry point for accessing Stream class resources.

	Import values from config file."""

with open("config.yaml", 'r') as ymlfile:
	cfg = yaml.load(ymlfile)

url = cfg['testnet']['url']
user = cfg['testnet']['rkuser']
password = cfg['testnet']['passwd']
chain = cfg['testnet']['chain']


"""Stream class to access stream related functions"""

class Stream:

	
	data = input("enter data:").encode('utf-8')  					#variable to store the data to be published
	
	address = input("enter address:")								#variable to store address of the publisher
	
	stream = input("enter stream:")				 					#variable to store stream to which data is published
	
	key = input("enter key:")					 					#variable to store key value of the data

	dataHex = data. hex()						 					#variable that stores the hex value of the data

	
	"""function to publish data into the stream"""

	def publish(address, stream, key, dataHex):						#publish function definition
		
		headers = { 'content-type': 'application/json'}

		payload = [
		         { "method": "publishfrom",
		          "params": [address,stream,key,dataHex],
		          "jsonrpc": "2.0",
		          "id": "curltext",
		          "chain_name": chain
		          }]

		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()

		return response_json[0]['result']

	
	txid = publish(address, stream, key, dataHex)					#variable to store transaction id

	
	print(txid)														#print transaction id

	
	
	"""function to retrieve data from the stream"""

	def retrieve(stream, txid):										#retrieve function definition

		headers = { 'content-type': 'application/json'}

		payload = [
		         { "method": "getstreamitem",
		          "params": [stream, txid],
		          "jsonrpc": "2.0",
		          "id": "curltext",
		          "chain_name": chain
		          }]
		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()

		return response_json[0]['result']

	result = retrieve(stream, txid)									#call to invoke retrieve function

	print(result)													#print result of the retrieved stream data
	

	address = input("enter address: ")
	stream = input("enter stream: ")


	"""function to verify data against a particular publisher address"""

	def verifyWithAddress(stream, address):					#verifywithaddress function definition

		headers = { 'content-type': 'application/json'}
				
		payload = [
		{ "method": "liststreampublisheritems",
		"params": [stream, address],
		"jsonrpc": "2.0",
		"id": "curltext",
		"chain_name": chain
		}]

		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()

		key = response_json[0]['result'][0]['key']				#returns key value of the published data
		data = response_json[0]['result'][0]['data']			#returns published data
		txid = response_json[0]['result'][0]['txid']			#returns transaction id of the published data

		return key, data, txid;

	key,data, txid = verifyWithAddress(stream, address)				#call to verifyWithKey function

	raw_data = binascii.unhexlify(data).decode('utf-8')

	print("Key of the published data is: ",key)								#print published data key value
	print("Data published is: ",raw_data)									#print published data
	print("Transaction id of the published data is: ",txid)					#print transaction id of published data

	
	key = input("enter key: ")
	stream = input("enter stream: ")


	"""function to verify data against a particular key value"""

	def verifyWithKey(stream, key):								#verifywithkey function definition

		headers = { 'content-type': 'application/json'}
				
		payload = [
		{ "method": "liststreamkeyitems",
		"params": [stream, key],
		"jsonrpc": "2.0",
		"id": "curltext",
		"chain_name": chain
		}]

		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()

		publisher = response_json[0]['result'][0]['publishers'][0]		#returns publisher's address of published data		
		data = response_json[0]['result'][0]['data']			#returns published data
		txid = response_json[0]['result'][0]['txid']			#returns transaction id of published data



		return publisher, data, txid;

	publisher, data, txid = verifyWithKey(stream, key)		#call to verifyWithKey function
	raw_data = binascii.unhexlify(data).decode('utf-8')
			
	print("Publisher of the published data is: ",publisher)					#print publisher address 
	print("Data published is: ",raw_data)	#print published data
	print("Transaction id of the published data is: ",txid)					#print transaction id of published data

		


	

