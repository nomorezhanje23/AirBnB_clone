#!/usr/bin/python

import datetime
import unittest

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    a = Amenity()

    def test_class_exists(self) -> None:
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), res)

    def test_user_inheritance(self) -> None:
        self.assertIsInstance(self.a, Amenity)

    def test_has_attributes(self) -> None:
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def test_types(self) -> None:
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
