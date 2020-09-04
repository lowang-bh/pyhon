import unittest


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        if len(self.nums) < self.k:
            return None

        # sorted(self.nums, reverse=True)
        self.nums.sort( reverse=True)
        print(self.nums)
        return self.nums[self.k - 1]


class MyTestCase(unittest.TestCase):
    
    def setUp(self):
        self.kthLargest = None
    def tearDown(self):
        pass
    def test_add(self):
        self.kthLargest = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(4, self.kthLargest.add(3))
        self.assertEqual(5, self.kthLargest.add(5))
        self.assertEqual(5, self.kthLargest.add(10))
        self.assertEqual(8, self.kthLargest.add(9))
        self.assertEqual(8, self.kthLargest.add(4))

    
    def test_add2(self):
        self.kthLargest = KthLargest(1, [])
        self.assertEqual(-3, self.kthLargest.add(-3))
        self.assertEqual(-2, self.kthLargest.add(-2))
        self.assertEqual(-2, self.kthLargest.add(-4))
        self.assertEqual(0, self.kthLargest.add(0))
        self.assertEqual(4, self.kthLargest.add(4))

    def test_add3(self):
        self.kthLargest = KthLargest(2, [])
        self.assertEqual(None, self.kthLargest.add(-3))
        self.assertEqual(-3, self.kthLargest.add(-2))
        self.assertEqual(-3, self.kthLargest.add(-4))
        self.assertEqual(-2, self.kthLargest.add(0))
        self.assertEqual(0, self.kthLargest.add(4))


if __name__ == '__main__':
    unittest.main()
