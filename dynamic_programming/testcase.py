import unittest

from reverse_sorted_arr_search_an_element import search
from minim_length_unsorted_subarr import unsorted_subarray

class Test(unittest.TestCase):
	def test_01(self):
		arr = [3, 4, 5, 1, 2]
		n = len(arr)
		assert -1 == search(arr, 0, n-1, 10)

	def test_02(self):
		arr = [7, 8, 9, 1, 2, 3, 4]
		s, e = unsorted_subarray(arr, len(arr))
		assert s == 0

	# @unittest.skip("msg")
	# @unittest.expectedFailure
	def test_03(self):
		arr = [7, 8, 9, 1, 2, 3, 4]
		s, e = unsorted_subarray(arr, len(arr))
		self.assertEqual(e, len(arr))

	def test_04(self):
		arr = [1, 2, 3, 4, 7, 8, 9]
		s, e = unsorted_subarray(arr, len(arr))
		assert s == None


if __name__ == '__main__':
	unittest.main()

