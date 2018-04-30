"""Library to work with RecordsKeeper streams.

   You can retrieve block information by using block class.
   You just have to pass parameters to invoke the pre-defined functions."""

""" import requests, json and HTTPBasicAuth packages"""

import requests
import json
from requests.auth import HTTPBasicAuth
import yaml


""" Entry point for accessing Block class resources.

	Import values from config file."""

with open("config.yaml", 'r') as ymlfile:
	cfg = yaml.load(ymlfile)

url = cfg['testnet']['url']
user = cfg['testnet']['rkuser']
password = cfg['testnet']['passwd']
chain = cfg['testnet']['chain']



"""Block class to access block information"""

class Block:

	
	block_height = input("enter block height:")  							#variable to store the height of the block
	
	"""function to get a particular block"""

	def blockinfo(block_height):											#blockinfo function definition
		headers = { 'content-type': 'application/json'}


		payload = [
		         { "method": "getblock",
		          "params": [block_height],
		          "jsonrpc": "2.0",
		          "id": "curltext",
		          "chain_name": chain
		          }]
		response = requests.get(url, auth=HTTPBasicAuth(user, password), data = json.dumps(payload), headers=headers)
		response_json = response.json()

		tx_count = len(response_json[0]['result']['tx'])					#variable returns block's transaction count
		miner = response_json[0]['result']['miner']							#variable returns block's miner 
		size = response_json[0]['result']['size']							#variable returns block's size
		nonce = response_json[0]['result']['nonce']							#variable returns block's nonce
		blockHash = response_json[0]['result']['hash']						#variable returns blockhash
		
		tx = []																#list to store transaction ids

		
		for i in range(0, tx_count):
			
			tx.append(response_json[0]['result']['tx'][i])					#appends transaction ids into tx list
			


		return  tx_count, tx, miner, size, nonce, blockHash;

	
	tx_count, tx, miner, size, nonce, blockHash = blockinfo(block_height)	#call to blockinfo function 

	
	print("Block miner's address: ",miner)									#print block's miner
	print("Block size: ",size)												#print block's size
	print("Nonce: ",nonce)													#print block's nonce
	print("Block Hash: ",blockHash)											#print block's hash
	print("Block Transactions count: ",tx_count)							#print block's transaction count
	print("Block Transactions: ",tx)										#print block's transactions
