import unittest
import yaml
import pyrklib
from pyrklib.address import Address

import stream


with open("config.yaml", 'r') as ymlfile:
	cfg = yaml.load(ymlfile)


class BlockTest(unittest.TestCase):


    def test_block_info(self):
        
    	tx_count, tx, miner, size, nonce, blockHash = blockinfo(block_height)
    
    print(tx_count)
    print(tx)
    print(miner)
    print(size)
    print(nonce)
    print(blockHash)


    def test_error(self):
        raise RuntimeError('Test error!')

if __name__ == '__main__':
    unittest.main()