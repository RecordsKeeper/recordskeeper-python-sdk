"""Library to work with RecordsKeeper Blockchain.

   You can send, retrieve and verify transactions by using transaction class.
   You just have to pass parameters to invoke the pre-defined functions."""

""" import requests, json, HTTPBasicAuth, yaml, sys and binascii packages"""

import requests
import json
from requests.auth import HTTPBasicAuth
import yaml
import sys
import binascii

""" Entry point for accessing Blockchain class resources.

	Import values from config file."""

with open("config.yaml", 'r') as ymlfile:
	cfg = yaml.load(ymlfile)

url = cfg['testnet']['url']
user = cfg['testnet']['rkuser']
password = cfg['testnet']['passwd']
chain = cfg['testnet']['chain']


#Blockchain class to access blockchain related functions
class Blockchain:

	"""function to retrieve RecordsKeeper Blockchain parameters"""

	def getChainInfo():								#getChainInfo() function definition
		
		headers = { 'content-type': 'application/json'}

		payload = [
		         { "method": "getblockchainparams",
		          "params": [],
		          "jsonrpc": "2.0",
		          "id": "curltext",
		          "chain_name": chain
		          }]
		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()
			
		result = response_json[0]['result']
			
		# add all those params here
		return result;										#returns chain params

	#chain = getChainInfo()				 #call to function getChainInfo()	



	"""function to retrieve node's information on RecordsKeeper Blockchain"""

	def getNodeInfo():								#getNodeInfo() function definition

		headers = { 'content-type': 'application/json'}

		payload = [
		 	{ "method": "getinfo",
		      "params": [],
		      "jsonrpc": "2.0",
		      "id": "curltext",
		      "chain_name": chain
		    }]

		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()
			
		node_balance = response_json[0]['result']['balance']
		synced_blocks = response_json[0]['result']['blocks']
		node_address = response_json[0]['result']['nodeaddress']

		return node_balance, synced_blocks, node_address;			#returns node details

	#node = getNodeInfo(public_address)		#getNodeInfo() function call


	"""function to retrieve node's permissions on RecordsKeeper Blockchain"""

	def permissions():							#permissions() function definition

		headers = { 'content-type': 'application/json'}

		payload = [
		 	{ "method": "listpermissions",
		      "params": [],
		      "jsonrpc": "2.0",
		      "id": "curltext",
		      "chain_name": chain
		    }]

		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()
		
		pms_count = len(response_json[0]['result'])
		
		permissions = []

		for i in range(0, pms_count):
			permissions.append(response_json[0]['result'][i]['type'])

		return permissions;							#returns list of permissions

	#result = permissions()							#permissions() function call


	"""function to retrieve pending transactions information on RecordsKeeper Blockchain"""

	def getpendingTransactions():						#getpendingTransactions() function call

		headers = { 'content-type': 'application/json'}

		payload = [
		 	{ "method": "getmempoolinfo",
		      "params": [],
		      "jsonrpc": "2.0",
		      "id": "curltext",
		      "chain_name": chain
		    }]

		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()
			
		tx_count = response_json[0]['result']['size']		#store tx count

		headers = { 'content-type': 'application/json'}

		payload = [
		 	{ "method": "getrawmempool",
		      "params": [],
		      "jsonrpc": "2.0",
		      "id": "curltext",
		      "chain_name": chain
		    }]

		response2 = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json2 = response2.json()
			
		tx = []

		for i in range(0, tx_count):
			tx.append(response_json2[0]['result'])
		
		return tx_count, tx;					#returns tx and tx count

	#signedmessage = signMessage(private_key, message)							#getPrivateKey() function call


	# """function to verify message on RecordsKeeper Blockchain"""

	# def verifyMessage(address, signedMessage, message):

	# 	headers = { 'content-type': 'application/json'}

	# 	payload = [
	# 	 	{ "method": "verifymessage",
	# 	      "params": [address, signedMessage, message],
	# 	      "jsonrpc": "2.0",
	# 	      "id": "curltext",
	# 	      "chain_name": chain
	# 	    }]

	# 	response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
	# 	response_json = response.json()
			
	# 	verifiedMessage = response_json[0]['result']

	# 	if verifiedMessage is True:
	# 		validity = "Yes, message is verified"
	# 	else:
	# 		validity = "No, signedMessage is not correct"

	# 	return validity;												#returns private key

	# #validity = verifyMessage(address, signedMessage, message)							#getPrivateKey() function call


	# """function to retrieve wallet information on RecordsKeeper Blockchain"""

	# def retrieveWalletinfo():

	# 	headers = { 'content-type': 'application/json'}

	# 	payload = [
	# 	 	{ "method": "getwalletinfo",
	# 	      "params": [],
	# 	      "jsonrpc": "2.0",
	# 	      "id": "curltext",
	# 	      "chain_name": chain
	# 	    }]

	# 	response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
	# 	response_json = response.json()
			
	# 	balance = response_json[0]['result']['balance']
	# 	tx_count = response_json[0]['result']['txcount']
	# 	unspent_tx = response_json[0]['result']['utxocount']

	# 	return balance, tx_count, unspent_tx;												#returns private key

	# #validity = verifyMessage(address, signedMessage, message)							#getPrivateKey() function call
