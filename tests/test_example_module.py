import unittest

from {{library_name}} import exceptions, ExampleModule

from .base import BaseTestCase


class TestExampleModule(BaseTestCase):
    """ Testing operation of the ExampleModule class
     """

    def test_init_example_module(self):
        """ Ensures that the twine class can be instantiated with a file
        """
        test_data_file = self.path + "test_data/.json"
        ExampleModule()

    def test_broken_json_twine(self):
        """ Ensures that an invalid json file raises an InvalidTwine exception
        """
        twine_file = self.path + "twines/invalid_json_twine.json"
        with self.assertRaises(exceptions.InvalidTwineJson):
            Twine(file=twine_file)


if __name__ == "__main__":
    unittest.main()
