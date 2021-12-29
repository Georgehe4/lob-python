import unittest
import os
import lob
import pytest


class TestAddressFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = os.environ.get('LOB_API_KEY')


    def test_create_address(self):
        address = lob.Address.create(
            name='Lob',
            address_line1='185 Berry Street',
            address_line2='Suite 1510',
            address_city='San Francisco',
            address_zip='94017',
            address_state='CA',
            address_country='US'
        )

        self.assertTrue(isinstance(address, lob.Address))
        self.assertEqual(address.name, 'LOB')

    def test_list_addresses(self):
        addresses = lob.Address.list()
        self.assertTrue(isinstance(addresses.data[0], lob.Address))
        self.assertEqual(addresses.object, 'list')

    def test_list_addresses_total_count(self):
        addresses = lob.Address.list(include=['total_count'])
        self.assertTrue(isinstance(addresses.data[0], lob.Address))
        self.assertEqual(addresses.object, 'list')
        self.assertTrue(addresses['total_count'])

    def test_list_addresses_limit(self):
        addresses = lob.Address.list(limit=2)
        self.assertTrue(isinstance(addresses.data[0], lob.Address))
        self.assertEqual(len(addresses.data), 2)

    def test_list_address_fail(self):
        with pytest.raises(lob.error.InvalidRequestError):
            lob.Address.list(foobar=1000)

    def test_create_addresss_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Address.create)

    def test_retrieve_address(self):
        address = lob.Address.retrieve(id=lob.Address.list().data[0].id)
        self.assertTrue(isinstance(address, lob.Address))

    def test_retrieve_address_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Address.retrieve, id='test')

    def test_delete_address(self):
        address = lob.Address.create(
            name='Lob',
            address_line1='185 Berry Street',
            address_line2='Suite 1510',
            address_city='San Francisco',
            address_zip='94017',
            address_state='CA',
            address_country='US'
        )
        
        delAddr = lob.Address.delete(id=address.id)
        self.assertEqual(address.id, delAddr.id)
