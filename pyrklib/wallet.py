"""Library to work with RecordsKeeper wallet.

   You can send, retrieve and verify transactions by using transaction class.
   You just have to pass parameters to invoke the pre-defined functions."""

""" import requests, json, HTTPBasicAuth, yaml, sys and binascii packages"""

import requests
import json
from requests.auth import HTTPBasicAuth
import yaml
import sys
import binascii

""" Entry point for accessing Wallet class resources.

	Import values from config file."""

with open("config.yaml", 'r') as ymlfile:
	cfg = yaml.load(ymlfile)

url = cfg['testnet']['url']
user = cfg['testnet']['rkuser']
password = cfg['testnet']['passwd']
chain = cfg['testnet']['chain']


#Wallet class to access wallet related functions
class Wallet:

	"""function to create wallet on RecordsKeeper Blockchain"""

	def createWallet():										#createWallet() function definition
		
		headers = { 'content-type': 'application/json'}

		payload = [
		         { "method": "createkeypairs",
		          "params": [],
		          "jsonrpc": "2.0",
		          "id": "curltext",
		          "chain_name": chain
		          }]
		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()

		public_address = response_json[0]['result'][0]['address']				# returns public address of the wallet
		private_key = response_json[0]['result'][0]['privkey']					# returns private key of the wallet

		def importAddress(public_address):							#importAddress() function call

			headers = { 'content-type': 'application/json'}

			payload = [
		         { "method": "importaddress",
		          "params": [public_address, " ", False],
		          "jsonrpc": "2.0",
		          "id": "curltext",
		          "chain_name": chain
		          }]
			response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
			response_json = response.json()
			
			result = response_json[0]['result']
			return result;

		import_address = importAddress(public_address)
		return public_address, private_key;							#returns public and private key

	#public_address, private_key = createWallet()					#call to function createWallet()	



	"""function to retrieve private key of a wallet on RecordsKeeper Blockchain"""

	def getPrivateKey(public_address):								#getPrivateKey() function definition

		headers = { 'content-type': 'application/json'}

		payload = [
		 	{ "method": "dumpprivkey",
		      "params": [public_address],
		      "jsonrpc": "2.0",
		      "id": "curltext",
		      "chain_name": chain
		    }]

		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()
			
		private_key = response_json[0]['result']

		return private_key;												#returns private key

	#privkey = getPrivateKey(public_address)							#getPrivateKey() function call


	privkey = getPrivateKey(public_address)							#getPrivateKey() function call


	"""function to sign message on RecordsKeeper Blockchain"""

	def signMessage(private_key, message):

		headers = { 'content-type': 'application/json'}

		payload = [
		 	{ "method": "signmessage",
		      "params": [private_key, message],
		      "jsonrpc": "2.0",
		      "id": "curltext",
		      "chain_name": chain
		    }]

		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()
			
		signedMessage = response_json[0]['result']

		return signedMessage;												#returns private key

	#privkey = getPrivateKey(public_address)							#getPrivateKey() function call


	"""function to verify message on RecordsKeeper Blockchain"""

	def verifyMessage(address, signedMessage, message):

		headers = { 'content-type': 'application/json'}

		payload = [
		 	{ "method": "verifymessage",
		      "params": [address, signedMessage, message],
		      "jsonrpc": "2.0",
		      "id": "curltext",
		      "chain_name": chain
		    }]

		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()
			
		verifiedMessage = response_json[0]['result']

		if verifiedMessage is True:
			validity = "Yes, message is verified"
		else:
			validity = "No, signedMessage is not correct"

		return validity;												#returns private key

	#validity = verifyMessage(address, signedMessage, message)							#getPrivateKey() function call


	"""function to retrieve wallet information on RecordsKeeper Blockchain"""

	def retrieveWalletinfo():

		headers = { 'content-type': 'application/json'}

		payload = [
		 	{ "method": "getwalletinfo",
		      "params": [],
		      "jsonrpc": "2.0",
		      "id": "curltext",
		      "chain_name": chain
		    }]

		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()
			
		balance = response_json[0]['result']['balance']
		tx_count = response_json[0]['result']['txcount']
		unspent_tx = response_json[0]['result']['utxocount']

		return balance, tx_count, unspent_tx;												#returns private key

	#validity = verifyMessage(address, signedMessage, message)							#getPrivateKey() function call
