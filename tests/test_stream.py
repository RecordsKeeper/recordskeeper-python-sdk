import unittest
import yaml
import sys
sys.path.insert(0, '/path/to/pythonsdk/scripts/stream.py')

import stream



with open("config.yaml", 'r') as ymlfile:
	cfg = yaml.load(ymlfile)


class StreamTest(unittest.TestCase):

    test_data =	"This is test data"
    test_address = "mpC8A8Fob9ADZQA7iLrctKtwzyWTx118Q9"
    test_stream = "root"
    test_key = "test"

    hex_data = test_data. hex()


    def test_publish(self):
        
    	txid = publish(test_address, test_stream, test_key, hex_data)
        tx_size = sizesys.getsizeof(txid)

        self.assertEqual(tx_size, 113)



    # def test_retrieve(self):
    #     self.assertTrue(True)

    
    # def test_verify_with_key(self):
    #     self.assertTrue(True)

    # def test_verify_with_address(self):
    #     self.assertTrue(True)


    # def test_error(self):
    #     raise RuntimeError('Test error!')

if __name__ == '__main__':
    unittest.main()