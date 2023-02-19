import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get_normal(self):
        self.assertEqual(arrs.get([1, 2, 3], 2, "test"), 3)

    def test_get_negative_index(self):
        self.assertEqual(arrs.get([1, 2, 3], -2, "test"), "test")

    def test_get_IndexError(self):
        with self.assertRaises(IndexError):
            arrs.get([], 0, "test"), "test"

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_slice_zero_length(self):
        self.assertEqual(arrs.my_slice([]), [])

    def test_slice_negative_length(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], -4, -2), [1])

    def test_slice_normalazied_start(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])
