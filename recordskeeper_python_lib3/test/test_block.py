import unittest
import yaml
import json
from recordskeeper_python_lib3 import block
from recordskeeper_python_lib3.block import Block

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

class BlockTest(unittest.TestCase):

    def test_block_info(self):
        
        size = Block.blockinfo(self, "100")
        block_size = json.loads(size)
        blocksize = block_size['size']
        self.assertGreaterEqual(blocksize, 280)

    def test_retrieveBlocks(self):

        txcount = Block.retrieveBlocks(self, "10-20")
        tx_count = json.loads(txcount)
        blocktxcount = tx_count['tx count'][0]
        self.assertGreaterEqual(blocktxcount, 1)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BlockTest)
    unittest.TextTestRunner(verbosity=2).run(suite)