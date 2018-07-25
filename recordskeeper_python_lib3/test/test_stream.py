import unittest
import yaml
import binascii
import json
from recordskeeper_python_lib3 import stream
from recordskeeper_python_lib3.stream import Stream

import sys

import os.path

if (os.path.exists("config.yaml")):
   with open("config.yaml", 'r') as ymlfile:
      cfg = yaml.load(ymlfile)
      
      network = cfg['network']

      url = network['url']
      user = network['rkuser']
      password = network['passwd']
      chain = network['chain']
      net = address.network
else:
   
   url = os.environ['url']
   user = os.environ['rkuser']
   password = os.environ['passwd']
   chain = os.environ['chain']
   net = os.environ 

class StreamTest(unittest.TestCase):


    def test_publish(self):
        
        txid = Stream.publish(self, net['miningaddress'], net['stream'], net['testdata'], "This is test data")
        tx_size = sys.getsizeof(txid)
        self.assertEqual(tx_size, 113)

    def test_retrieve_with_txid(self):

        result = Stream.retrieve(self, net['stream'], net['dumptxid'])
        self.assertIsNotNone(result)


    def test_retrieve_with_id_address(self):

        result = Stream.retrieveWithAddress(self, net['stream'], net['miningaddress'], 10)
        address = json.loads(result)
        publisher_key = address['key'][0]
        self.assertIsNotNone(publisher_key)
    
    def test_retrieve_with_key(self):

        result = Stream.retrieveWithKey(self, net['stream'], net['testdata'], 10)
        key = json.loads(result)
        publisher_data = key['data'][0]
        self.assertIsNotNone(publisher_data)

    def test_verifyData(self):

        result = Stream.verifyData(self, net['stream'], net['testdata'], 100)
        self.assertEqual(result, "Data is successfully verified.")

    def test_retrieveItems(self):
        
        result = Stream.retrieveItems(self, net['stream'], 10)
        items = json.loads(result)
        published_items = items['data'][0]
        self.assertIsNotNone(published_items)
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(StreamTest)
    unittest.TextTestRunner(verbosity=2).run(suite)