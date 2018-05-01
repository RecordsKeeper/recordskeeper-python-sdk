"""Library to work with RecordsKeeper transactions.

   You can send, retrieve and verify transactions by using transaction class.
   You just have to pass parameters to invoke the pre-defined functions."""

""" import requests, json, HTTPBasicAuth, yaml, sys and binascii packages"""

import requests
import json
from requests.auth import HTTPBasicAuth
import yaml
import sys
import binascii

""" Entry point for accessing Transaction class resources.

	Import values from config file."""

with open("config.yaml", 'r') as ymlfile:
	cfg = yaml.load(ymlfile)

url = cfg['testnet']['url']
user = cfg['testnet']['rkuser']
password = cfg['testnet']['passwd']
chain = cfg['testnet']['chain']

#Transaction class to access stream related functions
class Transaction:
	 
	"""function to send transaction on RecordsKeeper Blockchain"""

	sender_address = input("Enter Sender Address: ") 				 #variable to store sender's address
	reciever_address = input("Enter Reciever Address: ")			 #variable to store reciever's address
	amount = float(input("Enter amount to send: "))					 #variable to store amount to be transferred


	def sendTransaction(sender_address, reciever_address, amount):		#sendTransaction function definition
		headers = { 'content-type': 'application/json'}


		payload = [
		         { "method": "createrawsendfrom",
		          "params": [sender_address, {reciever_address : amount}, [], "send"],
		          "jsonrpc": "2.0",
		          "id": "curltext",
		          "chain_name": chain
		          }]
		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()

		
		return response_json[0]['result']				# return transaction id

	
	txid = sendTransaction(sender_address, reciever_address, amount)	#call to function sendTransaction

	
	print ("Transaction id: ",txid)									#prints transaction id of sent transaction

	"""function to create transaction hex on RecordsKeeper Blockchain"""

	sender_address = input("Enter sender's address: ")					#sender's address
	reciever_address = input("Enter reciever's address: ")				#reciever's address
	amount = float(input('Enter amount: '))								#amount to transfer
	

	def createRawTransaction(sender_address, reciever_address, amount):		#createRawTransaction function definition

		headers = { 'content-type': 'application/json'}


		payload = [
		         { "method": "createrawsendfrom",
		          "params": [sender_address, {reciever_address : amount}, [], ''],
		          "jsonrpc": "2.0",
		          "id": "curltext",
		          "chain_name": chain
		          }]
		
		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()

		
		return response_json[0]['result']							# return transaction hex of raw transaction

	
	tx_hex = createRawTransaction(sender_address, reciever_address, amount)	#call to function createRawTransaction

	
	print ("Raw transaction hex is: ",tx_hex)						#prints transaction hex of raw transaction


	"""function to sign transaction on RecordsKeeper Blockchain"""

	txHex = input("Enter transaction hex: ")							#transaction Hex of raw transaction
	private_key = input("Enter private key: ")

	def signRawTransaction(txHex, private_key):							#signRawTransaction function definition		

		headers = { 'content-type': 'application/json'}


		payload = [
		         { "method": "signrawtransaction",
		          "params": [txHex, [], [private_key]],
		          "jsonrpc": "2.0",
		          "id": "curltext",
		          "chain_name": chain
		          }]
		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()

		return response_json[0]['result']['hex']	

	signed_hex = signRawTransaction(txHex, private_key)				#call to function signRawTransaction

	
	print ("Signed transaction hex is: ",signed_hex)					#prints signed hex of raw transaction


	"""function to send raw transaction on RecordsKeeper Blockchain"""

	signed_txHex = input("Enter signed transaction hex: ")

	def sendRawTransaction(signed_txHex):
		headers = { 'content-type': 'application/json'}


		payload = [
		         { "method": "sendrawtransaction",
		          "params": [signed_txHex],
		          "jsonrpc": "2.0",
		          "id": "curltext",
		          "chain_name": chain
		          }]

		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()

		return response_json[0]['result']	

	tx_id = sendRawTransaction(signed_txHex)					#call to function sendRawTransaction

	
	print ("Transaction id is: ",tx_id)								#prints transaction id of transaction

	"""function to send signed transaction on RecordsKeeper Blockchain"""

	def sendSignedTransaction():									#sendSignedTransaction function definition

		sender_address = input("Enter sender's address: ")
		reciever_address = input("Enter reciever's address: ")
		amount = float(input('Enter amount: '))
		private_key = input("Enter private key: ")
		

		def createRawTransaction(sender_address, reciever_address, amount):
			headers = { 'content-type': 'application/json'}


			payload = [
			         { "method": "createrawsendfrom",
			          "params": [sender_address, {reciever_address : amount}, [], ""],
			          "jsonrpc": "2.0",
			          "id": "curltext",
			          "chain_name": chain
			          }]
			
			response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
			response_json = response.json()

			
			return response_json[0]['result']				

		
		txHex = createRawTransaction(sender_address, reciever_address, amount)	
		
		def signRawTransaction(txHex, private_key):
			headers = { 'content-type': 'application/json'}


			payload = [
			         { "method": "signrawtransaction",
			          "params": [txHex, [], [private_key]],
			          "jsonrpc": "2.0",
			          "id": "curltext",
			          "chain_name": chain
			          }]

			response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
			response_json = response.json()

			return response_json[0]['result']['hex']	

		signed_tx_hex = signRawTransaction(txHex, private_key)			

		def sendRawTransaction(signed_tx_hex):							

			headers = { 'content-type': 'application/json'}


			payload = [
			         { "method": "sendrawtransaction",
			          "params": [signed_tx_hex],
			          "jsonrpc": "2.0",
			          "id": "curltext",
			          "chain_name": chain
			          }]

			response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
			response_json = response.json()

			return response_json[0]['result']	

		tx_id = sendRawTransaction(signed_tx_hex)						
		
		return tx_id;												

	transaction_id = sendSignedTransaction()						#call to sendSigned Transaction

	print(transaction_id)											#returns tx_id of sendSigned Transaction


	"""function to retrieve transaction on RecordsKeeper Blockchain"""

	tx_id = input("Enter Transaction id to retrieve information: ")			#tx_id of transaction to retrieve


	def retrieveTransaction(tx_id):											#retrieveTransaction function definition
		headers = { 'content-type': 'application/json'}


		payload = [
		         { "method": "getrawtransaction",
		          "params": [tx_id, 1],
		          "jsonrpc": "2.0",
		          "id": "curltext",
		          "chain_name": chain
		          }]
		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()

		
		sent_data = response_json[0]['result']['data']
		sent_amount = response_json[0]['result']['vout'][0]['value']
		reciever_address = response_json[0]['result']['vout'][0]['scriptPubKey']['addresses']

		return sent_data, sent_amount, reciever_address;					#returns data from retrieved transaction

	sent_data, sent_amount, reciever_address = retrieveTransaction(tx_id)	#call to function retrieveTransaction

	
	print ("Data sent in retrieved transaction: ", sent_data)						#prints sent data
	print ("Amount sent in retrieved transaction: ", sent_amount)					#prints sent amount
	print ("Reciever's address of the retrieved transaction: ", reciever_address)	#prints reciever's address	



	"""function to verify transaction on RecordsKeeper Blockchain"""

	address = input("Enter sender's address: ")							#sender's address of transaction to verify
	tx_id = input("Enter Transaction id to verify information: ")		#tx_id of transaction to verify


	def verifyTransaction(address, tx_id):					#verifyTransaction function definition
		headers = { 'content-type': 'application/json'}


		payload = [
		         { "method": "getaddresstransaction",
		          "params": [address, tx_id, True],
		          "jsonrpc": "2.0",
		          "id": "curltext",
		          "chain_name": chain
		          }]
		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()
		
		sent_amount = response_json[0]['result']['vout'][0]['amount']
		reciever_address = response_json[0]['result']['addresses']
		data = response_json[0]['result']['data']
		balance_amount = response_json[0]['result']['balance']['amount']

		fees = (abs(balance_amount) - sent_amount)

		return data, sent_amount, reciever_address, fees;				#returns data from verified transaction

	
	data, sent_amount, reciever_address, fees = verifyTransaction(address, tx_id)	#call to function sendSignedTransaction

	
	print ("Data sent in verified transaction: ", data)							#prints data of verified transaction
	print ("Amount sent in verified transaction: ", sent_amount)				#prints amount sent in verified transaction
	print ("Fees of verified transaction: ", fees)								#prints fees of verified transaction
	print ("Reciever's address of verified transaction: ", reciever_address)	#prints reciever's address of verofoed transaction

		
