import unittest
import yaml
from pyrklib import *
from pyrklib.stream import Stream

import sys
# sys.path.append('C:\\Users\\Trinayan\\pythonsdk\\scripts')

#from stream import Stream

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


class StreamTest(unittest.TestCase):

    


    def test_publish(self):
        
        test_data = "This is test data".encode('utf-8')
        test_address = "mpC8A8Fob9ADZQA7iLrctKtwzyWTx118Q9"
        test_stream = "root"
        test_key = "test"

        hex_data = test_data. hex()

        txid = Stream.publish(test_address, test_stream, test_key, hex_data)

        tx_size = sys.getsizeof(txid)
        self.assertEqual(tx_size, 113)



    # def test_retrieve(self):


    #     test_data = "This is test data".encode('utf-8')
    #     test_address = "mpC8A8Fob9ADZQA7iLrctKtwzyWTx118Q9"
    #     test_stream = "root"
    #     test_key = "test"

    #     hex_data = test_data. hex()

    #     txid = Stream.publish(test_address, test_stream, test_key, hex_data)
    #     print(txid)
    #     tx_size = sys.getsizeof(txid)
    #     self.assertEqual(tx_size, 113)
    #     self.assertTrue(True)

    
    # def test_verify_with_key(self):
    #     self.assertTrue(True)

    # def test_verify_with_address(self):
    #     self.assertTrue(True)


    # def test_error(self):
    #     raise RuntimeError('Test error!')

if __name__ == '__main__':
    unittest.main()