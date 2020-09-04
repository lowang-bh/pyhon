#!/usr/bin/env python

import unittest

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lenths = [len(s) for s in strs]
        if not lenths:
            return ""
        minLen = min(lenths)
        retStr = []
        for i in xrange(minLen):
            s = [str[i] for str in strs]
            if len(set(s)) != 1:
                break
            else:
                retStr.append(s[0])
        
        return "".join(retStr)
        
  
class SolutionTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        
    def tearDown(self):
        pass
    
    def test_case_null(self):
        self.assertEqual(self.s.longestCommonPrefix([]),"")
    
    def test_case_one(self):
        self.assertEqual(self.s.longestCommonPrefix(["a"]),"a")
    
    def test_case_common(self):
        self.assertEqual(self.s.longestCommonPrefix(["flower","flow","flight"]), "fl")
        self.assertEqual(self.s.longestCommonPrefix(["dog","racecar","car"]), "")


if __name__ == "__main__":
    unittest.main()

