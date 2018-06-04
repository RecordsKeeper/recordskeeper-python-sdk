import unittest
import yaml
import binascii
from rklib3 import address


import sys


with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

net = address.network

class AddressTest(unittest.TestCase):

    def test_getaddress(self):
        
        address = Address.getAddress()
        address_size = sys.getsizeof(address)
        self.assertEqual(address_size, 83)

    def test_checkifvalid(self):

        checkaddress = Address.checkifValid(net['validaddress'])
        self.assertEqual(checkaddress, 'Address is valid')

    def test_failcheckifvalid(self):

        wrongaddress = Address.checkifValid(net['invalidaddress'])
        self.assertEqual(wrongaddress, 'Address is valid')

    def test_checkifmineallowed(self):

        checkaddress = Address.checkifMineAllowed(net['miningaddress'])
        self.assertEqual(checkaddress, 'Address has mining permission')

    def test_failcheckifmineallowed(self):

        wrongaddress = Address.checkifMineAllowed(net['nonminingaddress'])
        self.assertEqual(wrongaddress, 'Address has mining permission')

    def test_checkbalance(self):

        balance = Address.checkBalance(net['nonminingaddress'])
        self.assertEqual(balance, 5)

    def test_getmultisigwalletaddress(self):

        address = Address.getMultisigWalletAddress(2, "miygjUPKZNV94t9f8FqNvNG9YjCkp5qqBZ, mwDbTVQcATL263JwpoE8AHCMGM5hE1kd7m, mpC8A8Fob9ADZQA7iLrctKtwzyWTx118Q9")
        self.assertEqual(address, net['multisigaddress'])

    def test_getmultisigaddress(self):

        address = Address.getMultisigAddress(2,  "miygjUPKZNV94t9f8FqNvNG9YjCkp5qqBZ, mwDbTVQcATL263JwpoE8AHCMGM5hE1kd7m, mpC8A8Fob9ADZQA7iLrctKtwzyWTx118Q9" )
        self.assertEqual(address, net['multisigaddress'])

    def test_importaddress(self):

        address = Address.importAddress(net['miningaddress'])
        self.assertEqual(address, "Address successfully imported")

    def test_wrongimportaddress(self):

        address = Address.importAddress(net['wrongimportaddress'])
        self.assertEqual(address, "Invalid Rk address or script")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AddressTest)
    unittest.TextTestRunner(verbosity=2).run(suite)