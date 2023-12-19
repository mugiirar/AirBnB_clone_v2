#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class TestConsole(unittest.TestCase):
    def test_quit(self):
        """Test quit command input"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.consol.onecmd("quit")
            self.assertEqual('', mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
