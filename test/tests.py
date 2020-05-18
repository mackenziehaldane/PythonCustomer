import unittest
from unittest.mock import MagicMock
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.EntitiesDatabaseMapping.CustomerDatabaseMapping import CustomerDatabaseMapping
from src.Entities.Customer import Customer


class TSITestsMock(unittest.TestCase):
    dataSourceFields = ["emailAddress", "firstName", "lastName", "password"]

    emailAddressPosition = 0
    firstNamePosition = 1
    lastNamePosition = 2
    passwordPosition = 3

    # doubling stub function
    def test_Stub(self):
        readCSVFile = ReadCSVFile()
        customerDatabaseMapping = CustomerDatabaseMapping()

        customerDatabaseMapping.setConfig(ConfigStub.ConfigStub())
        customerDatabaseMapping.dataSourceFields = []

        result = customerDatabaseMapping.getCustomerData()
        self.assertEqual(('derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'), result[0])

    # Doubling mock function
    def test_Mock(self):
        readCSVFile = ReadCSVFile()
        customerDatabaseMapping = CustomerDatabaseMapping()

        MockData = []
        MockData.append("derek.somerville@glasgow.ac.uk")
        MockData.append("Derek")
        MockData.append("Somerville")
        MockData.append("1234")

        customerDatabaseMapping.config.getConfig = MagicMock(return_value=MockData)
        customerDatabaseMapping.dataSourceFields = []

        result = customerDatabaseMapping.getCustomerData()
        self.assertEqual(('derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'), result[0])

    # Doubling fake function
    def test_Fake(self):
        customerData = []
        customerData.append("derek.somerville@glasgow.ac.uk")
        customerData.append("Derek")
        customerData.append("Somerville")
        customerData.append("1234")

        newCustomer = CustomerDatabaseMapping.createCustomer(self, customerData)
        result = newCustomer.emailAddress

        self.assertEqual('derek.somerville@glasgow.ac.uk', result)
